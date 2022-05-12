# check if docker is installed

import os

if os.system('docker --version') != 0:
    print('Docker is not installed. Please install docker first.')
    exit(1)

# build the docker image
os.system('docker build -t andrerc1/ansible .')

# start the docker compose
os.system('docker-compose up -d')

