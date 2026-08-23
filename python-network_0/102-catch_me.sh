#!/bin/bash
# Makes a request that causes the server to respond with "You got me!"
curl -s -b "user_id=98" -X PUT 0.0.0.0:5000/catch_me
