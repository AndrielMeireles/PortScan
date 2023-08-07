#Importação da biblioteca
import socket

#portas que serão verificadas pelo Script
ports = [21,22,25,80,433,445,3306]

for port in ports:
         client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         client.settimeout(0.1)   
         code = client.connect_ex(("nomedodominio", port)) #Em "nomedodominio" seria inserido o dominio que será verificado
         if code == 0:
                 print (port, "OPEN")
