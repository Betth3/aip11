from PIL import Image
import os

folder = "."

allowed = (".jpg", ".jpeg", ".png")

for filename in os.listdir(folder):
    if not filename.endswith(allowed):
        print(f"Пропускаем файл (не картинка): {filename}")
        continue

    img = Image.open(filename)

    print(f"--- Файл: {filename} ---")
    print(f"Размер: {img.size}")
    print(f"Формат: {img.format}")
    print(f"Цветовая модель: {img.mode}")
    print()
