import socket

while True:
    url = input('DIgite uma url: ')
    ip = socket.gethostbyname(url)
    print('O IP referente a URL informada é: ', ip)
    res = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if res == "N":
        break