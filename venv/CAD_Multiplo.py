from pathlib import Path
from zabbix_api import ZabbixAPI
from openpyxl import load_workbook

# Localização do arquivo hosts.xlsx relativa ao diretório principal do projeto
file_path = Path(__file__).resolve().parent.parent / 'hosts.xlsx'

# Conexão ao Zabbix:
url = ""
username = ""
password = ""

try:
    zabbix = ZabbixAPI(url, timeout=15)
    zabbix.login(username, password)
    print(f'Conectado na API do Zabbix, versão atual {zabbix.api_version()}')
except Exception as err:
    print(f'Falha ao se conectar na API do Zabbix, erro: {err}')

# Função para criar hosts:
def create_host(host, ip, interface_type, interface_port):
    try:
        create_host = zabbix.host.create({
            "groups": groups,
            "host": host,
            "interfaces": [{
                "type": interface_type,
                "main": 1,
                "useip": 1,
                "ip": ip,
                "dns": "",
                "port": interface_port
            }]
        })
        print(f'Host cadastrado com sucesso {host}')
    except Exception as err:
        print(f'Falha ao cadastrar host: erro {err}')

# Variáveis para definir Host group:
groupids = ['7']
groups = [{"groupid": groupid} for groupid in groupids]

# Carregar o arquivo Excel:
workbook = load_workbook(filename=str(file_path))  # Convertendo o caminho Path para uma string
sheet = workbook.active

# Loop para ler os dados do Excel e criar hosts:
for row in sheet.iter_rows(min_row=2, values_only=True):
    if len(row) != 4:
        print(f'Erro: Número incorreto de valores na linha: {row}')
        continue
    host, ip, interface_type, interface_port = row
    create_host(host, ip, interface_type, interface_port)
