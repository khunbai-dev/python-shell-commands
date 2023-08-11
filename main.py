#!/usr/bin/python

import argparse, subprocess, time

from shared.text_color import color, print_format_table


def debug():
  # print_format_table()
  # subprocess.run('mkdir -p /home/khunbai/test22', shell=True)
  # subprocess.run('echo {password} | sudo -S mkdir -p /mnt/test33', shell=True)
  pass



def option_notice():
  '''
  desc: Notice user to specific any option for using the program and exit.
  '''
  print('Please specific option to use the program. Ex. -f --fedora')
  for x in range (0,5):  
    b = "Exiting program" + " ." * x
    print (b, end="\r")
    time.sleep(1)
  print("Exiting the program . . . .")
  return


def main():
  '''
  Description: Check command argument and pass to specific function or app.
  '''
  parser = argparse.ArgumentParser(
    description="Description of the program.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
  )
  parser.add_argument("-f", "--fedora", action="store_true", help="Run command application on Fedora.")
  args = parser.parse_args()
  # config = vars(args)
  # print(config)

  func = option_notice

  if args.fedora:
    from fedora import fedora
    func = fedora.show_main_menu
    # print(args.fedora)

  # No specific option
  func()


if __name__ == "__main__":
	main()