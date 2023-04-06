#!/usr/bin/python

import argparse, subprocess

from shared.text_color import color, print_format_table


def debug():
  # print_format_table()
  # subprocess.run('mkdir -p /home/khunbai/test22', shell=True)
  # subprocess.run('echo {password} | sudo -S mkdir -p /mnt/test33', shell=True)

  print('Please specific option.')

  return


def main():
  '''
  Description: Check command argument and pass to specific function or app.
  '''
  parser = argparse.ArgumentParser(
    description="Description of the program.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
  )
  parser.add_argument("-f", "--fedora", action="store_true", help="Run usually command application on Fedora.")
  args = parser.parse_args()
  # config = vars(args)
  # print(config)

  func = debug

  if args.fedora:
    from fedora import fedora
    func = fedora.show_main_menu
    # print(args.fedora)

  # No specific option
  func()


if __name__ == "__main__":
	main()