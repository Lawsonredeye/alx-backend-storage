# 0x02. Redis basic

Redis is a cache system which can also be used as a database to store key value pairs.

It is the fastest when it comes to caching temporary data that would be discarded after usage and it uses a format of hashes.

## Basic Commands
GET
SET
MGET
MSET
LPUSH
RPUSH
LLEN
LRANGE
HMGET
HMSET

## Installation

```
sudo apt-get -y install redis-server
pip3 install redis
sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```
Use Redis in a container
Redis server is stopped by default - when you are starting a container, you should start it with: service redis-server start
