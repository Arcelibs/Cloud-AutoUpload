import time
from datetime import datetime
from PIL import ImageGrab  
import os

upload_folder = r'C:/Users/cn/Desktop/Cloud-AutoUpload/upt'  

while True:
  now = datetime.now()
  filename = now.strftime(r'%Y%m%d_%H%M%S.png') 
  image = ImageGrab.grab()
  
  if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)
  
  image_path = os.path.join(upload_folder, filename)
  image.save(image_path)
  
  print('Saved screenshot to:', image_path)
  
  time.sleep(60)