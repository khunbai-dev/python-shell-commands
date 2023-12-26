from pick import pick
from . import network, disk
from shared.text_color import color


def show_main_menu():
  title = 'Please choose Ubuntu program menu: '
  options = [
    '[Network]',
    '[Disk]',
    '[x] Quit Program'
  ]
  option, index = pick(options, title)
  # print(option)
  # print(index)


  if option == '[Network]':
    network.show_menu()

  if option == '[Disk]':
    disk.show_menu()

  if option == '[x] Quit Program':
    exit()
