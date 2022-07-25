import sys

# Retorna o último elemento de uma string

def verify(lang):
    my_list = [1,2,3,4]

    if lang in my_list:
        if(lang == 1):
            dic = {
            'first': 'Write a word and we will find your last term:', 
            'two':  'Thank you for joining our game', 
            'tree': 'If you want to close the program, write q:'
            }
        if(lang == 2):
             dic = {
            'first': 'Escribe una palabra y encontraremos tu último término: ', 
            'two':  'Gracias por unirte a nuestro juego.', 
            'tree': 'Si desea cerrar el programa, escriba q:'
            }
        if(lang == 3):
            
          dic = {
            'first': 'Digite uma palavra e econtraremos o seu último termo:', 
            'two':  'Obrigado por participar do nosso jogo.', 
            'tree': 'Caso deseje encerrar o programa digite q:'
            }
        arr = [True, dic]
        return arr
    return False

def getLastString(lang):
    if(lang == 4):
            print("Thank you for joining our game.")
            sys.exit(0)
    vr = verify(lang)

    if(vr[0]):
        langGame(vr[1])
    else:
        print("This option does not exist, we are closing your connection")
        sys.exit(0)

def langGame(lang):
    
    while True:
        n = str(input(lang['first']))
        if(n == 'q:'):
            print(lang['two'])
            sys.exit(0)

        # pega ultima posição da string
        print(n[-1:])
        print(lang['tree'])


def start():
    try:
        lang =int(input('''
            Choose your language
                1 - English
                2 - Spanish
                3 - Portuguese
                4 - Exit
                :  '''))
                
        getLastString(lang)
    except:
        print("This value is not valid, please try again.")
    

start()
