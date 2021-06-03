#!/usr/bin/python   
print('Content-type: text/html\r\n\r')

from prompt_toolkit import print_formatted_text, HTML

file1 = open('/logs/log.html', 'r')
Lines = file1.readlines()
stub = "<font color='#AAA'>"
stub_replace = '<span style="color:'
stub_replace_with = '<font color="'
line_start = "<font color='#AAA'>"
line_end = "</font>"
bad_word = '&bsol;'
stamp = None

import time
for j in range(45,len(Lines)-1):
    #Remove Stamp
    line = Lines[j][16:]
    #Remove Linebreaks & funky characters
    line = line.replace('\n','')
    line = line.replace(bad_word,'')
    line_numbers = sum(c.isdigit() for c in line)
    line_other = len(line) - line_numbers
    if line_other < 5:
        line = ''

    #Change Spans to Fonts
    line = line.replace(stub_replace,stub_replace_with)
    line = line.replace('</span>','</font>')
    #Add in boilerplate
    line = line_start + line + line_end
    if stamp is None:
        print_formatted_text(HTML(line))
        stamp = Lines[j][:16]
    else:
        prev_stamp = stamp
        stamp = Lines[j][:16]
        diff = int(stamp) - int(prev_stamp)
        diff = diff/1000000
        diff = min(diff,3)
        time.sleep(diff)
        print_formatted_text(HTML(line))





