
import string
import random

characters = list(string.ascii_letters + string.digits + " Ññ!@#$%^&*()")

def generate_password():
    password_length = int(input("Cuantos carácteres quieres que tenga la contraseña? "))
    
    random.shuffle(characters)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    
    password = "" .join(password)
    print(password)

option = input("Quieres generar la contraseña? (Si/No): ").capitalize()

if option == "Si":
    generate_password()
elif option == "No":
    print("Programa finalizado,que tengas un buen día! ")
    quit()
else:
    print("Insercción incorrecta, porfavor introduce Si o No")
    quit()