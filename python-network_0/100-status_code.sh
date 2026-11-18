#!/bin/bash
# Sends a request to the URL given as argument and displays only the status code
curl -so /dev/null -w "%{http_code}" "$1"
