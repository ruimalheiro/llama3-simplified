import gdown
import zipfile
import os

url = 'https://drive.google.com/uc?id=13p5hlyZ-axPjF5IfDm895SHVTBVQeVuW'
output = 'weights.zip'

gdown.download(url, output, quiet=False)

with zipfile.ZipFile(output, 'r') as zip_ref:
    zip_ref.extractall()

os.remove(output)