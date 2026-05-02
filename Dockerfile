FROM python:3.12-slim
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
ENV PATH="/root/.local/bin:$PATH"
RUN poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi
COPY . .