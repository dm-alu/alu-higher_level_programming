#!/bin/bash
# Displays all the HTTP methods the server at the URL given as argument accepts
curl -sI -X OPTIONS "$1" | grep -i '^Allow' | cut -d ' ' -f 2- | tr -d '\r'
