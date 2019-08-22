# Health Checks for Python

This repository houses examples of health check functions for various Python
packages and libraries that connect to other systems (e.g. Databases, Caches,
Web APIs and so on). Why is your application down? Is it because Redis not responding?
The aim is to answer these questions.

# How to use this repository?

Take a template function, take it a motivation to implement a health check
in your codebase.

 * Make sure to consider timeouts, and use proper timeouts for every health check.
 Otherwise your health check itself might hand up, waiting endlessly.

# Libraries Covered

## Databases and Caches

### Relational Databases

 * [databases](https://github.com/aniruddha-adhikary/healthchecks-python/blob/master/healthchecks/relational_db/databases_healthchecks.py) -
 An asyncio wrapper for PostgreSQL, MySQL etc.
 * [django](https://github.com/aniruddha-adhikary/healthchecks-python/blob/master/healthchecks/relational_db/django_healthchecks.py) -
 The most popular web framework in Python.
 * [sqlalchemy](https://github.com/aniruddha-adhikary/healthchecks-python/blob/master/healthchecks/relational_db/sqlalchemy_healthchecks.py) - 
 The Python ORM that everyone loves
 * [psycopg2](https://github.com/aniruddha-adhikary/healthchecks-python/blob/master/healthchecks/relational_db/psycopg2_healthchecks.py) - 
 The de-facto PostgreSQL driver for Python


### Redis

Redis is a popular K/V Store. We are using the PING command for checking system status.

 * [aioredis](https://github.com/aniruddha-adhikary/healthchecks-python/blob/master/healthchecks/redis/aioredis_healthcheck.py) -
 An asyncio-powered client for Redis
 * [redis-py](https://github.com/aniruddha-adhikary/healthchecks-python/blob/master/healthchecks/redis/redis_py_healthcheck.py) - 
 The most popular Redis client for Python
