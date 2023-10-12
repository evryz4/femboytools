import json
import os
import hashlib
import urllib.request

starttext ='''
███████╗███████╗███╗░░░███╗██████╗░░█████╗░██╗░░░██╗████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
██╔════╝██╔════╝████╗░████║██╔══██╗██╔══██╗╚██╗░██╔╝╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
█████╗░░█████╗░░██╔████╔██║██████╦╝██║░░██║░╚████╔╝░░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
██╔══╝░░██╔══╝░░██║╚██╔╝██║██╔══██╗██║░░██║░░╚██╔╝░░░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
██║░░░░░███████╗██║░╚═╝░██║██████╦╝╚█████╔╝░░░██║░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
╚═╝░░░░░╚══════╝╚═╝░░░░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░\n'''

def showstarttext():
    print(starttext)

inputstyle = input('Choose input style: ')
def linuxinput(text):
    return input(text + '\n' + inputstyle + ' ')

while True:
    showstarttext()

    chose = linuxinput('''Choose any option:

1 - info about ip
2 - info about phone number
3 - generate sha256
4 - generate X zeros sha256''')

    if int(chose) in [1, 2, 3, 4]:
        if int(chose) == 1:
            ip = linuxinput('Input any ip:')
            try:
                url = "https://ipinfo.io/" + ip + "/json"
                getInfo = urllib.request.urlopen( url )
                infoList = json.load(getInfo)
                print("Ip: ", infoList["ip"])
                print("City: ", infoList["city"])
                print("Region: ", infoList["region"])
                print("Country: ", infoList["country"])
                print("Coords: ", infoList["loc"])
            except:
                print('Ip doesn`t exist')
        elif int(chose) == 2:
            number = linuxinput('Input any phone number:')
            print('Phone number: ' + number)
        elif int(chose) == 3:
            text = linuxinput('Input any text:')
            print('Hash: ' + hashlib.sha256(bytes(text, 'utf-8')).hexdigest())
        elif int(chose) == 4:
            x = int(linuxinput('Input X:'))
            text = linuxinput('Input any text:')
            hash = hashlib.sha256(bytes(text, 'utf-8')).hexdigest()
            while hash[0:x] != '0' * x:
                hash = hashlib.sha256(bytes(hash, 'utf-8')).hexdigest()
                print(hash)
            print('Hash found: ' + hash)
    else:
        print('Invalid input!')

    input('\nPress Enter for continue. ')

    os.system('cls')