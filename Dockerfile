FROM python:3.11-slim

WORKDIR /app

# System-Abhängigkeiten installieren
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Python-Abhängigkeiten installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Konfiguration und Code kopieren
COPY config.yaml .
COPY openinsider_scraper.py .

# Verzeichnisse erstellen
RUN mkdir -p data .cache

# Nicht-Root-Benutzer erstellen
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Volumes definieren
VOLUME ["/app/data", "/app/.cache"]

# Healthcheck hinzufügen
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import os; exit(0 if os.path.exists('data') and os.access('data', os.W_OK) else 1)"

CMD ["python", "openinsider_scraper.py"]
