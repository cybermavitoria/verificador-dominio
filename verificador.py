import socket
import datetime
CDNS_CONHECIDAS = {
    "Cloudflare": ["103.21.", "103.22.", "103.31.", "104.16.", "104.17.", "108.162.", "141.101.", "162.158.", "162.159.", "172.64.", "172.65.", "172.66.", "172.67."],
    "AWS": ["13.", "52.", "54."],
    "Google": ["142.250.", "172.217.", "216.58."],}
def identificar_cdn(ip):
    for cdn, faixas in CDNS_CONHECIDAS.items():
        for faixa in faixas:
            if ip.startswith(faixa):
                return cdn
    return None
def verificar_dominio(dominio):
    resultado = []
    resultado.append(f"Dominio: {dominio}")
    resultado.append(f"Data: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    try:
        ip = socket.gethostbyname(dominio)
        resultado.append(f"[OK] IP encontrado: {ip}")
        cdn = identificar_cdn(ip)
        if cdn:
            resultado.append(f"[INFO] IP pertence a CDN: {cdn}")
        else:
            resultado.append("[INFO] CDN nao identificada")
    except socket.gaierror:
        resultado.append("[ERRO] Dominio nao encontrado")
    return resultado
dominio = input("Digite um dominio (ex: google.com): ")
resultado = verificar_dominio(dominio)
for linha in resultado:
    print(linha)
