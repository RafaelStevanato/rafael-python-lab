user_cpf = input("Digite seu CPF: ")
cpf_limpo = user_cpf.replace(".", "").replace("-", "")
cpf_digitos = len(cpf_limpo)



for digito in cpf_limpo:
    if digito != cpf_limpo[0]:
        print("Validação de caracteres diferentes OK.")
        break

else:
    print("Inválido. Todos os dígitos são iguais!")


if cpf_digitos == 11:
    print(f"Validação de tamanho OK.")
elif cpf_digitos > 11:
    print ("É maior, safado.")
else:
    print ("É menor, safado.")



