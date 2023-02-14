from fastapi import FastAPI

from src.web.routes import (
    link_routes,
)


# Core Application Instance
app = FastAPI(
    title="Oasys Plumber",
    version="v0.0.1",
)

# Add Routers
app.include_router(link_routes.router)
