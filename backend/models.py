from sqlalchemy import Column, Integer, String, Float

from backend.database import Base


class CurrencyHistory(Base):
    __tablename__ = "currency_history"

    id = Column(Integer, primary_key=True, index=True)

    from_currency = Column(String)

    to_currency = Column(String)

    amount = Column(Float)

    converted_amount = Column(Float)

    rate = Column(Float)