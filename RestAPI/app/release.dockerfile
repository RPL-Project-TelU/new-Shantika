FROM python:3.9-buster

ENV PYTHONWRITEBYCODE = 1
ENV PYTHONBUFFERED = 1
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

RUN python --version
RUN pip --version

WORKDIR /app
COPY ./app /app

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get install openssl
EXPOSE 80
CMD ["python -m http.server 8000"]