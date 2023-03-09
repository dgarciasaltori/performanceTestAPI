import time
import random
import pyodbc

class TesteBanco:
    #Driver para acessar a Azure
    def __init__(self, server, database, username, password):
        driver= '{ODBC Driver 17 for SQL Server}'
        self.conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        self.cur = self.conn.cursor()
    #Função para executar a consulta no banco de dados
    def executar_consultas(self, num_consultas):
        tempos = []
        for i in range(num_consultas):
            consulta = "SELECT * FROM tabela WHERE id = %s" % random.randint(1, 10000)#pode alterar o numero de consultas do randon.
            inicio = time.time()
            self.cur.execute(consulta)
            fim = time.time()
            tempos.append(fim - inicio)
        return tempos
    #Função para Calculo de Métricas
    def calcular_metricas(self, tempos):
        media = sum(tempos) / len(tempos)
        mediana = sorted(tempos)[len(tempos) // 2]
        variancia = sum((t - media) ** 2 for t in tempos) / len(tempos)
        desvio_padrao = variancia ** 0.5
        return media, mediana, variancia, desvio_padrao
    #Função de avaliação da Métrica.
    def avaliar_desempenho(self, media):
        if media < 0.1:
            return "Excelente"
        elif media < 0.5:
            return "Bom"
        elif media < 1.0:
            return "Tolerável"
        else:
            return "Péssimo"
#Gerango resultados
if __name__ == '__main__':
    teste = TesteBanco("nome_servidor.database.windows.net", "nome_banco", "nome_usuario", "senha") #Altere as informações para o banco desejado
    tempos = teste.executar_consultas(100) #altere o valor para a quantidade de consultas desejadas
    media, mediana, variancia, desvio_padrao = teste.calcular_metricas(tempos)
    avaliacao = teste.avaliar_desempenho(media)
    print("Média: %.3f" % media)
    print("Mediana: %.3f" % mediana)
    print("Variância: %.3f" % variancia)
    print("Desvio Padrão: %.3f" % desvio_padrao)
    print("Avaliação: %s" % avaliacao)
