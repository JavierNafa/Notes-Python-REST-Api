FROM python:3.8-alpine

WORKDIR /api

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
CMD ["celery","-A","main.celery","worker","-l","info","-c","1","-Q","default,high_priority"]