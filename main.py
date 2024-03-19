import os
import time

print("""

 ___________   _____                                 
|_   _| ___ \ /  ___|                                
  | | | |_/ / \ `--.  ___ __ _ _ __  _ __   ___ _ __ 
  | | |  __/   `--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
 _| |_| |     /\__/ / (_| (_| | | | | | | |  __/ |   
 \___/\_|     \____/ \___\__,_|_| |_|_| |_|\___|_|


""")

print("**************************Welcome to IP scanner**************************************")
print("*************************************************************************************")

print("I give you the IP on the network you just have to copie the IP adress you want.")

time.sleep(1)

while True:
    os.system("arp -a")

    time.sleep(3)

    ip = input("Enter the IP adress you want to scan (nmap required) => ")
    os.system("nmap -A "+ip)
