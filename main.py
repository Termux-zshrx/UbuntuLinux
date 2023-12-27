import os

os.system("clear")

def main():
    print ("")
    print ('''\033[1;35m
█░█ █▄▄ █░█ █▄░█ ▀█▀ █░█
█▄█ █▄█ █▄█ █░▀█ ░█░ █▄█
    ''')
    print ("\033[1;31m[1]\033[1;32mUbuntu start")
    print ("\033[1;31m[2]\033[1;32mUpdate")
    print ("\033[1;31m[3]\033[1;32mExit")
    print ("")
    x=int(input("\033[1;31m[●]\033[1;33mEnter Your Choice \033[1;31m》》\033[1;37m:"))
    if x==1:
       os.system("clear")
       os.system("proot-distro list")
       os.system("proot-distro install ubuntu ")
       os.system("proot-distro  login ubuntu")
       main()
    elif x==2:
         os.system("clear")
         os.system("apt update && apt upgrade -y")
         os.system("apt install proot-distro -y")
         os.system("clear")
         main()
    elif x==3:
         os.system("clear")
    else:
         print ("not .../")
main()
