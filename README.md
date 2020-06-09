# hackaboss_backend
Python Backend

## Database configuration
### Python Backend
sudo docker network create ednonlabs-network
​
sudo docker container run -d --name postgresql \
 -e POSTGRES_DB=ednonhackaboss \
 -e POSTGRES_USER=ednonhackaboss \
 -e POSTGRES_PASSWORD=maythe4thbewithyou \
 --network ednonlabs-network \
 postgres:9.6.18 
​
sudo docker container run -d --name hackaboss-backend \
 -e DATABASE_NAME=ednonhackaboss \
 -e DATABASE_USER=ednonhackaboss \
 -e DATABASE_PASSWORD=maythe4thbewithyou \
 -e DATABASE_HOST=postgresql \
 -p 8081:8000 \
 --network ednonlabs-network \
hackaboss_backend:0.0.1