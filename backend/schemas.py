from pydantic import BaseModel


class CurrencyCreate(BaseModel):
    from_currency: str

    to_currency: str

    amount: float