class Funcionario:
    def __init__(self, nome, cpf, numero, email):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.email = email

class Comida:
    def __init__(self, nome, tipo_comida, data_validade):
        self.nome = nome
        self.tipo_comida = tipo_comida
        self.data_validade = data_validade

class Estoque:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, comida, quantidade):
        if comida.nome in self.itens:
            self.itens[comida.nome] += quantidade
        else:
            self.itens[comida.nome] = quantidade

    def remover_item(self, comida, quantidade):
        if comida.nome in self.itens:
            if self.itens[comida.nome] >= quantidade:
                self.itens[comida.nome] -= quantidade
            else:
                print("Quantidade insuficiente em estoque.")
        else:
            print("Item não encontrado.")

    def verificar_estoque(self):
        print("Estoque atual:")
        for comida, quantidade in self.itens.items():
            print(f"{comida}: {quantidade}")

class Aluno:
    def __init__(self, nome, matricula, numero, email):
        self.nome = nome
        self.matricula = matricula
        self.numero = numero
        self.email = email
        self.presente = False  # Inicialmente aluno não está presente

    def marcar_presenca(self, presenca):
        if presenca:
            self.presente = True
            print(f"{self.nome} está presente.")
        else:
            self.presente = False
            print(f"{self.nome} não está presente.")

# Entrada de dados
nome_funcionario = input("Qual seu nome? ")
cpf_funcionario = input("Informe seu CPF? ")
numero_funcionario = input("Informe seu número: ")
email_funcionario = input("Informe seu email: ")

nome_comida = input("Qual nome do alimento? ")
tipo_comida = input("Informe qual tipo de comida, se é industrializada ou perecível: ")
data_validade = input("Se é industrializada, qual a data de validade? ")

nome_aluno = input("Qual seu nome? ")
cpf_aluno = input("Informe seu CPF? ")
numero_aluno = input("Informe seu número: ")
email_aluno = input("Informe seu email: ")