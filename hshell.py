#! /usr/bin/env python3
import subprocess
import os
import sys 

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m' 
    ENDC = '\033[0m'

username = os.getlogin()
username = username.replace('\'', '"')

print(' ')
print('Hakurei Shell - Version 1.00')
print('Gensokyo User : ' + username )
print('Dokcer : DinD_' +username )
print(' ')
print('You have those containers : ')

try:
    subprocess.call('docker exec -it ' + username + ' docker ps -a --format \'> {{.Image}}({{.ID}}) Status: {{.Status}}\'', shell=True)
except Exception as e:
    print('Do not have dind, please contact your system admin.')

print(' ')
print('please type "help" to see how to use hshell.')
print(' ')
while 1 :
    x = input(bcolors.FAIL + '>:' +bcolors.ENDC)
    if str(x)[0:4] == "conn" :
        try:
            subprocess.call('docker exec -it ' + username + ' docker exec -it '+ x[4:] + ' /bin/sh', shell=True)
        except Exception as err:
            print('Do not have this container.')

    elif str(x)[0:5] == "start" :
        try:
            subprocess.call('docker exec -it ' + username + ' docker start '+ x[5:], shell=True)
        except Exception as err:
            print('Do not have this container.')

    elif str(x)[0:4] == "stop" :
        try:
            subprocess.call('docker exec -it ' + username + ' docker stop '+ x[4:], shell=True)
        except Exception as err:
            print('Do not have this container.')

    elif str(x)[0:2] == "rm" :
        try:
            subprocess.call('docker exec -it ' + username + ' docker rm '+ x[2:], shell=True)
        except Exception as err:
            print('Do not have this container.')

    elif str(x)[0:4] == "list" :
        subprocess.call('docker exec -it ' + username + ' docker ps -a --format \'> {{.Image}}({{.ID}}) Status: {{.Status}}\'', shell=True)

    elif str(x)[0:4] == "help" :
        print('"conn <Name>" - goto container /bin/sh.')
        print('"list" - list all container. ')
        print('"start <Name>" - start container.')
        print('"rm <Name>" - remove container.' )
        print('"stop <Name>" - stop container.') 
        print('"exit" - leave hshell')

    elif x == 'exit':
        sys.exit()

    else:
        print('[Err] error command')



