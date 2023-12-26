import subprocess, os, getpass, time
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
      'Show listening port',
      '<- Go back to main menu',
      '[x] Quit Program',
    ]
    option, index = pick(options, title)

    if index == 0:  # 'Show listening port'
      os.system('clear')
      if user.is_root_user():
        output = subprocess.check_output('ss -tunlp | grep LISTEN', shell=True, text=True)
      else:
        output = subprocess.check_output('sudo ss -tunlp | grep LISTEN', shell=True, text=True)
        os.system('clear')
      print(color('== sudo ss -tunlp | grep LISTEN ==', '0;30;41'))
      print(output)

      input("Press Enter to continue...")

    if option == '<- Go back to main menu':
      quit = True
      from .ubuntu import show_main_menu
      show_main_menu()

    if option == '[x] Quit Program':
      os.system('clear')
      exit()