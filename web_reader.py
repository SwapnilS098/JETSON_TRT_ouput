

from PIL import Image
import os

images=os.listdir(os.getcwd())
print(images)

image_path=os.path.join(os.getcwd(),images[0])
image=Image.open(image_path)
print(type(image))
image.show()
