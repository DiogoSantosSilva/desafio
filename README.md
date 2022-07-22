# Run project

## General info
This project is a simple Book API to get and rate books

## Setup
To run this project, install it locally docker-compose:

```
 docker-compose up --detach
```

Check if the project is running in background

```
 docker ps
```

With the project running is necessary to run the migrations for the database

```
docker-compose exec web python manage.py migrate
``` 

To run the tests run the following command 

```
docker-compose exec web pytest
``` 

To access the API is necessary to open the browser on http://localhost:8000 

## Technologies
Project is created with:
* Django: 3.2

* Django-Rest-Framework: 3.13.1

