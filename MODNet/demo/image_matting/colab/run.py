import os

# # clone the repository
# %cd /content
# if not os.path.exists('MODNet'):
#   !git clone https://github.com/ZHKKKe/MODNet
# %cd MODNet/

# dowload the pre-trained ckpt for image matting

# checkpoint download
# https://drive.google.com/drive/folders/1umYmlCulvIFNaqPjwod1SayFmSRHziyR 에서 pretrained/modnet_photographic_portrait_matting.ckpt 이걸 다운

# upload image
import shutil
from google.colab import files

# clean and rebuild the image folders
# input_folder = 'demo/image_matting/colab/input'
input_folder = './input'
if os.path.exists(input_folder):
  shutil.rmtree(input_folder)
os.makedirs(input_folder)

output_folder = './output'
if os.path.exists(output_folder):
  shutil.rmtree(output_folder)
os.makedirs(output_folder)

# upload images (PNG or JPG)
image_names = list(files.upload().keys())
for image_name in image_names:
  shutil.move(image_name, os.path.join(input_folder, image_name))
