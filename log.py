#tools by Giffahri
#Jangan edit selain username+password
#recode gk bikin lo jadi mastah


from getpass import getpass
import os
import time

def menu():
      while True:
           print("")
           os.system("clear")
           os.system("figlet -f slant '   Wellcome' | lolcat")
           print('\033[1;96m')
           print('   +--------------------------------------------------+  ')
           print('    Creator        : Gifahri                                 ')
           print('   +--------------------------------------------------+  ')
           print('    Gmail          : gifahri77777@gmail.com  ')
           print('   +--------------------------------------------------+  ')
           print('    instagram      :  @Tecno_Cyber            ')
           print('   +--------------------------------------------------+  ')
           print('    WhatsApp       : 081315973943             ')
           print('   +--------------------------------------------------+  ')
           print('    Team           : Saya Sendiri                       ')
           print('   +--------------------------------------------------+  ')
           print(' ')
           print(' ')
           print("")
           try:
                x = str(input('\033[1;92m [?] Username \033[1;93m: '))
                print("")
                e = getpass('\033[1;92m [?] Password \033[1;93m: ')
                print ("")
#silahkan ganti username+passwordnya gan
                if x=="AnonyCyyber" and e=="Rahasia":
#jangan edit yg lain kalo gak mau eror
                   print('Login Sukses Mohon Tunggu Sebentar...')
                   time.sleep(1)
                   os.system('clear')
                   print('')
                   os.system('figlet ' + x + ' | lolcat')
                   print('\033[1;92m ────────────────────────────────By Gifahri = AnonyCyyber')
                   print("")
                   break
                else:
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     [!] Username/Password Salah")
                      time.sleep(2)
                      print("")
           except Exception:
                      
                      print("")
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     [!] Username/Password Salah")
                      time.sleep(2)
           except KeyboardInterrupt:
                      print("")
                      os.system('killall -9 com.termux')
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     [!] Username/Password Salah")
                      time.sleep(2)
menu()
