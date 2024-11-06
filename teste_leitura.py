import pandas as pd
import os

class LeitorCSV:
    def __init__(self, ano_inicial, ano_final):
        """
        Inicializa o objeto LeitorCSV com os anos inicial e final.
        :param ano_inicial: Ano inicial para o intervalo de leitura
        :param ano_final: Ano final para o intervalo de leitura
        """
        self.ano_inicial = ano_inicial
        self.ano_final = ano_final

    def listar_arquivos(self, ano):
        """
        Lista os arquivos de um determinado ano.
        :param ano: Ano para o qual os arquivos serão listados
        :return: Lista de arquivos encontrados no diretório
        """
        diretorio = f'Dados Leichmaniose/Mortalidade/BA/{ano}'
        if os.path.exists(diretorio):
            return os.listdir(diretorio)
        else:
            print(f'Diretório {diretorio} não encontrado.')
            return []

    def ler_arquivos(self, ano, arquivos):
        """
        Lê e imprime os primeiros registros dos arquivos CSV de um ano.
        :param ano: Ano dos arquivos
        :param arquivos: Lista de arquivos para ler
        """
        print(f'-------------------inicio---------------------{ano}\n')
        for arqsep in arquivos:
            diretorio = f'Dados Leichmaniose/Mortalidade/BA/{ano}/{arqsep}'
            if os.path.exists(diretorio):
                df = pd.read_csv(diretorio, sep=';', encoding='ISO-8859-1', header=0, skiprows=4, skipfooter=14, engine='python')
                print(f'Arquivo: {arqsep}')
                print(df.head())  # Exibe as primeiras linhas do arquivo
                print()
            else:
                print(f'Arquivo {diretorio} não encontrado.')
        print(f'-------------------final---------------------{ano}\n')

    def coletar_dados(self):
        """
        Realiza a coleta de dados para o intervalo de anos especificado.
        """
        ano = self.ano_inicial
        while ano >= self.ano_final:
            print(f'Coletando dados para o ano {ano}...')
            arquivos = self.listar_arquivos(ano)
            if arquivos:
                self.ler_arquivos(ano, arquivos)
            ano -= 1

# Criando uma instância da classe LeitorCSV
leitor = LeitorCSV(2024, 2017)

# Chamando o método para coletar os dados
leitor.coletar_dados()
