import pytest
from sqlalchemy import (
    create_engine, MetaData, Table, Column,
    Integer, String, DateTime, select, func)
from datetime import datetime

# Для того чтобы сработал метод soft delete,
# добавила столбец deleted_at в таблицу users запросом:
# ALTER TABLE users ADD COLUMN deleted_at TIMESTAMP NULL;
DATABASE_URL = "postgresql://postgres:D0berman3@localhost:5432/QA"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

users = Table(
    "users", metadata,
    Column("user_id", Integer, primary_key=True),
    Column("user_email", String),
    Column("subject_id", Integer),
    Column("deleted_at", DateTime, nullable=True)
)


@pytest.fixture
def connection():
    conn = engine.connect()
    yield conn
    conn.close()


def test_add_user(connection):
    insert_user = users.insert().values(
        user_email="new_user@gmail.com", subject_id=3)
    result = connection.execute(insert_user)
    user_id = result.inserted_primary_key[0]

    query = select(users).where(
        users.c.user_id == user_id, users.c.deleted_at.is_(None))
    user = connection.execute(query).mappings().first()

    connection.execute(users.update().where(
        users.c.user_id == user_id).values(deleted_at=func.now()))

    assert user is not None
    assert user["user_email"] == "new_user@gmail.com"


def test_update_user(connection):
    insert_user = users.insert().values(
        user_email="old_email@gmail.com", subject_id=2)
    result = connection.execute(insert_user)
    user_id = result.inserted_primary_key[0]

    update_email = users.update().where(
        users.c.user_id == user_id).values(user_email="new_email@gmail.com")

    connection.execute(update_email)

    query = select(users.c.user_email).where(
        users.c.user_id == user_id, users.c.deleted_at.is_(None))
    updated_email = connection.execute(query).scalar_one()

    connection.execute(users.update().where(
        users.c.user_id == user_id).values(deleted_at=func.now()))
    assert updated_email == "new_email@gmail.com"


def test_soft_delete_user(connection):
    insert_user = users.insert().values(
        user_email="softdel@gmail.com", subject_id=5)
    result = connection.execute(insert_user)
    user_id = result.inserted_primary_key[0]

    connection.execute(users.update().where(
        users.c.user_id == user_id).values(deleted_at=func.now()))

    query = select(users.c.deleted_at).where(users.c.user_id == user_id)
    deleted_at = connection.execute(query).scalar_one()

    assert deleted_at is not None
    assert isinstance(deleted_at, datetime)
