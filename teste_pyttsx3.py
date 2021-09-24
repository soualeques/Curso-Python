import pyttsx3
falar = pyttsx3.init("sapi5")
frase = " "
while frase not in "Sair":
    frase = str(input("fale comigo: "))
    falar.say(frase)
    falar.runAndWait()
