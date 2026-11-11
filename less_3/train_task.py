import numpy as np
from PIL import Image

img_pil = Image.open("less_3/dog_2.jpg").convert("RGB")
img_arr = np.array(img_pil)

print(img_arr.shape)
print(img_arr.dtype)
print(img_arr.min(), img_arr.max())

## Яркость и контраст (numpy)

def change_brightness(arr, delta):
    work = arr.astype(np.int16)
    work = work + delta
    return np.clip(work, 0, 255).astype(np.uint8)

def change_contrast(arr, factor):
    work = arr.astype(np.float32)
    work = (work - 128) * factor + 128
    return np.clip(work, 0, 255).astype(np.uint8)

## Инверсия и квантизация (numpy)

def invert(arr):
    return 255 - arr

def quantize(arr, levels):
    if levels < 2:
        raise ValueError("Значение levels должно быть >= 2")

    work = arr.astype(np.float32)
    work = np.round(work / 255 * (levels - 1))
    work = work / (levels - 1) * 255
    return work.astype(np.uint8)

## Результаты

bright = change_brightness(img_arr, 50)
contrast = change_contrast(img_arr, 1.8)
inverted = invert(img_arr)
quantized = quantize(img_arr, 4)

Image.fromarray(bright).save("less_3/result/bright.png")
Image.fromarray(contrast).save("less_3/result/contrast.png")
Image.fromarray(inverted).save("less_3/result/inverted.png")
Image.fromarray(quantized).save("less_3/result/quantized.png")