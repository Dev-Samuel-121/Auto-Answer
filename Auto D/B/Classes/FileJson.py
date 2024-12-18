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
            print(f'ERRO NA CONVERÇÃO DE PYTHON PARA JSON: {e}')
    
    def json_to_python(self, content):
        """### CONVERTER JSON PARA PYTHON
        Converte um json(`str`, `bytes`, `bytearray`), para um dicionario(`dict`)."""
        try:
            return json.loads(content)
        except Exception as e:
            print(f'ERRO NA CONVERÇÃO DE JSON PARA PYTHON: {e}')
    
    def modificar_json(self, file_name, add_content, rm_content,  path=""):
        """### MODIFICAR JSON
        Modifica um json já criado, adicionado e/ou removendo item."""
        try:
            content = self.read(file_name, path)
            content.update(add_content)

            for item in list(rm_content):
                del content[item]

            self.create(file_name, content, path)
        except Exception as e:
            print(f'ERRO NA MODIFICAÇÃO DO JSON: {e}')
