FROM python:3.13-slim AS build
COPY --from=ghcr.io/astral-sh/uv:0.13.7 /uv /usr/local/bin/uv
WORKDIR /app
ENV UV_PYTHON_DOWNLOADS=never UV_LINK_MODE=copy
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev --no-install-project --no-cache

FROM python:3.13-slim
WORKDIR /app
ENV PATH="/app/.venv/bin:$PATH" PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
RUN groupadd --system journal && useradd --system --gid journal --home-dir /nonexistent journal
COPY --from=build /app/.venv .venv
COPY app app
COPY migrations migrations
COPY alembic.ini .
USER journal
CMD ["python", "-m", "app.main", "bot"]