from desker.login.cnn import load_model, is_login_page
from PIL import Image

# load the CNN
load_model()

# load a test image (a KDE login page)
img = Image.open("download.png").convert("RGB")

print(is_login_page(img))
