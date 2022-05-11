# check what os is running
import os
import sys

# check if the user is on linux
if os.name != 'posix': 
    print('This script is only for linux')
    sys.exit(1)

# check if the user is root
if os.geteuid() != 0: 
    print('This script must be run as root')
    sys.exit(1)

# check if the losetup command exists
if not os.path.isfile('/sbin/losetup'):
    print('losetup command not found')
    sys.exit(1)

# check if the raspbian.img exists
if not os.path.isfile('raspbian.img'):
    print('raspbian.img not found')
    print('Please download it from https://downloads.raspberrypi.org/raspbian_latest')
    print('and save it as raspbian.img')
    print('Then place it in the same directory as this script')
    sys.exit(1)

# run sudo losetup 
os.system('sudo losetup -Pf raspbian.img')

# get the device name
device = os.popen('losetup -j raspbian.img').read().strip()

# split the string to get the first part
device = device.split(' ')[0]

# remove the last character
device = device[:-1]

# remove the /dev/ from the string
device = device[5:]

print('Device: ' + device)


# generate random string
import random
import string

random_hash = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
print('Random hash: ' + random_hash)

# mount the device
os.system('sudo mkdir /mnt/' + random_hash)
os.system('sudo mount /dev/' + device + 'p2 /mnt/' + random_hash)

# create our root partition tar file
os.system('sudo tar cf root.tar -C /mnt/' + random_hash + ' .')

# unmount the device
os.system('sudo umount /mnt/' + random_hash)


    