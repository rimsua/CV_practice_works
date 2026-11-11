import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img_pil = Image.open("less_3/dog_2.jpg").convert("RGB")
img_arr = np.array(img_pil)
gray_arr = np.array(img_pil.convert('L'))

## Гистограмма яркости
fig, ax = plt.subplots(figsize=(8, 5)) 
ax.hist(gray_arr.ravel(), bins=256, range=(0, 256)) 
ax.set_xlabel("Значение яркости") 
ax.set_ylabel("Число пикселей") 
fig.savefig("less_3/result/hist_gray.png", dpi=150) 
plt.close(fig)

## Гистограммы каналов RGB
fig, ax = plt.subplots(figsize=(8, 5)) 
colors = ["red", "green", "blue"] 
labels = ["R", "G", "B"]

for channel in range(3):
    values = img_arr[:, :, channel] 
    ax.hist(values.ravel(), bins=256, range=(0, 256), histtype="step", color=colors[channel], label=labels[channel])

ax.legend() 
fig.savefig("less_3/result/hist_rgb.png", dpi=150) 
plt.close(fig)

## Гистограмма после квантизации яркости
levels = 8

indices = np.rint(
    gray_arr.astype(np.float32) * (levels - 1) / 255
)
quantized_array = np.rint(
    indices * 255 / (levels - 1)
).astype(np.uint8)

values, counts = np.unique(quantized_array, return_counts=True)
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(values, counts, width=5)
ax.set_xticks(values)
ax.set_xlim(0, 255)
ax.set_xlabel("Значение яркости")
ax.set_ylabel("Число пикселей")
fig.savefig("less_3/result/hist_quantized.png", dpi=150)
plt.close(fig)
