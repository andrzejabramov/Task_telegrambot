FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN ls -la /app/src/  # временно, для отладки
CMD ["python", "-m", "src.main"]