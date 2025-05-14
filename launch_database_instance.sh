#!/bin/bash



# MySQL
docker run -d --name mysql-api -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=testdb -p 3306:3306 mysql:8.0

# Redis
docker run -d --name redis-api -p 6379:6379 redis

