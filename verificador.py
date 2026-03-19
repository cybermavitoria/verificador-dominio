import socket
import datetime

def verificar_dominio(dominio):
    resultado = []
    resultado.append(f"Dominio: {dominio}")
    resultado.append(f"Data: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    try:
        ip = socket.gethostbyname(dominio)
        resultado.append(f"[OK] IP encontrado: {ip}")
    except socket.gaierror:
        resultado.append("[ERRO] Dominio nao encontrado")
    return resultado

dominio = input("Digite um dominio (ex: google.com): ")
resultado = verificar_dominio(dominio)

for linha in resultado:
    print(linha)