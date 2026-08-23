#!/bin/bash
# Sends a JSON POST request with the contents of a file
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
