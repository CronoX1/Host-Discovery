import platform, os, sys, subprocess

if len(sys.argv) != 2 or sys.argv[1] == 'h' or sys.argv[1] == 'help':
    print('Usage: python3 Host-Discovery.py "your IP address"')
    exit()

nocolor = "\033[0;37;10m"
azul = "\033[0;34;10m"
amarillo = "\033[1;33;10m"

IP = sys.argv[1]

fIP = IP.split('.')
fIP.pop()
mIP = ''
listaIPs = []
df = open('HDtargets.txt', 'w')

for i in fIP:
    mIP += i + '.'

for i in range(1, 255):
    pIP = mIP + str(i)
    listaIPs.append(pIP)

print(azul + '''
Host Discovery made by CronoX

''' + amarillo + '''https://github.com/CronoX1''' + azul + '''

Active machines will be saved at ''' + amarillo + '''HDtargets.txt ''' + azul + '''in the actual directory.
''' + amarillo + '''----------------------------------------------------------------------- 
''' + nocolor)

def plataforma(listaIPs):
    if platform.system() == 'Windows':
        ping = 'ping -n 1 '
        ping2 = ping + '-i 1 '
        Windows(ping, ping2, listaIPs)
    elif platform.system() == 'Linux':
        ping = 'timeout 0.2 ping -c 1 '
        Linux(ping, listaIPs)

def Windows(ping, ping2, listaIPs):
    for i in listaIPs:
        if i == IP:
            continue
        else:
            accion = ping + str(i)
            output = os.popen(accion)
            for line in output:
                if 'Received = 1' in str(line):
                    accion2 = ping2 + i
                    output2 = os.popen(accion2)
                    df.write(str(i) + '\n')
                    for line in output2:
                        if 'TTL=128' in line:
                            print(azul + i, ' ---> Windows' + nocolor)
                        elif 'TTL=64' in line:
                            print(amarillo + i, ' ---> Linux' + nocolor)

def Linux(ping, listaIPs):
    for i in listaIPs:
        if i == IP:
            continue
        else:
            accion = ping + str(i)
            output = os.popen(accion)
            for line in output:
                if 'ttl=64' in line:
                    print(amarillo + i, ' ---> Linux' + nocolor)
                    df.write(str(i) + '\n')
                elif 'ttl=128' in line:
                    print(azul + i, ' ---> Windows' + nocolor)
                    df.write(str(i) + '\n')

plataforma(listaIPs)