class Funcionario:
    def __init__(self, nome,cpf,numero,email):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.email = email

    def cadastrar_item(self, estoque, comida, quantidade,tipo_comida,validade):
        estoque.adicionar_item(comida, quantidade,tipo_comida,validade)

    nome = input("Qual seu nome?")
    cpf = input("Informe seu CPF?")
    numero = input("Informe seu número")
    email = input("Informe seu email")
    print ("Obrigado(a) pelas informações")

class Comida:
    def __init__(self, nome, tipo_comida,data_validade):
        self.nome = nome
        self.tipo_com = tipo_comida
        self.dat_valid = data_validade

    nome = input("Qual nome do alimento?")
    TipoComida = input("Informe qual tipo de comida,se é industrializada ou perecível")
    DataValidade = input("Se é industrializada qual a data de validade?")

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
    def verificar_validade(self):
        print("Validade:")

class Aluno:
    def __init__(self, nome, cpf, numero, email):
        self.nome = nome
        self.cpf = cpf
        self.num = numero
        self.email = email
        self.presente = False  #Inicialmente aluno não está presente

    nome = input("Qual seu nome?")
    cpf = input("Informe seu CPF?")
    numero = input("Informe seu número")
    email = input("Informe seu email")
    print("Obrigado(a) pelas informações")


    def marcar_presenca(self, presenca):
        if presenca:
            self.presente = True
            print(f"{self.nome} está presente.")
        else:
            self.presente = False
            print(f"{self.nome} não está presente.")

    def verificar_presenca(self):
        if self.presente:
            print(f"{self.nome} está presente.")
        else:
            print(f"{self.nome} não está presente.")