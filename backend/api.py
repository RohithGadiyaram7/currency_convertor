import re

from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.database import get_db

from backend import schemas
from backend import crud

router = APIRouter()


@router.post("/convert")
def create_conversion(
    conversion: schemas.CurrencyCreate,
    db: Session = Depends(get_db)
):
    return crud.create_conversion(db, conversion)


@router.get("/history")
def get_history(
    db: Session = Depends(get_db)
):
    return crud.get_conversions(db)


@router.post("/ai-convert")
def ai_convert(
    request: dict,
    db: Session = Depends(get_db)
):

    text = request["text"]

    pattern = r"(?:convert\s+)?(\d+)\s+([A-Za-z]{3})\s+to\s+([A-Za-z]{3})"
    match = re.search(pattern, text, re.IGNORECASE)

    if not match:
        return {
            "error": "Invalid format"
        }

    amount = float(match.group(1))

    from_currency = match.group(2).upper()

    to_currency = match.group(3).upper()

    conversion = schemas.CurrencyCreate(
        amount=amount,
        from_currency=from_currency,
        to_currency=to_currency
    )

    return crud.create_conversion(db, conversion)