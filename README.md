# Welcome to Hack a Boss Backend :whale2:

## Introduction

This repository was created with the aim of testing a **Backend** application (**Python**) with a **Database** (**PostgreSQL**) and a **Frontend** application (**Vue.js**).

## First Steps

* Install **Docker** : [Link](https://docs.docker.com/get-docker/)
* Install **Docker Compose** : [Link](https://docs.docker.com/compose/install/)

## Test Backend

- Build **backend container image**

```bash
sudo docker build -t hackaboss_backend:0.0.1 -f image/Dockerfile .
```

* Create **user-defined bridge network**

```
sudo docker network create ednonlabs-network
```

* Run **PostgreSQL**

```bash
sudo docker container run -d --name postgresql \
 -e POSTGRES_DB=ednonhackaboss \
 -e POSTGRES_USER=ednonhackaboss \
 -e POSTGRES_PASSWORD=maythe4thbewithyou \
 --network ednonlabs-network \
 postgres:9.6.18 
```

* Run **Backend**

```bash
sudo docker container run -d --name hackaboss-backend \
 -e DATABASE_NAME=ednonhackaboss \
 -e DATABASE_USER=ednonhackaboss \
 -e DATABASE_PASSWORD=maythe4thbewithyou \
 -e DATABASE_HOST=postgresql \
 -p 8081:8000 \
 --network ednonlabs-network \
hackaboss-backend:0.0.1
```

:eyes: If you want to test **Frontend** application, you should to take a look at [hackaboss-frontend](https://github.com/masual/hackaboss-frontend).

