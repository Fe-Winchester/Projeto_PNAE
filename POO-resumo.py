"""
POO- estilo de programação que enfatiza a modelagem computacional de objetos do mundo real para resolver um problema
"""
# classes-é uma representação do mundo real para objetos similares(mesmas características e comportamentos) - ex.:mamíferos
#objeto - um exemplo de determinada classe - exe: gato,cachorro,golfinho.
#atributos-características/ propriedades que definem obejetos similares(de uma mesma classe)
#métodos-ações que ajudam a definir uma classe com as quais os objetos interagem entre si.
#método construtor - método especial da classe usado para criar um objeto dessa classe(instanciar).

# modelando uma biblioteca computacional usando POO

# 1º passo:identificar as classes do universo do problema biblioteca
# usuário
# livro

# 2º passo: descrever/modelar as classes identificadas em Python
class Usuario:  # recomenda-se usar Letras maiúsculas no inicio do nome da classe.
    def __init__(self,nome,mat,cpf,uname,passwd,email,tel,dtn,livro=[]): # método construtor da classe - função
        # definir o molde do objeto que eu quero construir a partir da classe
        self.nome= nome # um atributo funciona como uma variável (espaço de memória que armazena um valor)
        self.matricula = mat
        self.cpf = cpf
        self.username = uname
        self.senha = passwd
        self.email = email
        self.fone = tel
        self.dt_nascimento = dtn
        self.livros_emprestados = livro
# o atributo recebe o que vem do parametros
# self/this é um atributo
# 3º passo: uma vez definida a classe,posso instanciar (criar/construir) um objeto (exemplo) dessa classe invocando seu método construtor
user1 = Usuario() # objeto instanciado da classe Usuario e chamado em user1
user2 = Usuario()
user3 = Usuario()
user4 = Usuario()
# Para acessar atributos de objetos em Python utilizou o seguinte padrão
# nome_do_objeto.nome_nome_do_atributo
user1.nome
print(user1.nome,user1.fone,user1.livros_emprestados)

def adicionar_item():   # Verifica se o alimento existe na lista de alimentos e permite adicionar uma quantidade específica ao estoque.
    while True:  # Inicia um loop infinito para continuar solicitando entradas até que o usuário decida parar.
        alimento = input("Qual alimento deseja adicionar ao estoque? R: ").lower()  # Solicita ao usuário o nome do alimento desejado e converte para minúsculas.
        encontrado = False  # Define uma flag para indicar se o alimento foi encontrado na lista de alimentos.
        for p in alimentos:  # Itera sobre cada item na lista de alimentos.
            if alimento == p.nome:  # Verifica se o nome do alimento digitado corresponde ao nome de um alimento na lista.
                quantidade = int(input(f"Quantidade de {p.nome} a ser adicionada ao estoque atual.(atual: {p.estoque}): "))  # Solicita ao usuário a quantidade do alimento a ser adicionada ao estoque.
                p.estoque += quantidade  # Adiciona a quantidade especificada ao estoque do alimento.
                print(f"Estoque atualizado para {p.nome}: {p.estoque}")  # Exibe uma mensagem indicando o estoque atualizado para o alimento.
                encontrado = True  # Define a flag como True para indicar que o alimento foi encontrado.
                break  # Sai do loop for, pois o alimento foi encontrado e o estoque atualizado.
        if not encontrado:  # Se o alimento não foi encontrado na lista.
            print("O produto procurado não está registrado no sistema!")  # Exibe uma mensagem informando que o produto não está registrado no sistema.
        continuar = input("Deseja adicionar mais algum item ao estoque? (S/N): ").upper()  # Pergunta ao usuário se deseja adicionar mais itens ao estoque e converte a resposta para maiúsculas.
        if continuar != 'S':  # Se a resposta do usuário não for 'S' (sim).
            break  # Sai do loop while, encerrando a função.

#https://github.com/practical-tutorials/project-based-learning

