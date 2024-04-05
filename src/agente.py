# Classe principal do agente reativo simples
class Agente:
    def __init__(self):
        self.regras = {}

    def adicionar_regra(self, condicao, acao):
        self.regras[condicao] = acao

    def sensoriamento(self, percepcao):
        if percepcao in self.regras:
            return self.regras[percepcao]
        elif percepcao.lower() == "sair":
            return "Sair"

# Classe principal para definir o ambiente de execução
class Ambiente:
    def __init__(self):
        self.agente = Agente()

    def executar_acao(self, percepcao):
        if percepcao.lower() == "sair":
            print("Programa encerrado.")
            exit()
        else:
            print("Ação escolhida pelo agente:", percepcao)

# Função criada para ler as percepções do arquivo .txt
def ler_percepcoes(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        percepcoes = arquivo.readlines()
    return percepcoes

# Função criada para obter ação do usuário ao escolher as opções disponíveis
def obter_acao(opcoes):
    while True:
        print("Opções disponíveis:")
        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i}. {opcao}")
        try:
            escolha = int(input("Escolha uma opção: ")) - 1
            if escolha < 0 or escolha >= len(opcoes):
                raise ValueError("Opção inválida!")
            return opcoes[escolha]
        except ValueError as e:
            print(e)

# Exemplo de uso:
if __name__ == "__main__":
    ambiente = Ambiente()

    # Lendo percepções do arquivo teste.txt
    percepcoes = ler_percepcoes("C:/Users/maria/OneDrive/Área de Trabalho/agentes reativos simples/src/teste.txt")
    
    # Exibindo percepções lidas do arquivo
    print("Percepções lidas do arquivo teste.txt:")
    for i, percepcao in enumerate(percepcoes, start=1):
        percepcao = percepcao.strip()  # Remove quebras de linha e espaços em branco
        print(f"{i}. {percepcao}")  # Mostra a percepção lida
    
    # Solicitando ação para cada percepção
    for percepcao in percepcoes:
        percepcao = percepcao.strip()  # Remove quebras de linha e espaços em branco
        acoes_possiveis = ["Ação 1", "Ação 2", "Ação 3", "Ação 4", "Sair"]  # Adicionando ação "Sair"
        acao = obter_acao(acoes_possiveis)
        ambiente.executar_acao(acao)