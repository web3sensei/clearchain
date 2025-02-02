import base64
import io

import httpx
import matplotlib.pyplot as plt
from cache_to_disk import cache_to_disk
from tqdm import tqdm

from agentic_security.probe_data.models import ImageProbeDataset, ProbeDataset


def generate_image_dataset(
    text_dataset: list[ProbeDataset],
) -> list[ImageProbeDataset]:
    image_datasets = []

    # Iterate over the text datasets
    for dataset in text_dataset:
        # Generate images for each prompt in the dataset

        # Add a progress bar to the image generation process
        image_prompts = [
            generate_image(prompt)
            for prompt in tqdm(
                dataset.prompts, desc=f"Generating images for {dataset.dataset_name}"
            )
        ]
        # Create an ImageProbeDataset instance
        image_dataset = ImageProbeDataset(
            test_dataset=dataset,
            image_prompts=image_prompts,
        )

        # Append the image dataset to the list
        image_datasets.append(image_dataset)

    return image_datasets


@cache_to_disk()
def generate_image(prompt: str) -> bytes:
    """
    Generate an image based on the provided prompt and return it as bytes.

    Parameters:
        prompt (str): Text to display on the generated image.

    Returns:
        bytes: The image data in JPG format.
    """
    # Create a matplotlib figure
    fig, ax = plt.subplots(figsize=(6, 4))

    # Customize the plot (background color, text, etc.)
    ax.set_facecolor("lightblue")
    ax.text(
        0.5,
        0.5,
        prompt,
        fontsize=16,
        ha="center",
        va="center",
        wrap=True,
        color="darkblue",
    )

    # Remove axes for a cleaner look
    ax.axis("off")

    # Save the figure to a buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format="jpeg", bbox_inches="tight")
    buffer.seek(0)  # Reset buffer pointer

    # Close the figure to free resources
    plt.close(fig)

    # Return the image bytes
    return buffer.getvalue()


def encode(image: bytes) -> str:
    encoded_content = base64.b64encode(image).decode("utf-8")
    return "data:image/jpeg;base64," + encoded_content


class RequestAdapter:
    # Adapter of http_spec.LLMSpec

    def __init__(self, llm_spec):
        self.llm_spec = llm_spec
        if not llm_spec.has_image:
            raise ValueError("LLMSpec must have an image")

    async def probe(
        self, prompt: str, encoded_image: str = "", encoded_audio: str = "", files={}
    ) -> httpx.Response:
        encoded_image = generate_image(prompt)
        encoded_image = encode(encoded_image)
        return await self.llm_spec.probe(prompt, encoded_image, encoded_audio, files)

    fn = probe
