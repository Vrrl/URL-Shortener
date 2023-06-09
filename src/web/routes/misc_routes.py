import logging
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()


@router.get("/healthcheck")
def redirect_link():
    """Healthcheck route"""
    return "alive"
