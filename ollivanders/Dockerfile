FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /diagon-alley
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python3 manage.py collectstatic --noinput
RUN python3 manage.py migrate
