#! /usr/bin/python
import time
hosts_direction = '/private/etc/hosts'
block_sites = ['www.facebook.com', 'www.youtube.com',
               'www.pepper.pl', 'www.goodreads.com',
               'www.netflix.com', 'www.zalando.pl', 'www.instagram.com']
lin = '0.0.0.0'

running = False
userInp = input('start? ')


def start():

    with open(hosts_direction, 'r+') as file:
        content = file.read()
        for website in block_sites:
            if website in content:
                pass

            else:
                file.write(lin + " " + website + "\n")


def stop():

    with open(hosts_direction, 'r+') as file:
        content_all = file.readlines()
        file.seek(0)
        for line in content_all:
            if not any(website in line for website in block_sites):
                file.write(line)
        file.truncate()


if userInp == 'y':
    print('Focus ON')
    running = True
    start()

while running:
    stopInp = input('stop? ')

    if stopInp == 'y':
        print('Odmrozenie za 10min')
        time.sleep(time.localtime().tm_min + 10)
        print('Focus OFF')
        running = False
        stop()
