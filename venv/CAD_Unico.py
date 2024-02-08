from zabbix_api import ZabbixAPI

# Conexão ao Zabbix:
url = ""
username = ""
password = ""

try:
    zabbix = ZabbixAPI(url, timeout=15)
    zabbix.login(username, password)
    print(f'Conectado na API do Zabbx, versão atual {zabbix.api_version()}')
except Exception as err:
    print(f'Falha ao se conectar na API do zabbix, erro: {err}')

# Variavel para as opções de interface:
info_interfaces = {
    "1": {"type": "agent", "id": "1", "port": "10050"},
    "2": {"type": "SNMP", "id": "2", "port": "161"},
}

# Variaveis para definir Host group:
groupids = ['24']
groups = [{"groupid": groupid} for groupid in groupids]

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

# Uso da função "create_host" para adicionar hosts:
create_host('teste', '192.168.0.1', info_interfaces['1']['id'], info_interfaces['1']['port'])