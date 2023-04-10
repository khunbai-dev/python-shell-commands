import subprocess, os, getpass
from pick import pick
from shared.text_color import color


def show_menu():
  '''
  Description: Show all menu list.
  '''

  quit = False

  while not quit:
    title = 'Please choose command in [Disk] menu: '
    options = [
      'List all disk and partition with type',
      '<- Go back to main menu',
      '[x] Quit Program',
    ]
    option, index = pick(options, title)

    if option == 'List all disk and partition with type':
      output = subprocess.check_output('lsblk --output NAME,SIZE,TYPE,FSTYPE', shell=True, text=True)
      print(output)

      input("Press Enter to continue...")

    if option == '<- Go back to main menu':
      from .fedora import show_main_menu
      show_main_menu()

    if option == '[x] Quit Program':
      quit = True

  print(color('Exit', '5;31;40'))