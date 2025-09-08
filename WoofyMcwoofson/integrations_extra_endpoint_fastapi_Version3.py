# Maintained by BoozeLee, 2025-09-08
from fastapi import APIRouter

router = APIRouter()

@router.get("/woof-extra", summary="Extra dog fact")
def woof_extra():
    return {
        "fact": "Dogs have unique nose prints, just like human fingerprints!",
        "endpoint": "/woof-extra"
    }