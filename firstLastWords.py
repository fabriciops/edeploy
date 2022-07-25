# Escreva uma função que determina se uma string termina com 'A' e começa com 'B'

def fisrtAndLastWord():
    string = str(input("Let's see if your string starts with A and ends with B. Type it here: ")).upper()
    first = str(string).split()[0]

    if(first[0] == 'A' and string[-1::] == 'B'):
        print("True your string starts with A and ends with B")
        print(string)
    else:
        print("The string passed does not start with A and end with B. Its starting element is:", first[0], "and ends", string[-1::])

fisrtAndLastWord()
