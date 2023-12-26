import subprocess

def get_current_user() -> str:
  p = subprocess.run('whoami', shell=True, stdout=subprocess.PIPE, text=True)
  user = p.stdout.strip() #.strip() is removing /n (newline) from string
  return user

def is_root_user() -> bool:
  if get_current_user() == 'root':
    return True
  else:
    return False