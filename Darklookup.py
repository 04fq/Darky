import requests,re
from colorama import *
import socket
import os
import platform
red = "\033[1;31m" 
blue = "\033[1;34m"
cyan = "\033[1;36m"
os.system('clear')
def Dark():
    print('indient')
print(f'''{red}
  ██████╗░░█████╗░██████╗░██╗░░██╗██╗░░░██╗
  ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝╚██╗░██╔╝
  ██║░░██║███████║██████╔╝█████═╝░░╚████╔╝░
  ██║░░██║██╔══██║██╔══██╗██╔═██╗░░░╚██╔╝░░
  ██████╔╝██║░░██║██║░░██║██║░╚██╗░░░██║░░░
  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░''')
print(f'{cyan} ------------------------------------------')
print(f' {red}[{blue}!!{red}] {cyan}By Wardencraz | i0.wf')
option= input(f''' {red}[{blue}01{red}] {cyan}DNS Lookup              {red}[{blue}10{red}] {cyan}Zone Transfer
 {red}[{blue}02{red}] {cyan}GeoIP Lookup            {red}[{blue}11{red}] {cyan}Bypass Cloudflare {red}[using {cyan}HatCloud{red}]
 {red}[{blue}03{red}] {cyan}Subnet Lookup           {red}[{blue}12{red}] {cyan}SubDomain Detector {red}[{cyan}@3h6h{red}]
 {red}[{blue}04{red}] {cyan}Whois Lookup {red}[CLOSED{red}]   {red}[{blue}13{red}] {cyan}CMS Filter {red}[{cyan}@eoq.z{red}]{blue}[SOON{blue}]                                             
 {red}[{blue}05{red}] {cyan}Port Scanner            {red}[{blue}14{red}] {cyan}Admin Login {red}[using {cyan}Breacher{red}]  
 {red}[{blue}06{red}] {cyan}HTTP Header             {red}[{blue}15{red}] {cyan}Email Gathering {red}[using {cyan}Infoga{red}]
 {red}[{blue}07{red}] {cyan}Host Finder             
 {red}[{blue}08{red}] {cyan}Shared DNS Server       
 {red}[{blue}09{red}] {cyan}Host DNS Finder
 {blue}[{red}??{blue}] {cyan}Select {red}? {blue}: ''')
if option == '1':
    os.system('clear')
    print(f'{cyan}[{red}-{cyan}] {red}D{blue}N{cyan}S {blue}L{blue}oo{cyan}k{red}u{blue}p')
    dns = input(f'{blue}[{red}?{blue}] {red}Enter IP/Domain {cyan}: ')
    dnslook = 'https://api.hackertarget.com/dnslookup/?q='+dns
    info = requests.get(dnslook)
    print(cyan,info.text)
elif option == '2':
    os.system('clear')
    print(f'{cyan}[{red}-{cyan}] {red}G{blue}E{cyan}O {blue}I{red}P{cyan}L{red}oo{blue}u{cyan}p')
    geoip = input(f'{blue}[{red}?{blue}] {red}Enter IP/Domain {cyan}: ')
    ipgeo = 'https://api.hackertarget.com/geoip/?q='+geoip
    info = requests.get(ipgeo)
    print(blue,info.text)
elif option == '3':
    os.system('clear')
    print(f'{cyan}[{red}-{cyan}] {red}S{blue}u{cyan}b{blue}n{red}e{cyan}t {blue}L{red}oo{blue}k{red}u{cyan}p')
    subnet0 = input(f'{blue}[{red}?{blue}] {red}Enter IP/Domain {cyan}: ')
    subnet = 'http://api.hackertarget.com/subnetcalc/?q='+subnet0
    info = requests.get(subnet)
    print(blue,info.text)
elif option == '4':
    os.system('clear')
    print(f'{red}cLoSeD')
elif option == '5':
    os.system('clear')
    print(f'{cyan}[{red}-{cyan}] {red}P{blue}o{cyan}r{blue}t {red}S{cyan}c{blue}a{red}nn{blue}e{red}r')
    port0 = input(f'{blue}[{red}?{blue}] {red}Enter IP/Domain {cyan}: ')
    port = 'https://api.hackertarget.com/nmap/?q='+port0
    info = requests.get(port)
    print(cyan,info.text)
elif option == '6':
    os.system('clear')
    print(f'{cyan}[{red}-{cyan}] {red}H{blue}TT{cyan}P {blue}H{red}e{cyan}a{blue}d{red}e{blue}r')
    http0 = input(f'{blue}[{red}?{blue}] {red}Enter IP/Domain {cyan}: ')
    header = 'https://api.hackertarget.com/httpheaders/?q='+http0
    info = requests.get(header)
    print(blue,info.text)
elif option == '7':
    os.system('clear')
    print(f'{cyan}[{red}-{cyan}] {red}H{blue}o{cyan}s{blue}t {red}F{cyan}i{blue}n{red}d{blue}e{red}r')
    host0 = input(f'{blue}[{red}?{blue}] {red}Enter IP/Domain {cyan}: ')
    host = 'https://api.hackertarget.com/hostsearch/?q='+host0
    info = requests.get(host)
    print(cyan,info.text)
elif option == '8':
    os.system('clear')
    print(f'{cyan}[{red}-{cyan}] {red}S{blue}h{cyan}a{blue}r{red}e{cyan}d {blue}D{red}N{blue}S {red}S{cyan}e{red}r{blue}v{red}e{cyan}r')
    shared0 = input(f'{blue}[{red}?{blue}] {red}Enter IP/Domain {cyan}: ')
    shared = 'https://api.hackertarget.com/findshareddns/?q='+shared0
    info = requests.get(shared)
    print(blue,info.text)
elif option == '9':
    os.system('clear')
    print(f'{cyan}[{red}-{cyan}] {red}H{blue}o{cyan}s{blue}t {red}D{cyan}N{blue}S {red}F{blue}i{red}n{cyan}d{red}e{blue}r')
    hostdnsfind = input(f'{blue}[{red}?{blue}] {red}Enter IP/Domain {cyan}: ')
    hostdns = 'https://api.hackertarget.com/mtr/?q='+hostdnsfind
    info = requests.get(hostdns)
    print(cyan,info.text)  
elif option == '10':
    os.system('clear')
    print(f'{cyan}[{red}-{cyan}] {red}Z{blue}o{cyan}n{blue}e {red}T{cyan}r{blue}a{red}n{blue}s{red}f{cyan}e{red}r')
    revip = input(f'{blue}[{red}?{blue}] {red}Enter IP/Domain {cyan}: ')
    zone = 'https://api.hackertarget.com/zonetransfer/?q='+revip
    info = requests.get(zone)
    print(blue,info.text)
elif option == '11':
    os.system('clear')
    domain = input(f'{blue}[{red}?{blue}] {red}Enter IP/Domain {cyan}: ')
    os.system('ruby ./Extensions/HatCloud.rb -b '+domain)
elif option == '12':
    A = '\033[1;10m'
    B = '\033[1;30m'
    C ='\033[1;36m'
    D =('='*40)
    print(f"""{A}{D}
    <>---<>---<>---<>---<>---<>---<>---<>---<>
    [*] Find out hidden paths on the site [*]  
    <>---<>---<>---<>---<>---<>---<>---<>---<>        
        >> Naplon ◕_◕ <<
    _   _             _             
    | \ | |           | |            
    |  \| | __ _ _ __ | | ___  _ __  
    | . ` |/ _` | '_ \| |/ _ \| '_ \ 
    | |\  | (_| | |_) | | (_) | | | |{C}
    |_| \_|\__,_| .__/|_|\___/|_| |_|
                | | instagram: 3h6h                 
                |_| snap: tv-of  
                    Telegram: naplon0 
    <>---<>---<>---<>---<>---<>---<>---<> 
    //Link must contain http or https\\
    <>---<>---<>---<>---<>---<>---<>---<>    
    {D}""")   
    user = str(input('Enter the website link: '))
    domains = user +"/robots.txt"

    try:
        page = requests.get(domains,"html.parser").text
        hidden = re.findall("Disallow\: \S{1,}",page)

        for i in hidden:
            link = "[*]" + user + i[10:]
            print(link)
            fil = open("blacklink.txt", "a")
            fil.write("\n"+link)
            fil.close()
    except:
        pass
elif option == '13':
    os.system('clear')
    print(f'{red}SOON')
elif option == '14':
    os.system('clear')
    adsilo = input(f'{blue}[{red}?{blue}] {red}Enter IP/Domain {cyan}: ')
    os.system('cd Extensions && python breacher.py -u '+adsilo)
elif option == '15':
    taremail = input(f'{blue}[{red}?{blue}] {red}Enter IP/Domain {cyan}: ')
    os.system('cd Extensions && python3 infoga.py --domain '+taremail)
else:
    os.system('clear')
    print(f'[!] Select Number')
    exit()
