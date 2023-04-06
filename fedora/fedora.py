from pick import pick
from . import network, session, install
from shared.text_color import color


def show_main_menu():
  title = 'Please choose Fedora program to run: '
  options = [
    '[Network] List available samba shared directory',
    '[Session] Check running session (X11 or Wayland)',
    '[Install] Install Nerd fonts',
  ]
  option, index = pick(options, title)
  # print(option)
  # print(index)


  if option == '[Network] List available samba shared directory':
    network.list_available_samba()

  if option == '[Session] Check running session (X11 or Wayland)':
    session.session_type_check()

  if option == '[Install] Nerd fonts':
    install.install_nerd_font()
