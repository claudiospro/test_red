from datetime import datetime

from lib import red
from lib import file


def execute(file_path):
    r = red.get()
    c = r['client']
    s = r['server']

    header = ['download', 'upload', 'ping', 'timestamp', 'timestamp_local',
              'server_name', 'server_cc', 'server_sponsor', 'server_id', 'server_latency',
              'client_ip', 'client_lat', 'client_lon', 'client_isp', 'client_isprating', 'client_cc']
    data = [
        r['download'], r['upload'], r['ping'], r['timestamp'], datetime.now().strftime('%Y-%m-%d %H:%M'),
        s['name'], s['cc'], s['sponsor'], s['id'], s['latency'],
        c['ip'], c['lat'], c['lon'], c['isp'], c['isprating'], c['country'],
    ]

    file.save(file_path, data, header)
