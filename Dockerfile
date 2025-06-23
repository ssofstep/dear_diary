FROM python:3.12-slim

WORKDIR /app



COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV SECRET_KEY=os.getenv("SECRET_KEY")

EXPOSE 8000
