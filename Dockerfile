FROM python:3.11-slim
WORKDIR /app
COPY . .
EXPOSE 5000
RUN apt update -y && apt install sqlite3
RUN pip install flask
CMD ["python3", "app.py"]
