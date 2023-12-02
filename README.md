# API example

Simple API on FastAPI

(python, [FastAPI](https://fastapi.tiangolo.com/), [SQLAlchemy](https://www.sqlalchemy.org/), [SQLite](https://sqlite.org/index.html))

\
Api has two main endpoints:
- save new note of current user
- get all notes of current user

\
Implemented:
- [OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/),
- api test with [PyTest](https://docs.pytest.org/en/7.4.x/),
- db admin interface with [SQLAdmin](https://aminalaee.dev/sqladmin/)
- versioning with [FastAPI-Versioning](https://github.com/DeanWay/fastapi-versioning)
- [json logging](https://github.com/madzak/python-json-logger) to a stream
- monitoring with [Sentry](https://docs.sentry.io/platforms/python/integrations/fastapi/) 
and [Prometheus](https://github.com/trallnag/prometheus-fastapi-instrumentator) 


# Interfaces

- Documentation - http://127.0.0.1:5000/v2/docs
- SQLAdmin interface - http://127.0.0.1:5000/admin  
- Sentry (registration is required) https://sentry.io/
- Prometheus is available at - http://127.0.0.1:9090  
- Grafana (currently not configured) - http://127.0.0.1:3000   


# Launching in Docker

Create and start container:
```bash
$ docker-compose up
```
Stop lifted containers:
```bash
$ docker-compose stop
```
Start stopped containers:
```bash
$ docker-compose start
```
Stop and delete containers and network:
```bash
$ docker-compose down
```
Remove app image:
```bash
$ docker rmi notes_api
```
Clear logs:
```bash
$ sudo rm -rf logs/*
```
