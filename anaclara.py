valor = float(input("digite o valor em R$"))
porc = float(input("digite a porcentagem do desconto"))
valDeconto = (valor * porc)/100
pagamento = valor - valDeconto
print("""valor total: {valor}
      desconto: {valDesconto} %
      valor final: R${pagamento}""")
