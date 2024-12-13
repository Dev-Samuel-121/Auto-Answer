import json
import os

class FileJson:
    def __init__(self):
        pass

    def create(self, file_name, content,  path=""):
        """### CRIAR UM ARQUIVO JSON
        Cria um arquivo json a partir de um dicionario(`dict`)."""
        try:
            if path == "":
                path = os.getcwd()

            if not os.path.exists(path):
                os.makedirs(path)

            concret_file = f'{file_name}.json'
            file_path = os.path.join(str(path), str(concret_file))

            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(content, file, skipkeys=True, indent=None, separators=(',',':'))
        except Exception as e:
            print(f'ERRO DE CRIAÇÃO DO JSON: {e}')

    def read(self, file_name, path=""):
        """### LER ARQUIVOS JSON
        Ler um arquivo json e retorna um dicionario(`dict`)."""
        try:
            if path == "":
                path = os.getcwd()

            if not os.path.exists(path):
                os.makedirs(path)
            
            concret_file = f'{file_name}.json'
            file_path = os.path.join(str(path), str(concret_file))

            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    return json.load(file)
        except Exception as e:
            print(f'ERRO DE LEITURA DO JSON: {e}')
    
    def python_to_json(self, content):
        """### CONVERTER PYTHON PARA JSON
        Converte um dicionario(`dict`), para um json(`str`)."""
        try:
            return json.dumps(content, skipkeys=True, indent=None, separators=(',',':'))
        except Exception as e:
            print(e)
    
    def json_to_python(self, content):
        """### CONVERTER JSON PARA PYTHON
        Converte um json(`str`, `bytes`, `bytearray`), para um dicionario(`dict`)."""
        try:
            return json.loads(content)
        except Exception as e:
            print(e)
