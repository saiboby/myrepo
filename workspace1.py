import os
import sys
import argparse
import subprocess

#def cleanup(*args):
def cleanup():
  print ("The cleanup ip and password {} and {}".format(ipaddress,password))
  args1 = ['sshpass','-p',password ,'ssh', '-o', 'StrictHostKeyChecking=no','-p',port ,username +'@'+ ipaddress+ ' ' ,wspace]

  #if ipaddress:
  try:
    r_status=subprocess.Popen(args1)
    r_status.communicate()
    print("The return code is {}".format(r_status.returncode))
    if r_status.returncode == 0:
      print("Workspsace clean_up has been done on ACA host")
    else:
      print("Didn't connect to server and please ensure the connectivity, status code is {}".format(r_status.returncode))
      #subprocess.call(['exit','1'])
  except:
         print("command is wrong")
         #subprocess.call(['exit','1'])


def ar_parser():


  parser = argparse.ArgumentParser(description="ip,uname,password, port")

  parser.add_argument("-ip","--ipaddress",
                      required=True,
                      action='store',
                      help="mention the hostnem")

  parser.add_argument("-uname", "--username",
                      required=True,
                      action='store',
                      help="mention the username")

  parser.add_argument("-pword","--password",
                      required=True,
                      action='store',
                      help="Mention the pasword")

  parser.add_argument("-port","--port",
                      required=True,
                      action='store',
                      help="Mention the port")

  parser.add_argument("-wspace","--workspace",
                      required=True,
                      action='store',
                      help="Mention the workspace")

  args = parser.parse_args()

  print("The given hostname is {}, username is {}, password is {},port is {}, workspace is {}".format(args.ipaddress,args.username,args.password,args.port,args.workspace))

  return args.ipaddress,args.username,args.password,args.port,args.workspace


if __name__ == "__main__":
  #parser = argparse.ArgumentParser()
  ipaddress,username,password,port,wspace = ar_parser()
  #cleanup(ipaddress,username,password,port,wspace)
  cleanup()
