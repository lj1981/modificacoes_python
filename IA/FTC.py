import openai

# Insira sua chave da OpenAI aqui
openai.api_key = "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"

# Insira o nome do seu modelo aqui
model_name = "davinci:ft-meutudo-2023-03-15-19-13-18"

# Insira o nome do seu conjunto de dados aqui
new_data_file = "OpenAI _ Model_Engine.csv"

# Carregue o modelo
model = openai.FineTune.load(model_name)

# Atualize o modelo com os novos dados
model.update(new_data_file)

# Salve o modelo atualizado
model.save(model_name)
