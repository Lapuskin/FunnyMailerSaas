from fastapi import APIRouter


def get_apps_router():
    router = APIRouter(prefix='/api/v1', tags=['api'])
    # router.include_router(notes_controller.router)

    return router