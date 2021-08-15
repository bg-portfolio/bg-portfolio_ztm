from PIL import Image, ImageFilter
# basic pillow img processing

img = Image.open("./pokedex/bulbasaur.jpg")
# filtered = img.filter(ImageFilter.BLUR)  # BLUR, SHARPEN, SMOOTH etc more in docs.
# filtered = img.convert("L") # converted into a grayscale - "L" mode here, mode avaible - in docs.
# filtered.save("./pokedex/_bulba.png")
# img.show() # opens an image in a explorer
# img.resize((width, height) <- tuple) , img.rotate(degrees 90/180/270 etc) other methods avaible in docs
# box = [100, 100, 400, 400]
# img.crop(box) # cropes the img for position in the box
# for resize we can use .thumbnail method to try to keep an aspect ratio of the img
