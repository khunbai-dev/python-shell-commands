

def color(text:str, format_code:str) -> str :
  '''
  description: Return string with color format for printing.
  params:
    text, str, Text that we want to print.
    format_code, str, Code receive from print_format_table() ex. '0;30;41'
  '''
  prefix = '\x1b[' + format_code + 'm'
  subfix = '\x1b[0m'
  text_with_format = prefix + text + subfix
  return text_with_format


def print_format_table():
  """
  description: prints table of formatted text format options
               Ex.
                 format_code = '0;30;41'
                 prefix = '\x1b[' + format_code + 'm'
                 subfix = '\x1b[0m'
                 text = 'Hello World'
                 text_with_format = prefix + text + subfix
                 print(text_with_format)
  """
  for style in range(8):
    for fg in range(30,38):
      s1 = ''
      for bg in range(40,48):
        format = ';'.join([str(style), str(fg), str(bg)])
        # s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
        s1 += f'\x1b[{format}m {format} \x1b[0m'

      print(s1)
    print('\n')