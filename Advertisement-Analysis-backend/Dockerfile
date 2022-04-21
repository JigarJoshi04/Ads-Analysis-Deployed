FROM python:3.8.10

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update && apt-get install build-essential -y
RUN pip install --upgrade pip 
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
RUN chmod g+x ./guinicorn.sh
EXPOSE 5000

#CMD ["python", "app.py" ]
ENTRYPOINT ["./guinicorn.sh"]
