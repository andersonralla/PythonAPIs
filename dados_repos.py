
import requests
import pandas as pd
from math import ceil

class DadosRepositorios:

    def __init__(self, owner):
        self.owner = owner
        self. api_base_url = 'https://api.github.com'
        self.access_token = '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'
        self.headers = {'Authorization': 'Bearer ' + self.access_token, 'X-GitHub-Api-Version': '2022-11-28'}
        

    def lista_repositorios (self):
        repos_list = []

        response = requests.get(f'https://api.github.com/users/{self.owner}')
        num_pages = ceil(response.json()['public_repos']/30)

        for page_num in range(1,num_pages + 1):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url,headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)

        return repos_list
    

    def nomes_respos(self, repos_list):
        repo_names = []

        for page in repos_list:
            for repo in page:
                try:
                    repo_names.append(repo['name'])
                except:
                    pass

        return repo_names
    

    def nomes_linguagens(self,repos_list):
        repo_languages=[]
        
        for page in repos_list:
            for repo in page:
                try:
                    repo_languages.append(repo['language'])
                except:
                    pass
        return repo_languages
    

    def cria_df_linguagens(self):

        repositorios = self.lista_repositorios()
        nomes = self.nomes_respos(repositorios)
        linguagens = self.nomes_linguagens (repositorios)

        dados = pd.DataFrame()
        dados['repository_name'] = nomes
        dados['language'] = linguagens

        return dados

amazon_rep = DadosRepositorios('amzn')
ling_mais_usada_amzn = amazon_rep.cria_df_linguagens()
print(ling_mais_usada_amzn)