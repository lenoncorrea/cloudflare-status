# Monitorando services e locations da Cloudflare através da API
## Pré requisitos
Instale os pacotes Git e Python3.7 no servidor do Zabbix.

```bash
apt install git python3.7 python3-venv -y
```
## Baixando
```bash
cd /usr/lib/zabbix/externalscripts/
git clone https://github.com/lenoncorrea/cloudflare-status.git
```
## VirtualEnv
Crie um venv na pasta do nosso script e instale os requerimentos.
```python
python3 -m venv /usr/lib/zabbix/externalscripts/cloudflare-status/venv
. /usr/lib/zabbix/externalscripts/cloudflare-status/venv/bin/activate
pip install -r /usr/lib/zabbix/externalscripts/cloudflare-status/requirements.txt
```
## Ajustando
Vamos criar um link simbólico para nosso script em '/usr/lib/zabbix/externalscripts/'
```bash
ln -s /usr/lib/zabbix/externalscripts/cloudflare-status/cloudflare.py /usr/lib/zabbix/externalscripts/cloudflare.py

```
## Importe o template no Zabbix e o monitoramento será iniciado, se quiser também tem uma Dashboard básica para o Graffana.
### O template Zabbix é 'zbx_monitoring_cloudflare.xml' que está neste repositório.
### A Dashboard do Graffana é 'grafana_monitorando_cloudflare.json' que está neste repositório.

## Contribuição
Achou algum bug ou tem uma sugestão de melhoria? Envie-me!

## Licença
[MIT](https://github.com/lenoncorrea/cloudflare-status/blob/master/LICENSE)