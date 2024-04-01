class Funcionario:#criando uma classe
    def _init_(self, nome, cpf, numero, email):#chamando o método construtor da classe
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.email = email


class Comida:#criando outra classe
    def _init_(self, nome, tipo_comida, data_validade, estoque):#essa tambem necessita de um método construtor
        self.nome = nome
        self.tipo_comida = tipo_comida
        self.data_validade = data_validade
        ##criação de um novo atributo para mostrar quanto de um alimento ainda há em estoque
        self.estoque = estoque


##aqui criei uma função que cria/instancia novos objetos da classe comida, basicamente cria um alimento qualquer para ser registrado depois
def registrar():
    nome = input("Digite o nome do alimento a ser adicionado: ").lower()
    tipo_comida = input("Digite o tipo do alimento a ser adicionado: ").lower()
    data_validade = input("Digite a data de validade do alimento a ser adicionado: ").lower()
    estoque = input("Digite a quantidade do alimento a ser adicionado: ").lower()
    print("\nalimento registrado com sucesso!!")
    return Comida(nome, tipo_comida, data_validade, estoque)
##lower padroniza tudo para  letra minúcula. Não podemos controlar oque o usuario digita,mas sima forma em que o sitema lida com isso
##Lower é apenas um método para que 'S' vire um 's',assim o código roda de forma mais simples e sem erros.

##removi a classe estoque pois era desnecessaria, as listas sozinhas já eram o suficiente, mas se futuramente for precisar vcs adicionam a classe de novo
alimentos = []

# criação de uma nova lista para armazenar pessoas registradas
pessoas = []


##mudei estes métodos transformando eles em funções para se adequarem as novas mudanças
def adicionar_item():
    while True:
        alimento = input("qual alimento deseja adicionar ao estoque: ").lower()
        for i in alimentos:
            if alimento != i.nome:
                print("O produto procurado não esta registrado no sistema")
            else:
                quantidade = input("quanto deste alimento deseja adicionar ao estoque: ")
                i.estoque += quantidade
                break
        return alimentos


##aqui eu pergunto qual produto a pessoa quer pegar do estoque, portanto é importante lembrar que antes de usar essa função é nescessario ja ter registrado um alimento na lista usando a função 'registrar'
def remover_item():
    while True:
        alimento = input("qual item deseja pegar do estoque: ").lower()
        for i in alimentos:
            if alimento != i.nome:
                print("O produto procurado não esta registrado no sistema")
            else:
                quantidade = input("quanto deste alimento deseja pegar do estoque: ")
                if i.estoque < quantidade:
                    print(f"no estoque há apenas {i.estoque} unidades deste produto, pegue somente o que há disponível")
                else:
                    i.estoque -= quantidade
                    print(f"voce retirou {quantidade} unidades de {i.nome} do estoque\n{i.nome} restante: {i.estoque}")
                    break
                return alimentos
#Aqui estamos usando uma f-string para formatar a string.
#subtituindo as palavras 'quantidade','unidade','estoque','restante' por {quantidade},{unidade},{estoque},{restante}
#{i.nome} declara que ex:{quantidade} é de alimento,leia o código e fará sentido.
#isso é útil para que a mensagem final seja personalizada de acordo com o item que está sendo manipulado na string
#Isso cria strings légiveis e dinâmicas e contextualizadas.
def verificar_estoque():
    while True:
        alimento = input("qual item deseja visualizar: ").lower()
        for i in alimentos:
            if alimento != i.nome:
                print("O produto procurado não esta registrado no sistema")
            else:
                print(f"Produto: {i.nome}\nEstoque: {i.estoque}")
                break


class Aluno:
    def _init_(self, nome, cpf, numero, email):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.email = email
        self.presente = False  # Inicialmente aluno não está presente

    def marcar_presenca(self):
        presenca = input("o aluno esta presente (S/N): ").upper()
        if presenca == 'S':
            self.presente = True
            print(f"{self.nome} foi marcado como presente.")
        else:
            self.presente = False
            print(f"{self.nome} foi marcado como ausente.")
        return self.presente
#upper e lower tem a mesma função,esses métodos padronizam os caracteres digitados
#lower padroniza tudo em minusculo
#upper padroniza tudo em maiusculo
#sabemos que para a máquina/sistema 's' e 'S' são coisas diferentes então isso é útil

##função que registra o aluno na lista pessoas:
def registrar_aluno():
    nome_aluno = input("Qual o nome do aluno: ")
    cpf = input("Qual o cpf do aluno: ")
    numero = input("Qual o numero do aluno: ")
    email = input("Qual o email do aluno: ")
    return Aluno(nome_aluno, cpf, numero, email)


##aqui colocamos o codigo para funcionar utilizando as funções e metodos criados anteriormente
while True:
    #criando um menu para saber se o usuario quer mexer nas funções relacionadas a comidas ou alunos, depois dividimos em um menu para cada
    opsoes = input("Para visualizar a lista de comandos relacionados aos alimento em estoque digite 1.\nPara "
                   "visualizar a"
                   "lista de comandos relacionados aos alunos digite 2.\nCaso queira encerrar sessão digite 0")
    if opsoes == '1':
        while True:
            opsoes2 = input("Para registrar um novo alimento no estoque, digite 1\nPara adicionar mais unidades de "
                            "algum elemento ja registrado, digite2\nPara visualizar produtos em estoque, "
                            "digite 3\nPara encerrar sessão,digite 0")
            if opsoes2 == '1':
                comida = registrar()
                alimentos.append(comida)#append adiciona outro item ao fim da lista,isso é útil para não termos que editar a lista diretamente
            elif opsoes2 == '2':
                adicionar_item()
            elif opsoes2 == '3':
                verificar_estoque()
            elif opsoes2 not in ['1', '2', '3', '0']:
                print("não há funções para isto, por favor navegue utilizando o menu")
            else:
                break
    elif opsoes == '2':
        while True:
            opsoes3 = input("Para registrar um aluno, digite 1\nPara marcar presença em um aluno registrado, "
                            "digite 2\nPara encerrar sessão, digite 0")
            if opsoes3 == '1':
                aluno = registrar_aluno()
                pessoas.append(aluno)
            elif opsoes3 == '2':
                while True:
                    for i in pessoas:
                        nome = input("qual o nome do aluno: ")
                        if nome != i.nome:
                            print("este nome não esta na registrado no sistema, por favor digite outro")
                        else:
                            i.marcar_presenca()
            elif opsoes3 not in ['1', '2', '0']:
                print("não há opções para isto, por favor navegue utilizando o menu")
            else:
                break
    elif opsoes not in ['1', '2', '0']:
        print("não há opções para isto, por favor navegue utilizando o menu")
    else:
        break