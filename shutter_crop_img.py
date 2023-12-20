from PIL import Image


# crop watermark preview img shutter
filename = "3.webp"
with Image.open(filename) as img:
    img.load()

cropped_img = img.crop((0, 0, img.width, img.height - 20))
# cropped_img.size
cropped_img.save(filename)
# cropped_img.show()


# print(img.size)
# img.show()


