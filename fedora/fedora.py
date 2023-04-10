from pick import pick
from . import network, session, install, disk
from shared.text_color import color


def show_main_menu():
  title = 'Please choose Fedora program menu: '
  options = [
    '[Network] List available samba shared directory',
    '[Session] Check running session (X11 or Wayland)',
    '[Installation]',
    '[Disk Manager]',
    '[x] Quit Program'
  ]
  option, index = pick(options, title)
  # print(option)
  # print(index)


  if option == '[Network] List available samba shared directory':
    network.list_available_samba()

  if option == '[Session] Check running session (X11 or Wayland)':
    session.session_type_check()

  if option == '[Installation]':
    install.show_menu()

  if option == '[Disk Manager]':
    disk.show_menu()

  if option == '[x] Quit Program':
    exit()
