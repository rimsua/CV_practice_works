from PIL import Image, ImageChops, ImageOps

image = Image.open("less_2/dog.jpg")

## Выбор интересуещей области
box = (350, 397, 585, 600)
roi = image.crop(box)
roi.save("less_2/result/roi.png")

## Маска (зеленая трава)
h, s, v = image.convert('HSV').split()

mask_h = h.point(lambda x: 255 if 45 <= x <= 110 else 0)
mask_s = s.point(lambda x: 255 if x >= 30 else 0)
mask_v = v.point(lambda x: 255 if x >= 120 else 0)

mask = ImageChops.multiply(mask_h, mask_s)
mask = ImageChops.multiply(mask, mask_v)
mask.save("less_2/result/mask_grass.png")

grass_only = Image.new("RGB", image.size, 'white')
grass_only.paste(image, mask=mask)
grass_only.save("less_2/result/grass_only.png") # захвачена не вся трава

## Инверсия маски
object_mask = ImageChops.invert(mask)
object_mask.save("less_2/result/mask_object.png")

object_only = Image.new("RGB", image.size, 'white')
object_only.paste(image, mask=object_mask)
object_only.save("less_2/result/object_only.png")