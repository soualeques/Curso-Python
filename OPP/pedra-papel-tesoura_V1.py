class Participante:
  def __init__(self, nome):
    self.nome = nome
    self.pontos = 0
    self.escolha = ""
  def escolhas(self):
    self.escolha = input("{nome}, ESCOLHA: pedra, papel, tesoura, spock, lagarto. ".format(nome= self.nome))
    print("{nome} ESCOLHEU: {escolha}".format(nome=self.nome, escolha = self.escolha))
  def escolhaNumeral(self):
    opcoes = {
        "pedra": 0,
        "papel": 1,
        "tesoura": 2,
        "lagarto": 3,
        "spock": 4
    }
    return opcoes[self.escolha]
  def incrementoPonto(self):
    self.pontos += 1 

class GameRound:
  def __init__(self, p1, p2):
    self.regras = [
   [0, -1, 1, 1, -1],
   [1, 0, -1, -1, 1],
   [-1, 1, 0, 1, -1],
   [-1, 1, -1, 0, 1],
   [1, -1, 1, -1, 0]
]
    p1.escolhas()
    p2.escolhas()
    resultado = self.compararEscolha(p1,p2)
    print("Resultado deu em {resultado}".format(resultado = self.resultado(resultado) ))
    if resultado > 0:
      p1.incrementoPonto()
    elif resultado < 0:
      p2.incrementoPonto()
    else:
      print("Nenhum ponto para ninguem!")
    
  def compararEscolha(self, p1, p2):
    return self.regras[p1.escolhaNumeral()][p2.escolhaNumeral()]
  def ganharPonto(self):
    print("implement")
  def resultado(self, resultado):
    res = {
      0: "EMPATE",
      1: "GANHOU",
      -1: "PERDEU"
    }
    return res[resultado]

class Game:
  def __init__(self):
    self.endGame = False
    self.participante = Participante("Alex")
    self.secondParticipante = Participante("Sheldon")
  def start(self):
    while not self.endGame:
      GameRound(self.participante, self.secondParticipante)
      self.checarsequersair()
      
  def checarsequersair(self):
     answer = input("CONTINUAR O JOGO? [Y/N]: ")
     if answer == 'Y':
        GameRound(self.participante, self.secondParticipante)
        self.checarsequersair()
     else:
       print("fim do jogo, {p1name} teve {p1points}, e {p2name} teve {p2points}".format(p1name = self.participante.nome, p1points= self.participante.pontos, p2name=self.secondParticipante.nome, p2points=self.secondParticipante.pontos))
       self.determinarganhador()
       self.endGame = True
  def determinarganhador(self):
    resultado = "É um empate"
    if self.participante.pontos > self.secondParticipante.pontos:
      resultado = "Ganhador é {nome}".format(nome=self.participante.nome)
    elif self.participante.pontos < self.secondParticipante.pontos:
       resultado = "Ganhador é {nome}".format(nome=self.secondParticipante.nome)
    
    print(resultado)  

game = Game()
game.start()