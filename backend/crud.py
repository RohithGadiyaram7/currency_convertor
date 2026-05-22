from sqlalchemy.orm import Session

from backend import models
from backend import schemas

from backend.currency_service import get_conversion_rate


def create_conversion(
    db: Session,
    conversion: schemas.CurrencyCreate
):
    rate = get_conversion_rate(
        conversion.from_currency,
        conversion.to_currency
    )

    converted_amount = conversion.amount * rate

    db_conversion = models.CurrencyHistory(
        from_currency=conversion.from_currency,
        to_currency=conversion.to_currency,
        amount=conversion.amount,
        converted_amount=converted_amount,
        rate=rate
    )

    db.add(db_conversion)

    db.commit()

    db.refresh(db_conversion)

    return db_conversion

def get_conversions(db: Session):
    return db.query(models.CurrencyHistory).all()