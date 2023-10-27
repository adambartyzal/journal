import sys, os
from PIL import Image

def get_date_taken(path):
  exif = Image.open(path)._getexif()
  if not exif:
    raise Exception('Image {0} does not have EXIF data.'.format(path))
  return exif[36867]

if (len(sys.argv) < 2):
  sys.exit(f'Usage: python {sys.argv[0]} folder with images')

folder_name = sys.argv[1]
images = sorted(os.listdir(folder_name))

print(images)

days = [0] * 31
print(days)

for image in images:
  path = folder_name + image
  date = get_date_taken(path)
  day = int(str(date).split(' ')[0].split(':')[2])
  days[day - 1]  = days[day - 1] + 1
  new_path = folder_name + f'{day}_{days[day - 1]}.jpg'
  os.rename(path, new_path)

print(days)
