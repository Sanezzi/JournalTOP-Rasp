[project]
name = "journal-bot"
version = "1.0.0"
description = "Telegram-бот для расписания JOURNAL"
requires-python = ">=3.13,<3.14"
dependencies = [
    "aiogram>=3.22,<4",
    "alembic>=1.16,<2",
    "asyncpg>=0.30,<1",
    "pydantic>=2.13,<3",
    "pydantic-settings>=2.10,<3",
    "sqlalchemy>=2.0.43,<2.1",
    "httpx>=0.28,<1",
    "top-journal-sdk==0.4.0",
    "tzdata>=2025.2",
]

[dependency-groups]
dev = [
    "pip-audit>=2.9,<3",
    "pytest>=8.4,<10",
    "pytest-asyncio>=1.1,<2",
    "ruff>=0.12,<1",
]

[tool.pytest.ini_options]
asyncio_mode = "auto"
asyncio_default_fixture_loop_scope = "function"
testpaths = ["tests"]
pythonpath = ["."]

[tool.ruff]
target-version = "py313"
line-length = 100

[tool.ruff.lint]
select = ["E4", "E7", "E9", "F", "I"]
