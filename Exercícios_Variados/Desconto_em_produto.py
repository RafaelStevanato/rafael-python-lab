nome_produto = input("Digite o nome do produto: ")
preco_produto = input ("Digite o preço do produto: ")

preco_produto = float(preco_produto)

preco_produto_com_desconto = preco_produto * 0.9
economia = preco_produto - preco_produto_com_desconto

print(
    f"O produto {nome_produto} custa R${preco_produto:.2f} "
    f"e com 10% de desconto custa R${preco_produto_com_desconto:.2f}. "
    f"Você economizou R${economia}."
)
