import os

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from src.web.routes import link_routes, misc_routes


# Core Application Instance
app = FastAPI(
    title="URL Shortener",
    version=os.getenv("PROJECT_VERSION", "Unknown version"),
)
instrumentator = Instrumentator().instrument(app).expose(app)

# Add Routers
app.include_router(misc_routes.router)
app.include_router(link_routes.router)