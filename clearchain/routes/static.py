from pathlib import Path

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from jinja2 import Environment, FileSystemLoader
from starlette.responses import Response

from ..models.schemas import Settings

router = APIRouter()
STATIC_DIR = Path(__file__).parent.parent / "static"

# Configure templates with custom delimiters to avoid conflicts
templates = Jinja2Templates(directory=str(STATIC_DIR))
templates.env = Environment(
    loader=FileSystemLoader(str(STATIC_DIR)),
    autoescape=True,
    block_start_string="[[%",
    block_end_string="%]]",
    variable_start_string="[[",
    variable_end_string="]]",
)

# Content type mapping for static files
CONTENT_TYPES = {
    ".js": "application/javascript",
    ".ico": "image/x-icon",
    ".html": "text/html",
    ".css": "text/css",
}


def get_static_file(filepath: Path, content_type: str | None = None) -> FileResponse:
    """
    Helper function to serve static files with proper error handling and caching.

    Args:
        filepath: Path to the static file
        content_type: Optional content type override

    Returns:
        FileResponse with appropriate headers

    Raises:
        HTTPException if file not found
    """
    if not filepath.is_file():
        raise HTTPException(status_code=404, detail="File not found")

    headers = {
        "Cache-Control": "public, max-age=3600",
        "Content-Type": content_type
        or CONTENT_TYPES.get(filepath.suffix, "application/octet-stream"),
    }

    return FileResponse(filepath, headers=headers)


@router.get("/", response_class=HTMLResponse)
async def root(request: Request) -> Response:
    """Serve the main index.html template."""
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/main.js")
async def main_js() -> FileResponse:
    """Serve the main JavaScript file."""
    return get_static_file(STATIC_DIR / "main.js")


@router.get("/base.js")
async def base_js() -> FileResponse:
    """Serve the base JavaScript file."""
    return get_static_file(STATIC_DIR / "base.js")


@router.get("/telemetry.js")
async def telemetry_js() -> FileResponse:
    """
    Serve either telemetry.js or telemetry_disabled.js based on settings.
    """
    filename = "telemetry_disabled.js" if Settings.DISABLE_TELEMETRY else "telemetry.js"
    return get_static_file(STATIC_DIR / filename)


@router.get("/favicon.ico")
async def favicon() -> FileResponse:
    """Serve the favicon."""
    return get_static_file(STATIC_DIR / "favicon.ico")
