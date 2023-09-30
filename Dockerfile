FROM python:3.11

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7666

# CMD ["python", "main.py"]
CMD ["uvicorn", "main:app", "--port", "7666", "--reload"]