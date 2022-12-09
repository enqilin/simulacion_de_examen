from ast import main

def minion_game(palabras):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    for i in range(len(palabras)):
        if palabras[i] in vowels:
            kevin_score += (len(palabras)-i)
        else:
            stuart_score += (len(palabras)-i)
            if kevin_score < stuart_score:
                print('Stuart', stuart_score)
            elif kevin_score > stuart_score:
                print ('Kevin', kevin_score)
            else:
                print('Draw')




if __name__ == "__main__":
    minion_game()