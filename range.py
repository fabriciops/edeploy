from time import sleep
import numpy as np
import sys

# Considerando a a sequência numérica a seguir (11, 18, 25, 32, 39... )faça uma função que recebe como entrada uma posição e devolve qual o valor do número naquela posição, considerando a sequência numérica apresentada. 
# Ex:
# print_valor(x=1) retornará 11; print_valor(x=6) retornará 46; print_valor(x=254) retornará 1.782;
# print_valor(x=3.542.158) retornará 24.795.110;

def verify(lang):
    my_list = [1,2,3,4]

    if lang in my_list:
        if(lang == 1):
            dic = {
            'first': 'Input an indeces value that we will fetch in the array: ',
            'question': '''
            Use this list [11, 20, 30, 35, 40, 55, 10] : [Yes] 1 
            Or You want That the Software make a aleatory list? [2] 
            You can create your ower Array list EX: 1 2 3 4 5 6 7 8, : 
            If you want to close the program, write q: ''',

            'question_ind': 'What index would you like to fetch from the list: ',
            'two':  'Thank you for joining our game', 
            'tree': 'If you want to close the program, write q:'
            }
        if(lang == 2):
             dic = {
            'first': 'Ingrese un valor de índices que buscaremos en la matriz: ', 
            'question': '''Utilice esta lista [11, 20, 30, 35, 40, 55, 10]: [Sí] 1
            ¿O quieres que el Software haga una lista aleatoria? [2]
            Puede crear su propia lista de matrices EX: 1 2 3 4 5 6 7 8, :
            Si desea cerrar el programa, escriba q: ''',
            'question_ind': '¿Qué índice le gustaría obtener de la lista: ',

            'two':  'Gracias por unirte a nuestro juego.', 
            'tree': 'Si desea cerrar el programa, escriba q:'
            }
        if(lang == 3):
            
          dic = {
            'first': 'Insira um valor de indeces que buscaremos no array:',
            'question' : '''
            Use esta lista [11, 20, 30, 35, 40, 55, 10] : [Sim] 1
            Ou você quer que o Software faça uma lista aleatória? [2]
            Você pode criar sua lista de matrizes EX: 1 2 3 4 5 6 7 8, :
            Se você quiser fechar o programa, escreva q:
            ''',
            'question_ind': 'Qual índice você gostaria de buscar na lista: ',
            'two':  'Obrigado por participar do nosso jogo.', 
            'tree': 'Caso deseje encerrar o programa digite q:'
            }
        arr = [True, dic]
        return arr
    return False

def getValue(lang):
    if(lang == 4):
            print("Thank you for joining our game.")
            sys.exit(0)
    vr = verify(lang)

    if(vr[0]):
        langGame(vr[1])
    else:
        print("This option does not exist, we are closing your connection")
        sys.exit(0)

def Convert(string):
    li = list(string.split(" "))
    return li


def langGame(lang):
    
    while True:
        n = input(lang['question'])

        if(n == 'q:'):
            print(lang['two'])
            sys.exit(0)

        if(n == '1'):
            ind = int(input(lang['question_ind']))
            print(ind)
            arr = [11, 20, 30, 35, 40, 55, 10]
            print(arr[ind])
        elif (n == '2'):
            ind = int(input(lang['question_ind']))
            arr = np.random.randint(10, size=(20))
            print(arr[ind])
        else:
            
            ind = int(input(lang['question_ind']))
            arr = Convert(n)
            print()
            print(type(arr))
            sleep(2)
            print(arr[ind])


def start():
    try:
        lang =int(input('''
            Choose your language
                1 - English
                2 - Spanish
                3 - Portuguese
                4 - Exit
                :  '''))
        getValue(lang)
    except:
        print("This value is not valid, please try again.")
    

start()
