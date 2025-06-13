# configurações
reg_user = "admin"
reg_pass = "py123"
tentativas = 3

# introdução
print("+++ SISTEMA de LOGIN +++")

# loop
while tentativas > 0:
    # user input
    in_user = input("Usuario: ")
    in_pass = input("Senha: ")

    # check info
    if in_user == reg_user and in_pass == reg_pass:
        print("Usuario e senha corretos! Bem vindo(a)!")
        break # freio do loop
    else:
        tentativas -= 1 # reduz as tentativas em 1
        if tentativas > 0:
            print(f"Usuario ou senha incorreto! (Tentativas restantes: {tentativas})")
        else:
            print(f"Usuario ou senha incorreto! (Tentativas esgotadas, entre em contato com o suporte.)")
