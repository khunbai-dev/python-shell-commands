import subprocess, os
from pick import pick


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