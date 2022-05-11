# check what os is running
import os
import sys

# tell the user the script is starting
print('Starting image disassembler...')

# check if the user is on linux
if os.name != 'posix': 
    print('This script is only for linux')
    sys.exit(1)

# check if the user is root
if os.geteuid() != 0: 
    print('This script must be run as root')
    sys.exit(1)

# check if the losetup command exists
print('checking if losetup command exists...')
if not os.path.isfile('/sbin/losetup'):
    print('losetup command not found')
    sys.exit(1)

# check if the raspbian.img exists
print('checking if raspbian.img exists...')
if not os.path.isfile('raspbian.img'):
    print('raspbian.img not found')
    print('Please download it from https://downloads.raspberrypi.org/raspbian_latest')
    print('and save it as raspbian.img')
    print('Then place it in the same directory as this script')
    sys.exit(1)

# run sudo losetup 
print('generating new loop device...')
os.system('sudo losetup -Pf raspbian.img')

# get the device name
print('getting device name...')
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

random_root_hash = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
print('Random root hash: ' + random_root_hash)

random_boot_hash = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
print('Random boot hash: ' + random_boot_hash)

# mount the device
print('mounting root device...')
os.system('sudo mkdir /mnt/' + random_root_hash)
os.system('sudo mount /dev/' + device + 'p2 /mnt/' + random_root_hash)

print('mounting boot device...')
os.system('sudo mkdir /mnt/' + random_boot_hash)
os.system('sudo mount /dev/' + device + 'p1 /mnt/' + random_boot_hash)

# create our root partition tar file
print('creating root partition tar file...')
os.system('sudo tar cf root.tar -C /mnt/' + random_root_hash + ' .')

# create our boot partition tar file
print('creating boot partition tar file...')
os.system('sudo tar cf boot.tar -C /mnt/' + random_boot_hash + ' .')

# unmount the device
print('unmounting device...')
os.system('sudo umount /mnt/' + random_root_hash)
os.system('sudo umount /mnt/' + random_boot_hash)

# remove the losetup device
print('removing loop device...')
os.system('sudo losetup -d /dev/' + device)


    