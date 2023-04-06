import subprocess
import os
from shared.text_color import color

def list_available_samba():
    # Clear screen
    os.system('clear')

    print('')
    ip = input('  Enter samba server ip: ')
    # subprocess.run(f'smbclient -L {ip} -N', shell=True)
    output = subprocess.check_output(f'smbclient -L {ip} -N', shell=True, text=True)
    output = output.replace('\t', '')
    # print(repr(output))
    print(color(output, '5;31;40'))