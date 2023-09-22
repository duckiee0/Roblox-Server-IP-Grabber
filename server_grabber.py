"""
Simple script that grabs the 
ip for the current roblox server 
you are / were in ~ lore
"""
from os.path import getctime, expanduser
from glob    import glob
from re      import findall

# Open recent log file.
LOG_FILE: list = open(
    file = max(glob(f"{expanduser('~')}\AppData\Local\Roblox\logs\*"), key = getctime),
).readlines()

def server_grabber() -> str:
    # NOTE: Check log data and only
    # NOTE: look for lines with
    # NOTE: "Connection accepted from".
    log_data: str = ''.join([line for line in LOG_FILE if 'Connection accepted from' in line]).replace('|', ':')
    # NOTE: Find all the server ips.

    if (server_ips := findall(r'\d+(?:\.\d+){3}:\d+', log_data)):
        # NOTE: Organize server ip's from
        # NOTE:  previous to current.
        server_ips[-1]: str = f'Current server: {server_ips[-1]}'

    # NOTE: Return final results.
    return ' -> '.join(server_ips)
        
print(server_grabber())
