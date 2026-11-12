FROM ghcr.io/astral-sh/uv:0.13.7-python3.13-trixie-slim
WORKDIR /flask-app
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-install-project
COPY . .
EXPOSE 5000
CMD ["uv", "run", "src/app.py"]
