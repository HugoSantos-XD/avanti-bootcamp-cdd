"Implemente um módulo contendo uma função que verfique se um número é primo"

#criando minha função 
def num_primo(numero):
    #bool: True se o número for primo, False caso contrário.
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    else:
        for i in range(3, int(numero**0.5) + 1, 2):
            if numero % i == 0:

                return False
        return True
    

# Teste da função
if __name__ == "__main__":
    num = int(input('DIGITE UM NÚMERO:'))
    if num_primo(num):
        print(f"{num} É UM N° PRIMO!")
    else:
        print(f'{num} NÃO É UM N° PRIMO')

   




