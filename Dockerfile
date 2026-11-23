FROM ghcr.io/astral-sh/uv:0.13.7-python3.13-trixie-slim
WORKDIR /flask-app
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-install-project
COPY . .
EXPOSE 5000
CMD ["uv", "run", "gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "src.app:app"]
