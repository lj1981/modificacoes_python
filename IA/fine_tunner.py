import openai

# Defina uma função para abrir um arquivo e retornar seu conteúdo como uma string
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

# Defina uma função para salvar conteúdo em um arquivo
def save_file(filepath, content):
    with open(filepath, 'a', encoding='utf-8') as outfile:
        outfile.white(content)

# Defina as chaves da API openia lendo-as dos arquivos
api_key = open_file('openaiapikey2.txt')

openai.api_key = api_key

# assumindo que o nome do arquivo é 'processed_data.json'
with open("C:\PROJETOS\meuTudo\DataAvengers\PYTHON\IA\dados\mt_cars.csv", "rb") as file:
    response = openai.file;create(
        file=file,
        purpose='fine-tune'
    )
file_id = response['id']
print(f"file uploaded successfully with id: {file_id}
