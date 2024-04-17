# Docker compose + Django + Postgres + React + Nginx

![docker](./img.jpg)

### 1. Description

This project demonstrates how to deploy a django react app with postgres db using nginx and docker compose.

### 2. Explanation

teh docker compose file containes 4 services:

#### I. nginx

this service serves 4 things

- static files
- protected media files
- django admin
- django api
- frontend

#### II. backend

this is a standard django rest framework app, but also serves media files and protect then, so only authenticated users can access files using presigned urls that expires after a while, it's similar to how amazon aws works

#### III. frontend

this is a standard react app that connect to the django rest framework api.

#### IV. database

this is a postgres database that is only accessile from inside docker network.

#### V. pgadmin

this is a pgadmin service that allows you to interact with the postgres db using web interface.

### 3. Prerequisites

- Docker and docker compose
- Git to clone the repo

### 4. Set up

###### Clone the repo:

`git clone https://github.com/yaserrar/docker-compose-nginx-django-react-postgres`

###### Set up environment variables:

set up environment variables for react and django, look at the .env.example

###### build and run conrainers:

`cd docker-compose-nginx-django-react-postgres`
`docker compose p --build -d`
`dcoker ps`
