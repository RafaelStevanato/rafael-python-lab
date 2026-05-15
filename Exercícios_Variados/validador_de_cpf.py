print("STVN - VALIDADOR DE CPF\n\n")

user_cpf = input("Por favor, insira seu CPF: ")
user_cpf = user_cpf.replace(".", "").replace("-","")


def validarPrimeiroDigito(user_cpf):

    multiplicador = 10
    soma = 0
    resto = 0
    
    for digit in user_cpf[0:9]:
        digit = int(digit)
        digit = digit * multiplicador
        
        soma = soma + digit
        multiplicador -= 1
    
    resto = soma % 11

    if resto < 2:
        primeiro_verificador = 0
    elif resto >= 2:
        primeiro_verificador = 11 -resto

    return (primeiro_verificador)


def validarSegundoDigito(user_cpf):
    
    multiplicador = 11
    soma = 0
    resto = 0
    
    for digit in user_cpf[0:10]:
        digit = int(digit)
        digit = digit * multiplicador
        soma = soma + digit
        multiplicador -= 1
    
    resto = soma % 11

    if resto < 2:
        segundo_verificador = 0
    elif resto >= 2:
        segundo_verificador = 11 -resto
        
    return(segundo_verificador)


while True:
    primeiro_verificador = validarPrimeiroDigito(user_cpf)
    segundo_verificador = validarSegundoDigito(user_cpf)
    if primeiro_verificador == int(user_cpf[9]) and segundo_verificador == int(user_cpf[10]):
        print("Seu CPF é válido!")
        break
    else:
        user_cpf = input("Seu CPF é inválido, por favor, insira um CPF válido: ")
        user_cpf = user_cpf.replace(".", "").replace("-","")
    