'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>
'''

'''
Samantha Bennefield
12/20/17
Mr. Davis
Port Scanner
'''

import socket

file = open('port_status.txt', 'w') #Writes open ports to this file

common_ports = [80, 20, 22] #Ports it's scanning


x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def menu():
    print("[1] Ping IP's 172.17.2.100 to 172.17.2.254")
    selection = input("")
    if selection == "1":
        ping()
    else:
        menu()

def ping():
    finished = True
    last_digits = 100 #Last three digits of the IP
    progress = ""

    while finished == True:
        host = "172.17.2."+str(last_digits) #Let's the IP number tick up

        if last_digits == 255: #Cuts the scanner off at 255
            print("Scan finished!")
            finished = False

        print("Scanning ports 80, 20, and 22 on "+str(host))
        for port in common_ports: #Scan the ports on given IP
            try:
                s = x.connect((host, port))
                if s == 0:
                    file.write(host+" Port: "+port+" open")
                    x.close()
            except socket.error:
                pass
            
        last_digits +=1 #Increases IP number
        print("Scan complete")
        print("")
      

menu()
