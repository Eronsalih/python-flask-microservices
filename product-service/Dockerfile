# Stage 1 - builder
FROM python:3.8.20-slim-bullseye AS builder

WORKDIR /build

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# Stage 2 - runtime
FROM python:3.8.20-slim-bullseye

WORKDIR /app

RUN groupadd --system appgroup && \
    useradd --system --gid appgroup appuser

COPY --from=builder /install /usr/local

COPY . .

RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 5002

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5002/health')" || exit 1

CMD ["python", "run.py"]