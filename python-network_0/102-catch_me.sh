#!/bin/bash
# Makes a request that causes the server to respond with "You got me!"
curl -s -L -d "" -X PUT -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
