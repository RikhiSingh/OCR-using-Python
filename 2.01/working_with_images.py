from PIL import Image

# load the image into memory
image_file = "data/page_01.png"

# load this object using Image from PIL library into this variable
image = Image.open(image_file)

# can see the pillow object data (metadata)
print(image)

# filter size from the metadata
print(image.size)

# open and view the image
image.show()

# rotate the image but not really cropped well !
image.rotate(90).show()

# save as new file (the directory should exist beforehand)
image.save("temp/page_ocr.png")