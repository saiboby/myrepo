import os
import sys
import argparse
import subprocess

def cleanup(ipaddress,username,password,port,workspace):
    
    args1 = ['sshpass','-p',password ,'ssh', '-o', 'StrictHostKeyChecking=no','-p',port ,username +'@'+ ipaddress+ ' ' ,'sudo rm -rf', workspace ]

    r_status=subprocess.Popen(args1)
    r_status.communicate()
    print("The return code is {}".format(r_status.returncode))
    
    if r_status.returncode == 0:
        print("Workspsace clean_up has been done on the given host")

    elif r_status.returncode == 1:
        print("The command has already satisfied")

    else:
        print("Didn't connect to server ,please ensure the connectivity and command line arguments, status code is {}".format(r_status.returncode))

def ar_parser():


    parser = argparse.ArgumentParser(description="ip,uname,password, port")

    parser.add_argument("-ip","--ipaddress",
                        dest = "ipaddress",
                        action='store',
                        help="mention the hostnem")

    parser.add_argument("-uname", "--username",
                        dest = "username",
                        action='store',
                        help="mention the username")

    parser.add_argument("-pword","--password",
                        dest = "password",
                        action='store',
                        help="Mention the pasword")

    parser.add_argument("-port","--port",
                        dest = "port",   
                        action='store',
                        help="Mention the port")

    parser.add_argument("-wspace","--workspace",
 			dest = "workspace",
                        action='store',
                        help="Mention the workspace")

    args = parser.parse_args()


    return args


if __name__ == "__main__":

    args = ar_parser()
    #print(args)
    if args.ipaddress is None or args.workspace is None or args.username is None or args.password is None:
      print("usage:python workspace_cleanup.py ,-ipaddress valid_ipaddress,-username valid_username,-password valid_password,-workspace valid_workspace")
    print("the port is {}".format(args.port))
    if args.port:
      port = args.port
    else:
      port = "22"
    print("the print after if is {}".format(port))
    
 
    try:
      cleanup(ipaddress=args.ipaddress,username=args.username,password=args.password,port=port,workspace=args.workspace)
    except Exception as e:
      print("ERROR {} ".format(e))
      print("Check the usage: 'python workspac_cleanup.py -h' and couldn't run cleanup function")
    
    
    
    

