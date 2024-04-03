# Protótipo de um sistema desenvolvido para o PNAE- Fase 1
#Implementar a classe funcioário
#Estudar onde cada função é executada
#Adicionar uma mensagem de aviso á linha 14
#Colocar comentários
#estudar herança
#implementar a classe pessoa/user
#Sistema de senha de acesso

class Comida:
    def _init_(self, nome, tipo_comida, data_validade, estoque):
        self.nome = nome
        self.tipo_comida = tipo_comida
        self.data_validade = data_validade
        self.estoque = int(estoque)


alimentos = []

pessoas = []


def registrar():
    nome = input("\nDigite o nome do alimento a ser adicionado: ").lower()
    tipo_comida = input("Digite o tipo do alimento a ser adicionado: ").lower()
    data_validade = input("Digite a data de validade do alimento a ser adicionado: ").lower()
    estoque = input("Digite a quantidade do alimento a ser adicionado: ").lower()
    print("\nalimento registrado com sucesso!!\n")
    return Comida(nome, tipo_comida, data_validade, estoque)


def procurar_item(lista):
    alimento = input("Qual nome deseja buscar: ").lower()
    for p in lista:
        if alimento == p.nome:
            return p
    return None
class Aluno:
    def _init_(self, nome, matricula, email):
        self.nome = nome
        self.matricula = matricula
        self.email = email
        self.presente = False  # Inicialmente aluno não está presente

    def marcar_presenca(self):
        presenca = input("\no aluno esta presente (S/N): ").upper()
        if presenca == 'S':
            self.presente = True
            print(f"\n{self.nome} foi marcado como presente.")
        else:
            print(f"\n{self.nome} foi marcado como ausente.")
        return self.presente


def registrar_aluno():
    nome_aluno = input("\nQual o nome do aluno: ")
    matricula = input("Qual a matrícula do aluno: ")
    email = input("Qual o email do aluno: ")
    print("\nAluno registrado com sucesso!!")
    return Aluno(nome_aluno, matricula, email)


while True:
    opcoes = input("\nPara visualizar a lista de comandos relacionados aos alimentos em estoque digite 1.\n"
                   "Para visualizar a lista de comandos relacionados aos alunos digite 2.\n"
                   "Caso queira encerrar sessão digite 0: ")
    if opcoes == '1':
        while True:
            opcoes2 = input("\nPara registrar um novo alimento no estoque, digite 1.\n"
                            "Para adicionar mais unidades de algum alimento já registrado, digite 2.\n"
                            "Para remover unidades de algum alimento já registrado, digite 3.\n"
                            "Para visualizar informações de produtos em estoque, digite 4.\n"
                            "Para voltar ao menu principal, digite 0: ")
            if opcoes2 == '1':
                comida = registrar()
                alimentos.append(comida)
            elif opcoes2 == '2':
                while True:
                    print("\ndigite o nome do item que deseja adicionar abaixo.")
                    comida = procurar_item(alimentos)
                    if comida == None:
                        print("\nEste alimento não esta registrado no estoque.")
                    else:
                        quantidade = int(input(f"\nQuanto de {comida.nome} deseja adicionar ao estoque"
                                               f"(estoque atual: {comida.estoque}): "))
                        comida.estoque += quantidade
                        print("\nUnidades adicionadas com sucesso!!")
                        break

            elif opcoes2 == '3':
                print("\nPara remover um item do estoque, digite o nome do item abaixo.")
                while True:
                    comida = procurar_item(alimentos)
                    if comida == None:
                        print("\nEste alimento não esta registrado no estoque.")
                    else:
                        while True:
                            quantidade = int(input(
                                f"\nQuanto de {comida.nome} deseja retirar do estoque(estoque atual: {comida.estoque}): "))
                            if comida.estoque >= quantidade:
                                comida.estoque -= quantidade
                                print("\nunidades retiradas com sucesso!!")
                                break
                            else:
                                print("\nestoque insuficiente, por favor pegue somente o que há no estoque.\n")
                        break
            elif opcoes2 == '4':
                print("\nDigite o nome do produto que deseja visualizar abaixo.")
                while True:
                    comida = procurar_item(alimentos)
                    if comida == None:
                        print("\nEste alimento não esta registrado no estoque.")
                    else:
                        print(f"\nNome: {comida.nome}\nTipo: {comida.tipo_comida}\n"
                              f"Data de validade: {comida.data_validade}\nUnidades em estoque: {comida.estoque}")
                        break
            elif opcoes2 == '0':
                break
            else:
                print("\nNão há funções para isto, por favor navegue utilizando o menu.")
    elif opcoes == '2':
        while True:
            opcoes3 = input("\nPara registrar um aluno, digite 1.\n"
                            "Para marcar presença em um aluno registrado, digite 2.\n"
                            "Para verificar as informações de um aluno, digite 3.\n"
                            "Para retornar ao menu principal, digite 0: ")
            if opcoes3 == '1':
                aluno = registrar_aluno()
                pessoas.append(aluno)
            elif opcoes3 == '2':
                print("\ndigite o nome do aluno que deseja marcar presença abaixo.")
                while True:
                    aluno = procurar_item(pessoas)
                    if aluno == None:
                        print("\nEste aluno não esta registrado no sistema.")
                    else:
                        aluno.marcar_presenca()
                        break
            elif opcoes3 == '3':
                print("\nDigite o nome do aluno que deseja visualizar as informações abaixo.")
                while True:
                    aluno = procurar_item(pessoas)
                    if aluno == None:
                        print("\nEste aluno não esta registrado no sistema.")
                    else:
                        print(f"\nNome: {aluno.nome}\nMatrícula: {aluno.matricula}\n"
                              f"E-mail: {aluno.email}\nPresença: {aluno.presente}")
                        break
            elif opcoes3 == '0':
                break
            else:
                print("\nNão há opções para isto, por favor navegue utilizando o menu.")
    elif opcoes == '0':
        break
    else:
        print("\nNão há opções para isto, por favor navegue utilizando o menu.")