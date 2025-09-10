import sys, os
from PIL import Image

def getDateTaken(path):
  exif = Image.open(path)._getexif()
  if not exif:
    raise Exception('Image {0} does not have EXIF data.'.format(path))
  return exif[36867]

if (len(sys.argv) < 2):
  sys.exit(f'Usage: python {sys.argv[0]} folder with images')

folderName = sys.argv[1]
images = sorted(os.listdir(folderName))

days = [0] * 31

for originalFileName in images:
  path = folderName + originalFileName
  try:
    date = getDateTaken(path)
  except:
    continue
  day = int(str(date).split(' ')[0].split(':')[2])
  days[day - 1]  = days[day - 1] + 1
  newFileName = f'{day:02d}_{days[day - 1]}.jpg'

  print(f'![image]({newFileName})')
  os.rename(path, folderName + newFileName)

