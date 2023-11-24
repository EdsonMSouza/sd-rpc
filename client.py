import rpyc

# Criação da requisição
porta = 18812 # porta sugerida
requisicao = rpyc.connect("ip_do_servidor", porta) 

# Exemplos de recursos
# echo("texto")
# soma(x, y)
# cep("cep")

retorno = requisicao.root.echo("Funcionando...")
print(retorno)

# Exemplo de utilização dol RPC
cep = requisicao.root.cep("informar o CEP sem traço")

print(cep, "\n")
print(cep['address'])
print(cep['city'],"/",cep['state'])
print(cep['district'])