print("Desconto INSS")
nome = input("Nome: ")
salario_bruto = float(input("Salário bruto: ").replace(",","."))
if(salario_bruto >=3000):
   desconto_inss = salario_bruto * 0.11
elif(salario_bruto >=2000):
    desconto_inss = salario_bruto * 0.09
else:
    desconto_inss = salario_bruto * 0.08

if(salario_bruto >=2000):
    desconto_vale_transporte = salario_bruto * 0.06
else:
    desconto_vale_transporte = salario_bruto * 0.05

if(salario_bruto >=3000):
    bonus = 300
else:
    bonus = 200
if(salario_bruto >=3000):
    cargo = "Acionista"
elif(salario_bruto >=200):
    cargo = "Gerente"
else:
    cargo = "Vendedor"
salario_liquido = salario_bruto - (desconto_inss + desconto_vale_transporte) + bonus
print(f"Nome: {nome}")
print(f"Salário bruto: {salario_bruto:.2f}" .replace(".",","))
print(f"Desconto INSS: {desconto_inss:.2f}".replace(".",","))
print(f"Desconto vale trabsporte: {desconto_vale_transporte:.2f}".replace(".",","))
print(f"Bonus: {bonus:.2f}".replace(".",","))
print(f"Cargo: {cargo}")
print(f"Salário Líquido: {salario_liquido:.2f}".replace(".",",")) #O .2f é para limitar em apenas 2 casas decimais
