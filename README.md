![GG](https://github.com/Dec1o/Zabbix_HostAuto/assets/104839239/e450fa4c-59f5-4532-b6dd-6d00b19e1a13)

# Bibliotecas Utilizadas:

pathlib: Usada para manipular caminhos de arquivo de forma independente do sistema operacional.
zabbix_api: Fornece uma API para interagir com o Zabbix Server.
openpyxl: Utilizada para carregar e manipular arquivos Excel.


# Variáveis de Configuração:

file_path: Caminho para o arquivo hosts.xlsx que contém as informações dos hosts a serem cadastrados.
url, username, password: Informações de conexão com a instância do Zabbix.

   
# Conexão com o Zabbix:

O bloco try-except tenta estabelecer uma conexão com a API do Zabbix usando as credenciais fornecidas. Em caso de sucesso, imprime a versão da API do Zabbix. Em caso de falha, exibe uma mensagem de erro.


# Função para Criar Hosts:

A função create_host recebe parâmetros como nome do host, endereço IP, tipo de interface e porta de interface.
Utiliza a biblioteca zabbix_api para enviar uma solicitação de criação de host para o Zabbix Server.
Se o host é criado com sucesso, imprime uma mensagem confirmando o cadastro. Caso contrário, imprime uma mensagem de erro.


# Definição de Grupos de Hosts:

A variável groupids define os grupos de hosts aos quais os novos hosts serão associados.


# Carregamento do Arquivo Excel:

Utiliza a biblioteca openpyxl para carregar o arquivo hosts.xlsx.
Itera sobre as linhas do arquivo Excel a partir da segunda linha (ignorando o cabeçalho) e coleta os dados de cada host.
Loop para Cadastro de Hosts:

