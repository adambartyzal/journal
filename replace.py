import sys

if (len(sys.argv) < 2):
  sys.exit(f'Usage: python {sys.argv[0]} file.raw')

rawfilename = sys.argv[1]
newfilename = rawfilename[0:rawfilename.find('.raw')] + '.md'

with open(newfilename, 'w') as new:
  with open(rawfilename, 'r') as old:
    for line in old:
      if (line[0:8] == '![image]'):
        image_name = line[line.find('(') + 1 : line.find(')')]
      else:
        new.write(line)

#<a href="../images/2022_july/1_1.jpg" target="_blank"><img src="../images/thumbnails/2022_july/1_1.jpg"></a>
