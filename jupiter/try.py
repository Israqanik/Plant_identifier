import os
from PIL import Image

model_path = os.path.join(os.getcwd(), "jacka.jpg")
print(model_path)

ima = Image.open(model_path)
ima.show()