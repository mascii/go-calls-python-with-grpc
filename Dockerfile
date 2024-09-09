FROM python:3.12.5-slim

WORKDIR /app

COPY pyproject.toml /app
COPY uv.lock /app
COPY main.py /app
COPY gen/python /app/gen/python

RUN pip install --no-cache-dir uv
RUN uv sync --no-dev --locked

EXPOSE 50051

CMD ["uv", "run", "python", "main.py"]
