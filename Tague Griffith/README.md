# WS2A - Building location aware application using Redis

## Description 

In this workshop, we are going to use the [geospatial data](https://redislabs.com/redis-best-practices/indexing-patterns/geospatial/) features of 
[Redis](https://www.redis.io) to index and query for data based on the location of a user.
We will use public data feeds from bike sharing systems around the world to index 
the station data, generate a kml file to test our work, then query for the location of a 
station.

## Requirements 

* Install [Python 3](https://www.python.org/downloads)
* Clone the [NABSA/gbfs](https://github.com/NABSA/gbfs) git repo.
* Accessible Redis instance running version 3.2.0 or later.
* (Optional) Install command line utility for finding current location

## Accessing Redis

There are a variety of ways to obtain a functioning Redis instance:

  * Local Installation (Mac OS and Linux)
  * Docker 
  * Cloud Redis Instance

You must be running a version a version 3.2.0 or later of Redis to access the
[GEO](https://redis.io/commands#geo) commands.  If you are running Windows, you will
need to run Redis via docker or use a Cloud instance.

### Local Installation

Install Redis using your OS's package or third-party port manager.  On Linux or Mac (brew)
you will usually install Redis 4.0.

### Docker

You can install Redis by running the following command:
`docker run -p 6379:6379 redis`

### Cloud Redis Instance

You can get a free Redis Enterprise Cloud instance by signing up
[here](https://app.redislabs.com/#/sign-up/cloud).


## Files

* `hello_redis` - optional exercise to get familiar with Redis
* `load_station_data.py` - skeleton file for indexing Bike Station Data
* `generate_station_kml.py` - skeleton file for generating KML overlay
* `query_location_data.py` - skeleton file for querying Redis data