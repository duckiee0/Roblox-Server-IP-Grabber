"""
Simple script that grabs the 
ip for the current roblox server 
you are / were in ~ lore
"""
from os.path import getctime, expanduser
from re      import findall
from glob    import glob

# Open recent log file.
LOG_FILE = open(
    file     = max(glob(f"{expanduser('~')}\AppData\Local\Roblox\logs\*"), key = getctime),
    encoding = 'utf-8'
).readlines()

def server_grabber():
    # Check log data and only
    # look for lines with
    # "Connection accepted from".
    log_data       = ''.join([line for line in LOG_FILE if 'Connection accepted from' in line]).replace('|', ':')
    # Find all the server ips.
    server_ips     = findall(r'\d+(?:\.\d+){3}:\d+', log_data)
    # Organize server ip's from
    # previous to current.
    server_ips[-1] = f'Current server: {server_ips[-1]}'
    # Return final results.
    return ' -> '.join(server_ips)
        
print(server_grabber())