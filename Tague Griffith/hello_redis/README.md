# Hello Redis

This directory contains an optional exercise for those of you not familiar with Redis,
building the classic Hello World with a Redis twist.  In this exercise, you will create a
Hello Redis program which connects to Redis, writes a message to the database, reads that
message back, then displays the message to the end user.  After that you will modify the
program to add a  counter to track the number of times the program executes.

The files `hello_redis.py` is a skeleton program to get you started.  It provides and explains
the boilerplate code needed to set up a connection to Redis.  If you get stuck
`hello_redis_solution.py` implements a solution to the exercise.  Feel free to study it or get
help from the training staff.

## Part One: Hello Redis

### Instructions
1. Prior to modifying `hello_redis.py`, run the program and see what happens
2. Add code to the program to store a Hello World message in Redis
3. Modify the code that prints the message to read the message from Redis instead of a constant string

### Further Activities
1. Do you understand what the function of the `decode_response` flag?
2. Try running the program with `decode_response=false`.  What happens?

## Part Two: 

### Instructions
1. Add code to `hello_redis.py` to track how often the program runs
2. Uncomment the code to print the run count message and modify to use the value from Redis
