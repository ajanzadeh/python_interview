## disk applation will return a jason of your basic sysstate on port 80
import psutil
import platform
import os
import time
from flask import Flask, json

def sysstate():
    msg = {
    'type' : 'register',
    'content' : {
        'cpu' : psutil.cpu_count(),
        'hostname' : os.uname()[1],
        'mem' : psutil.virtual_memory().total,
        'platform' : platform.platform(),
        'arch' : platform.architecture()[0],
        'time' : time.time(),
        'root_disk_usage' : psutil.disk_usage('/').percent
        }
      }
    return msg

api = Flask(__name__)
@api.route('/state', methods=['GET'])
def get_companies():
  return json.dumps(sysstate())

if __name__ == '__main__':
    api.run(port='80')
