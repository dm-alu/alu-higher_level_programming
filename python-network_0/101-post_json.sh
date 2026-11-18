#!/bin/bash
# Sends a JSON POST request with the contents of the file given as second argument and displays the body
curl -s -X POST -H "Content-Type: application/json" --data-binary @"$2" "$1"
