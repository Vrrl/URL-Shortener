import logging
from fastapi import APIRouter, Depends, HTTPException, status

from src.application.services import GetLinkService, MakeLinkService
from src.application.interfaces import GetLinkUseCase, MakeLinkUseCase

router = APIRouter()


@router.get("/{key}")
def redirect_link(
    key: str, get_link_use_case: GetLinkUseCase = Depends(GetLinkService)
):
    """Redirect to the corresponding link"""
    return get_link_use_case.handle(key)


@router.post("/save")
def save_link(url: str, make_link_use_case: MakeLinkUseCase = Depends(MakeLinkService)):
    """save a new link"""
    return make_link_use_case.handle(url)
