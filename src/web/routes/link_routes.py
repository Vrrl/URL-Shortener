import logging
from fastapi import APIRouter, Depends, HTTPException, status

from src.application.services import GetLinkService, MakeLinkService
from src.application.interfaces import GetLinkUseCase, MakeLinkUseCase

router = APIRouter(tags=["links"])

@router.get("/{key}")
def redirect_link(
    key: str,
    get_link_use_case: GetLinkUseCase = Depends(GetLinkService)
):
    """Add Pipeline Route"""
    return get_link_use_case.handle(key)

@router.post("/save")
def save_link(
    url: str,
    make_link_use_case: MakeLinkUseCase = Depends(MakeLinkService)
):
    """Add Pipeline Route"""
    return make_link_use_case.handle(url)
