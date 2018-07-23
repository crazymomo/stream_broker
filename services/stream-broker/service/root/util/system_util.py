import subprocess
import configparser
import requests

def system(command):
    # try to execute script
    try:
        response = subprocess.check_output(command, shell = True).decode('utf-8')
        response = response.strip("\r\n")
        response = response.strip("\n")
        return response
    except subprocess.CalledProcessError as e:
        return None
    
def config(section, key):
    try:
        config = configparser.ConfigParser()
        config.read('/opt/Config.ini')
        return config.get(section, key);
    except:
        return ''

def curl(url, params):
    try:
        r = requests.get(url, timeout=10, params=params)
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
        r = None
    if not r or r.status_code != 200:
        return None
    return r.text