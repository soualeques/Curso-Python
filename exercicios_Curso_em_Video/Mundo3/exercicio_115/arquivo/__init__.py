

def arquivoExiste(nome):
    try:
        arquivo = open(nome, "rt")
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        arquivo = open(nome, "wt+")
        arquivo.close()
    except:
        print('Problema ao criar arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
        
        
def lerArquivo(nome):
    try:
        arquivo = open(nome, "rt")
    except:
        print('Erro ao ler arquivo')
    else:
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]} anos')
        

def cadastrarArquivo(arq, nome = 'Desconhecido', idade = 0):
    try:
        a = open(arq, "at")
    except:
        print('ouve um erro ao acessar o arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao cadastrar no arquivo')
    finally:
        a.close()
        