from PIL import Image, ImageOps

image = Image.open("less_1/cow.jpg")
image.save("less_1/result/orig_cow.png")

print("Формат исходного изображения:", image.format)
print("Размер исходного изображения:", image.size)
print("Режим исходного изображения:", image.mode)

## Получение RGB-каналов

r, g, b = image.split()
red = ImageOps.colorize(r, black="white", white="red")
green = ImageOps.colorize(g, black="white", white="green")
blue = ImageOps.colorize(r, black="white", white="blue")

red.save("less_1/result/chanel_r.png")
green.save("less_1/result/chanel_g.png")
blue.save("less_1/result/chanel_b.png")

## Преобразование в оттенки серого

gray = image.convert('L')
gray.save("less_1/result/gray.png")

print("Режим gray:", gray.mode)

## Квантизация

quantized = image.quantize(colors=8).convert("RGB")
quantized.save("less_1/result/quantized_8.png")

print("Размер квантованного изображения:", quantized.size)
print("Режим квантованного изображения:", quantized.mode)


