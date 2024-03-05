#!/bin/bash
# posts a request to a server with the following parameters
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
