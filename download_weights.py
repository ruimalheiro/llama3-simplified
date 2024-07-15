import gdown
import zipfile
import os

url = 'https://drive.google.com/uc?id=1eVGJV2Ma0Xpf6pIaPjBRoyIb0a7GtPHn'
output = 'weights.zip'

gdown.download(url, output, quiet=False)

with zipfile.ZipFile(output, 'r') as zip_ref:
    zip_ref.extractall()

os.remove(output)