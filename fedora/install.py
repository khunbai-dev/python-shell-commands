import subprocess, os, getpass
from pick import pick


def install_nerd_font():
    # Clear screen
  os.system('clear')
  print('')
  password = input('  Sudo Password: ')

  title = 'Please choose font to be installed (press SPACE to mark, ENTER to continue):'
  options = [
    'Inconsolata',
    'Hack',
    'FiraMono',
    'JetBrainsMono',
    'Noto',
    'SourceCodePro',
    'SpaceMono'
  ]
  selected = pick(options, title, multiselect=True, min_selection_count=1)

  download_urls = {
    'Inconsolata': 'https://github.com/ryanoasis/nerd-fonts/releases/download/v2.3.3/Inconsolata.zip',
    'Hack': 'https://github.com/ryanoasis/nerd-fonts/releases/download/v2.3.3/Hack.zip',
    'FiraMono': 'https://github.com/ryanoasis/nerd-fonts/releases/download/v2.3.3/FiraMono.zip',
    'JetBrainsMono': 'https://github.com/ryanoasis/nerd-fonts/releases/download/v2.3.3/JetBrainsMono.zip',
    'Noto': 'https://github.com/ryanoasis/nerd-fonts/releases/download/v2.3.3/Noto.zip',
    'SourceCodePro': 'https://github.com/ryanoasis/nerd-fonts/releases/download/v2.3.3/SourceCodePro.zip',
    'SpaceMono': 'https://github.com/ryanoasis/nerd-fonts/releases/download/v2.3.3/SpaceMono.zip'
  }

  user = getpass.getuser()

  for font in selected:
    font_name = font[0]
    download_url = download_urls[font_name]
    download_directory = f'/home/{user}/Downloads/'
    font_directory = download_directory + font_name
    new_directory = f'/usr/share/fonts/{font_name}'
    subprocess.run(f'mkdir -p {font_directory}', shell=True)
    subprocess.run(f'wget {download_url} -P {download_directory}', shell=True)
    subprocess.run(f'unzip {font_directory}.zip -d {font_directory}', shell=True)
    subprocess.run(f'echo {password} | sudo -S mv {font_directory} {new_directory}', shell=True)
    subprocess.run(f'rm -rf {font_directory}.zip', shell=True)

  subprocess.run(f'echo {password} | sudo -S fc-cache -v', shell=True)
  subprocess.run(f'echo {password} | sudo -S fc-list', shell=True)