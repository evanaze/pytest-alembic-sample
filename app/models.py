from sqlalchemy import Integer, Column, Identity
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class TestResult(Base):
    """Schema for DB"""

    __tablename__ = "test_results"
    test_uuid = Column(Integer, Identity(), primary_key=True)
    test_results = Column(JSONB)