import pandas as pd

# Carregar o arquivo CSV
caminho_arquivo = r'C:\Users\015545\Desktop\Banco\Dados\Dados analíticos de funil.csv'
df = pd.read_csv(caminho_arquivo)

# Fazer as alterações nas colunas com base nas condições especificadas
df['category'] = df['category'].replace({'05 - Viu Oferta': 'Credito Aprovado',
                                         '13 - Incluiu proposta': 'Tiveram aumento de limite',
                                         '06 - Decisão oferta' : 'Indecisos',
                                         '11 - Pediu renda': 'Pediu aumento de limite',
                                         '03 - Resultado simulação': 'Credito não aprovado',
                                         '10 - Pediu dados bancários':'Incluiram novos produtos',
                                         '14 - Busca link de assinatura': 'Novas contas',
                                         '09 - Pediu CEP':'Seguro',
                                         '01 - CPF' : 'Novos Investidores',
                                         '04 - Elegibilidade': 'Portabilidade de salário',
                                         '15 - Exibe link de assinatura':'Cartão debito',
                                         '08 - Pediu Data Nasc.': 'Cratão de credito',
                                         '07 - Pediu nome':'Fecharam a conta',
                                         '12 - Tenta inclur proposta' : 'Prejuizo',
                                         '02 - Consulta CAIXA':'Consulta'})

# Salvar o arquivo CSV com as alterações
df.to_csv(caminho_arquivo, index=False)

print("As alterações foram feitas e o arquivo foi salvo com sucesso.")
