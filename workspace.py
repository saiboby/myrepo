import os
import sys
import subprocess

try :

        D=dict()
        aca = {"hostname": "aca","ip_address": "192.168.50.11","password": "vagrant", "username": "root", "port": "22"}
        mag = {"hostname": "mag","ip_address": "192.168.50.11","password": "vagrant", "username": "vagrant","port":"22"}
        D['mag']=mag
        D['aca']=aca



        #pw1 = aca.get("password")
        # print(pw1)
        # print(aca["hostname"])

        args1 = ['sshpass','-p', aca["password"],'ssh', '-o', 'StrictHostKeyChecking=no','-p',aca["port"] ,aca["username"] +'@'+ aca["ip_address"]+ ' ' ,'rm -rf /oopepepe']
        args2 = ['sshpass','-p', mag["password"],'ssh', '-o', 'StrictHostKeyChecking=no', mag["username"] +'@'+ mag["ip_address"]+ ' ' ,'sudo mkdir -p /opt/Sai123']

        def cleanup(param):
                param=sys.argv[1]
                if param == "aca":
                        print("executing on aca")
                        #os.system('sshpass -p "x" ssh -o StrictHostKeyChecking=no root@192.168.50.11 "mkdir -p /opt/aca231"')
                        #subprocess.call(args1)
                        output = subprocess.call(args1)
                        if output == 0:
                                print("Workspsace clean_up has been done on ACA host")
                        else:
                                print("Didnt connect to the host")
                                subprocess.call(['exit','1'])
                elif param == "mag":
                        #os.system('sshpass -p "$x" ssh -o StrictHostKeyChecking=no root@192.168.50.11 "mkdir -p /opt/mag231"')
                        subprocess.call(args2)
                        print("Workspace clean_up has been done on Magellan host")
                else:
                        print("Mention the exact argument as {}".format(D.keys()))
                        #subprocess.call(['exit','1'])

        cleanup(sys.argv[1])
except IndexError:
        print("Getting Index rrox, Please enter the argument as {}".format(D.keys()))
        subprocess.call(['exit','1'])
        #subprocess.call(['sshpass','-p', aca["password"],'ssh', '-o', 'StrictHostKeyChecking=no','-p',aca["port"] ,aca["username"] +'@'+ aca["ip_address"]+ ' ' ,'rm -rf /opt/B*'])
