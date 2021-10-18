import subprocess
import json


def get():
    """execute SpeedTest and return data."""
    command = 'speedtest'

    process = subprocess.Popen([command, '--json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = process.communicate()

    if result:

        return json.loads(result[0].decode('utf-8'))
    else:
        return []


