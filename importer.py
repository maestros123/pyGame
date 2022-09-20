from PIL import Image
 
image = Image.open('green.png')
image = image * 4
image.show()