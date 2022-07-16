import sys

if (len(sys.argv) < 2):
  sys.exit(f'Usage: python {sys.argv[0]} file.md')

oldfilename = sys.argv[1] # md
filename = oldfilename[0:oldfilename.find('.md')] # without extension
newfilename = filename + '.raw' # generated

with open(newfilename, 'w') as new:
  with open(oldfilename, 'r') as old:
    for line in old:
      if (line[0:8] == '<a href='):
        line = line[line.find('/') + 1:]
        line = line[line.find('/') + 1:]
        line = line[line.find('/') + 1:]
        image_name = line[0:line.find('"')]
        new.write(f'![image]({image_name})\n')
      else:
        new.write(line)
