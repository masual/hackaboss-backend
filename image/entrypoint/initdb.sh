#!/bin/bash

until ping -c 1 -W 1 ${DATABASE_HOST:?missing environment variable. DATABASE_HOST must be set}
    do
        echo "Waiting for postgresql to ping..."
        sleep 1s
done

python ./manage.py migrate
python ./manage.py runserver 0.0.0.0:8000