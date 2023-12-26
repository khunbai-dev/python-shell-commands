import subprocess, os, getpass
from pick import pick
from shared.text_color import color
from shared import user


def show_menu():
  '''
  Description: Show all menu list.
  '''

  quit = False

  while not quit:
    title = 'Please choose command in [Disk] menu: '
    options = [
      'List all disk and partition',
      '<- Go back to main menu',
      '[x] Quit Program',
    ]
    option, index = pick(options, title)

    if option == 'List all disk and partition':
      os.system('clear')
      if user.is_root_user():
        output = subprocess.check_output('lsblk -f | grep -v loop', shell=True, text=True)
      else:
        output = subprocess.check_output('sudo lsblk -f | grep -v loop', shell=True, text=True)
      print(color('== sudo lsblk -f | grep -v loop ==', '0;30;41'))
      print(output)

      input("Press Enter to continue...")

    if option == '<- Go back to main menu':
      quit = True
      from .ubuntu import show_main_menu
      show_main_menu()

    if option == '[x] Quit Program':
      os.system('clear')
      exit()