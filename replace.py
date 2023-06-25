import sys

if (len(sys.argv) < 2):
  sys.exit(f'Usage: python {sys.argv[0]} file.raw')

oldfilename = sys.argv[1] # raw
filename = oldfilename[0:oldfilename.find('.raw')] # without extension
newfilename = filename + '.md' # generated

with open(newfilename, 'w') as new:
  with open(oldfilename, 'r') as old:
    for line in old:
      if (line[0:8] == '![image]'):
        image_name = line[line.find('(') + 1 : line.find(')')]
        new.write(f'<a href="../images/{filename}/{image_name}" target="_blank"><img src="../images/thumbnails/{filename}/{image_name}"></a>\n')
      elif (line[0:7] == '[audio]'):
        audio_name = line[line.find('(') + 1 : line.find(')')]
        new.write(f'<p><audio controls><source src="../images/{filename}/{audio_name}" type="audio/x-m4a"></audio></p>\n')
      else:
        new.write(line)
