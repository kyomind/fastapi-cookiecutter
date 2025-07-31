"""FastAPI application entry point."""

import logging

from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import setup_logging

# Setup logging
setup_logging()

# Get logger for this module
logger = logging.getLogger(__name__)

# Create FastAPI app based on environment
if settings.is_development:
    app = FastAPI(
        title=settings.APP_NAME,
        description="{{cookiecutter.project_name}} API",
        version="0.1.0",
    )
    logger.info("FastAPI app created in development mode")
else:
    # Hide API docs in production
    app = FastAPI(
        title=settings.APP_NAME,
        description="{{cookiecutter.project_name}} API",
        version="0.1.0",
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
    )
    logger.info("FastAPI app created in production mode")


@app.get("/")
async def root() -> dict:
    """
    Welcome message for the root route.

    Returns:
        dict: API welcome message
    """
    return {"message": "Welcome to {{cookiecutter.project_name}}"}

logger.info("FastAPI application initialized successfully")
