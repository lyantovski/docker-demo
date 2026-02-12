FROM python:3.11-slim

ENV MODEL_ENGINE="gemini-2.0-flash"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY gpt3_script.py /app/

EXPOSE 5000

CMD ["python", "-E", "/app/gpt3_script.py"]

