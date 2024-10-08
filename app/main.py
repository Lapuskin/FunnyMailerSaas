import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from router import get_apps_router
from src.config import common as app_settings


def get_application() -> FastAPI:
    application = FastAPI(
        title=app_settings.PROJECT_SETTINGS['PROJECT_NAME'],
        debug=app_settings.PROJECT_SETTINGS['DEBUG'],
        version=app_settings.PROJECT_SETTINGS['VERSION'],
    )
    application.include_router(get_apps_router())

    application.add_middleware(
        CORSMiddleware,
        allow_origins=app_settings.CORS_ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=app_settings.CORS_ALLOWED_METHODS,
        allow_headers=app_settings.CORS_ALLOWED_HEADERS,
    )
    return application


app = get_application()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)