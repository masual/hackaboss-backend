#!/bin/bash

until ping -c 1 -W 1 ${DATABASE_HOST:?missing environment variable. DATABASE_HOST must be set}
    do
        echo "Waiting for postgresql to ping..."
        sleep 1s
done

sleep 20s

# Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema
python ./manage.py migrate

# Get all parameters from CMD
exec "$@"
