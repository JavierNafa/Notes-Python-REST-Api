

  

# NOTES API

A simple REST Api in Node js :)

Sorry for my bad English :(

  
  
  

<details  open="open">
<summary>Content</summary>
<ol>
<li>
<a  href="#about">About</a>
</li>
<li>
<a  href="#setup">Setup</a>
<ul>
<li><a  href="#requirements">Requirements</a></li>
<li><a  href="#installation">Installation</a></li>
</ul>
</li>
<li><a  href="#usage">Usage</a></li>
</ol>
</details>

  

## About

Simple REST Api for creating notes with authentication. This project was built with:

*  [Python](https://www.python.org/)

*  [Flask](https://flask.palletsprojects.com/en/1.1.x/)

*  [MongoDb](https://www.mongodb.com/)

*  [Redis](https://redis.io/)

*  [Docker](https://www.docker.com/)

* [Celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)

  

## Setup

### Requirements

* Python v3.8.5

* Flask v1.1.2

* Mongo v4.4

* Redis v6

* Docker v20.10

* Celery v5.0.5
  

For the tests

  

* unittest

  

### Installation

Install python and pip if you don't have it.

1. Create a virtual environment with conda, virtualenv  or other and activate it.

2. Clone the repo.
```
git clone https://github.com/JavierNafa/Notes-Python-REST-Api
```
3.  Run this command to install all the dependencies.
```
pip install -r requirements.txt
```
or
```
pip3 install -r requirements.txt
```

4. Create a file called .env in the root folder.

  

| Env name | Description |
| :----------- | :----------------------|
MONGO_HOST | The host of mongoDb. If you are going to run this without docker set the remote host or use the default ```localhost```. |
MONGO_PORT | The mongoDb port. Default ```27017```. |
MONGO_DB_NAME | The name of the mongo database. Default ```notes ```. |
REDIS_DB_INDEX | The redis database number. Default ```0```.|
REDIS_HOST | The host of redis. If you are going to run this without docker set the remote host or use the default ```localhost```.|
REDIS_PORT | The redis port. Default ```6379```.|
REDIS_EXPIRATION | The expiration time of each key in seconds. Default ```60```.|
TOKEN_KEY | JWT secret key. Example ``` supersecret123```. |
EMAIL_USER| The email to send a test mail.|
EMAIL_PASSWORD|Email password.|
EMAIL_SERVICE|The service supported by [smtplib](https://docs.python.org/3/library/smtplib.html)|
EMAIL_PORT|The port of the email service|
CELERY_RESULT_BACKEND| URI from the service for celery. Example ``` redis://127.0.0.1:6379/1```.|
CELERY_BROKER_URL|URI from the broker for celery. Example ``` redis://127.0.0.1:6379/1```.|
FLASK_PORT | The REST Api port . Default ``` 8000```.|
FLASK_DEBUG| Flag to enable the debug mode
ENV| Environment for flask.|

  
  

# Usage

### Without docker

1. Create the .env file with the above variables.

2. Make sure mongodb and redis are running first. After that, run 
```
python main.py
```
```
celery -A main.celery worker -l info -c 1 -Q default,high_priority
```
in the root folder.

3. Enter the following url in your favorite browser ```http://localhost:PORT/doc``` to see all routes.

4. Create a user ```/user```.

5. Log in ```/login```.

6. Use the token to authorize you. Example ```Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c```

7. You can now create, read, update and delete notes.

  

### With docker

1. Set the .env file only with  ```TOKEN_KEY``` , ```EMAIL```,```Celery``` and ```Flask``` variables.

3. Run ```docker-compose up``` in the root folder.

4. Follow steps 3-7 of the section without docker.

  

### Tests

The tests were maded with unittest.

1. First check that the connection with redis and mongodb is ok.

2. Run ```python -m unittest --buffer``` in the root folder.

  

## Thanks for reading this.