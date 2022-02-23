import pyttsx3
'''falar = pyttsx3.init("sapi5")
frase = " "
while frase not in "Sair":
    frase = str(input("fale comigo: "))
    falar.say(frase)
    falar.runAndWait()'''
ca = (
    '\033[m',        # 0 Default
    '\033[0;30;41m', # 1 Vermelho  
    '\033[0;30;42m', # 2 Verde
    '\033[0;30;43m', # 3 Amarelo
    '\033[0;30;44m', # 4 Azul
    '\033[0;30;45m', # 5 Roxo
    '\033[7;30m'     # 6 Branco
)
cl = (
    '\033[m',       # 0 Default
    '\033[0;31m', # 1 Vermelho  
    '\033[0;32m', # 2 Verde
    '\033[0;33m', # 3 Amarelo
    '\033[0;34m', # 4 Azul
    '\033[0;35m', # 5 Roxo
)

print(f'{cl[1]} oi {cl[0]}')