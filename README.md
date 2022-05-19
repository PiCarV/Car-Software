# 🏎️ Car Software

This repository contains the tools to create a custom Raspberry Pi image that runs on a PiCarV. The software running in the image provides control over the PiCar and also streams video from the PiCar

## Features

- 🐋 Docker compose for reliability and orchestration
- 🤖 Ansible to automate the setup process
- 🖥️ Virtual Raspberry Pi emulator for ease of development

## How it works

- We run the setup.py with python this starts the process
- This then builds a docker image containing Ansible, a automation system for setting up computers
- Now the script runs a docker compose file, this creates 2 docker containers (virtual machines)
- One of these contains our ansible instance, the other contains a Raspberry Pi emulator
- The docker compose file also networks these containers together so they can communicate
- Once the Pi Emulator has started ansible connects to it using ssh and automatically sets up the operating system
- Once Ansible has finished we can convert the `distro.qcow2` to a bootable image

## Dependencies

These need to be installed to use the program. You can use winget (windows) or apt-get (linux).

### [🐍 Python 3](https://www.python.org/downloads/)

`winget install python3 -v 3.9.6150.0`

### [🐋 Docker](https://www.docker.com/get-started/)

`winget install -e --id Docker.DockerDesktop`

## How to use

1. Clone or download the repository

`git clone --depth=1 https://github.com/PiCarV/Car-Software.git`

2. Move into the Car-Software directory

`cd Car-Software`

3. Run the setup.py script

`python setup.py`

4. Monitor the process with Docker Desktop

Look for the stack called `car-software` you can click on the stack and you should see 2 containers inside. You can monitor the Ansible container, when it is done both containers should stop.

Expect this too take a long time, we're emulating a virtual raspberry pi!
You could technically set this up to configure a real raspberry pi too.

5. A file called PiCarV.img should appear in the dist folder. This is your final bootable image.
