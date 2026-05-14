from PIL import Image, ImageFilter
import os

output_dir = "filtered_images"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir("."):
    if not filename.endswith(".jpg"):
        continue

    img = Image.open(filename)
    filtered = img.filter(ImageFilter.CONTOUR)

    name, ext = os.path.splitext(filename)
    filtered.save(f"filtered_images/{name}_filtered{ext}")
    print(f"Обработан: {filename}")

print("Папка с отфильтрованными изображениями создана")
