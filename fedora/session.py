import subprocess, os
from pick import pick
from shared.text_color import color

OPTION_LIST = [
  'Check running session (X11 or Wayland)'
]

def show_menu():
  quit = False

  while not quit:
    title = 'Please choose command in [Session] menu: '
    options = [
      OPTION_LIST[0],
      '<- Go back to main menu',
      '[x] Quit Program',
    ]
    option, index = pick(options, title)

    if option == OPTION_LIST[0]:
      os.system('clear')
      session_type_check()
      input("Press Enter to continue...")

    if option == '<- Go back to main menu':
      quit = True
      from .fedora import show_main_menu
      show_main_menu()

    if option == '[x] Quit Program':
      os.system('clear')
      exit()


def session_type_check():
  output = subprocess.check_output('loginctl', shell=True, text=True)
  output = output.split()
  #== Remove title and comments at the last
  output = output[5:]
  output = output[:len(output) - 3]
  #==
  session_id_list = output[0:len(output):5]  # extract data, list[start:stop:step]
  user_list = output[2:len(output):5]

  title = 'Please choose user:'
  option, index = pick(user_list, title)

  os.system('clear')

  subprocess.run(f'loginctl show-session {session_id_list[index]} -p Type', shell=True)