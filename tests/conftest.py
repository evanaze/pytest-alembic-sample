from pytest_mock_resources import create_postgres_fixture

from app import models

alembic_engine = create_postgres_fixture(models.Base)
