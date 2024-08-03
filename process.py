import sys

tags = ['#', '-', '!', '[']

def isSpecial(line):
  return line[0] in tags

if (len(sys.argv) < 2):
  sys.exit(f'Usage: python {sys.argv[0]} file.raw')

file = sys.argv[1] # raw

lines = []
prevLine = '_'

f = open(file, 'r')
for line in f:
  if isSpecial(line) and not isSpecial(prevLine):
    lines.append('\n')
  else:
    if len(line) > 2:
      if line[-2] != '\\':
        line = line[:-1] + '\\\n'

  if len(line) == 1:
    if isSpecial(prevLine):
      lines.append(line)
  else:
    lines.append(line)
  prevLine = line

f.close()

f = open(file, 'w')
f.writelines(lines)
f.close
