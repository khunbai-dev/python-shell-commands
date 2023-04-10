import subprocess
import os
from pick import pick
from shared.text_color import color


def show_menu():
  quit = False

  while not quit:
    title = 'Please choose command in [Session] menu: '
    options = [
      'List available samba shared directory',
      '<- Go back to main menu',
      '[x] Quit Program',
    ]
    option, index = pick(options, title)

    if option == 'List available samba shared directory':
      os.system('clear')
      list_available_samba()
      input("Press Enter to continue...")

    if option == '<- Go back to main menu':
      quit = True
      from .fedora import show_main_menu
      show_main_menu()

    if option == '[x] Quit Program':
      # Clear screen
      os.system('clear')
      exit()


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