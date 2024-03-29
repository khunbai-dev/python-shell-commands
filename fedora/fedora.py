from pick import pick
from . import network, session, install, disk
from shared.text_color import color


def show_main_menu():
  title = 'Please choose Fedora program menu: '
  options = [
    f'[Network]         Total menu num. = {len(network.OPTION_LIST)}',
    f'[Session]         Total menu num. = {len(session.OPTION_LIST)}',
    '[Installation]',
    '[Disk Manager]',
    '[x] Quit Program'
  ]
  option, index = pick(options, title)
  # print(option)
  # print(index)


  if option == '[Network]':
    network.show_menu()

  if option == '[Session]':
    session.show_menu()

  if option == '[Installation]':
    install.show_menu()

  if option == '[Disk Manager]':
    disk.show_menu()

  if option == '[x] Quit Program':
    exit()
