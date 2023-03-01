from fastapi import FastAPI

from src.web.routes import link_routes, misc_routes

# Core Application Instance
app = FastAPI(
    title="URL Shortener",
    version="v0.0.1",
)

# Add Routers
app.include_router(misc_routes.router)
app.include_router(link_routes.router)
