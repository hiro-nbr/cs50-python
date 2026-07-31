import sys

from pil import image

images = []

for arg in sys.argv[1:]:
    image = image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]],
)