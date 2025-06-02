FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY bot ./bot/
CMD ["python3", "-m", "bot.core"]

# Add environment config

# Ensure .env is copied

