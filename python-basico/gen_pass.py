import random


def gen_pass():
    lista = list(range(33,94)) + list(range(97,123))
    lista= lista+[95,125,241,209]
    password= []
    for i in range(15):
        character = random.choice(lista)
        password.append(chr(character))
    password = ''.join(password)
    return password

def main():
    passwd = gen_pass()
    print (f"tu nueva contraseña es: {passwd}")


if __name__ == "__main__":
    main()
