from desker.faster_rcnn import load_model, predict_elements_demo
from PIL import Image

# import the model
load_model()

# load a test image
img = Image.open("./download.png").convert("RGB")

# run the model
ann_img = predict_elements_demo(img)

# show
ann_img.show()
