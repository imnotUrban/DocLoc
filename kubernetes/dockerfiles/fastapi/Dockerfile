FROM python:3.11.6

#RUN apk add --no-cache gcc
#RUN apk update && apk add pkgconfig mariadb-dev

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./DocLoc .

EXPOSE "5001"

CMD ["uvicorn", "main:app", "--proxy-headers","--host", "0.0.0.0", "--port", "5001"]
