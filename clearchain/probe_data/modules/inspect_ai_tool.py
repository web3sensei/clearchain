import asyncio
import importlib.util
import os

from loguru import logger

inspect_ai_task = (
    __file__.replace("inspect_ai_tool.py", "inspect_ai_task.py")
    .replace(os.getcwd(), "")
    .strip("/")
)


class Module:
    name = "Inspect AI"

    def __init__(self, prompt_groups: [], tools_inbox: asyncio.Queue, opts: dict = {}):
        self.tools_inbox = tools_inbox
        if not self.is_tool_installed():
            logger.error(
                "inspect_ai module is not installed. Please install it using 'pip install inspect_ai'"
            )
        self.opts = opts

    def is_tool_installed(self) -> bool:
        inspect_ai = importlib.util.find_spec("inspect_ai")
        return inspect_ai is not None

    async def _proc(self, command):
        env = os.environ.copy()
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=env,
            shell=True,
        )

        logger.info(f"Started {command}")

        # Read output as it becomes available
        async for line in process.stdout:
            logger.info(line.decode().strip())

        # Check for errors
        err = await process.stderr.read()
        if err:
            logger.error(err.decode().strip())

        await process.wait()
        logger.info(f"Command {command} {process}finished.")

    async def apply(self) -> []:
        port = self.opts.get("port", 8718)
        # Command to be executed
        command = f"inspect eval {inspect_ai_task} --model openai/gpt-4  --model-base-url=http://0.0.0.0:{port}/proxy"
        logger.info(f"Executing command: {command}")

        proc = asyncio.create_task(self._proc(command))
        is_empty = self.tools_inbox.empty()
        await asyncio.sleep(2)
        logger.info(f"Is inbox empty? {is_empty}")
        while not self.tools_inbox.empty():
            ref = self.tools_inbox.get_nowait()
            message, _, ready = ref["message"], ref["reply"], ref["ready"]
            yield message
            ready.set()
        logger.info(f"{self.name} tool finished.")
        await proc
