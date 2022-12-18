from ast import main

def minion_game(palabras):
    sub_palabras = {}
    for i in range(len(palabras)):
       if palabras[i] in 'AEIOU': 
            for j in range(i+1, len(palabras)+1):
                sub_palabras[palabras[i:j]] = sub_palabras.get(palabras[i:j], 0) + 1
       else:
            for j in range(i+1, len(palabras)+1):
                sub_palabras[palabras[i:j]] = sub_palabras.get(palabras[i:j], 0) + 1
    if sub_palabras.keys() in 'AEIOU':
        print('Kevin', sub_palabras.items())
    else:
        print('Stuart', sub_palabras.items())
minion_game(input())
if __name__ == '__main__':
    main()