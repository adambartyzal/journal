import sys

if (len(sys.argv) < 2):
  sys.exit(f'Usage: python {sys.argv[0]} file.raw')

oldfilename = sys.argv[1] # raw
filename = oldfilename[0:oldfilename.find('.raw')] # without extension
newfilename = filename + '.md' # generated

isList = False

with open(newfilename, 'w') as new:
  with open(oldfilename, 'r') as old:
    for line in old:      

      if len(line) == 1:
        if isList:
          isList = False
          new.write('\n')
        continue

      line = line.replace('<!-- omit in toc -->','')

      if (line[0] == '#'):
        line = '\n' + line
      elif (line[0] == '>'):
        line = '\n' + line
      elif (line[0:8] == '![image]'):
        image_name = line[line.find('(') + 1 : line.find(')')]
        line = f'\n<a href="../images/{filename}/{image_name}" target="_blank"><img src="../images/thumbnails/{filename}/{image_name}"></a>\n'
      elif (line[0:7] == '[audio]'):
        audio_name = line[line.find('(') + 1 : line.find(')')]
        line = f'\n<p><audio controls><source src="../images/{filename}/{audio_name}" type="audio/x-m4a"></audio></p>\n'
      elif (line[0:7] == '[video]'):
        audio_name = line[line.find('(') + 1 : line.find(')')]
        line = f'\n<p><video loop autoplay muted style="width:100%;max-width:800px"><source src="../images/{filename}/{audio_name}" type="video/mp4"></video></p>\n'
      else:
        if (line[0] == '-'):
          if not isList:
            new.write('\n') # empty line before lines
          line = line.replace('\n','')
          isList = True
        else:
          line = line.replace('\n','<br>')

      line += '\n'
      new.write(line)
