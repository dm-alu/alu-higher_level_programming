#!/bin/bash
# Sends a request to the URL given as argument and displays the size of the body in bytes
curl -s "$1" | wc -c
