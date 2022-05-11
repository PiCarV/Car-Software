# check what os is running
import os
import sys

# tell the user the script is starting
print('Starting image assembler...')

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

# check if custom-root.tar exists
if not os.path.isfile('custom-root.tar'):
    print('custom-root.tar not found')
    sys.exit(1)

# create a new raspbian image to modify
print('creating new raspbian image...')
os.system('sudo cp raspbian.img custom-raspbian.img')

# run sudo losetup 
print('generating new loop device...')
os.system('sudo losetup -Pf custom-raspbian.img')

#change custom-raspbian to the same permissions

# get the device name
print('getting device name...')
device = os.popen('losetup -j custom-raspbian.img').read().strip()

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

# re-assemble the image need to press y to confirm
print('re-assembling image...')
p = os.popen('sudo mkfs.ext4 /dev/' + device + 'p2', "w")

# mount the device
print('mounting root device...')
os.system('sudo mkdir /mnt/' + random_hash)
os.system('sudo mount /dev/' + device + 'p2 /mnt/' + random_hash)

# copy the files to the new image
print('copying files to new image...')
os.system('sudo tar xf custom-root.tar -C /mnt/' + random_hash)

#unmount the device
print('unmounting root device...')
os.system('sudo umount /mnt/' + random_hash)

# remove the losetup device
print('removing loop device...')
os.system('sudo losetup -d /dev/' + device)
