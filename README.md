# Health Checks for Python

This repository houses examples of health check functions for various Python
packages and libraries that connect to other systems (e.g. Databases, Caches,
Web APIs and so on). Why is your application down? Is it because Redis not responding?
The aim is to answer these questions.

# How to use this repository?

Take a template function, take it a motivation to implement a health check
in your codebase.

# Libraries Covered

## Databases and Cachess

### Redis

Redis is a popular K/V Store. We are using the PING command for checking system status.

 * [aioredis](https://github.com/aniruddha-adhikary/healthchecks-python/blob/master/healthchecks/redis/aioredis_healthcheck.py) -
 An asyncio-powered client for Redis
 * [redis-py](https://github.com/aniruddha-adhikary/healthchecks-python/blob/master/healthchecks/redis/redis_py_healthcheck.py) - 
 The most popular Redis client for Python
