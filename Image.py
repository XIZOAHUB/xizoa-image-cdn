from PIL import Image
import os

INPUT_DIR = "raw-img"
OUTPUT_DIR = "img"
MAX_WIDTH = 1600
QUALITY = 80

os.makedirs(OUTPUT_DIR, exist_ok=True)

for file in os.listdir(INPUT_DIR):
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        img = Image.open(os.path.join(INPUT_DIR, file))

        # resize
        if img.width > MAX_WIDTH:
            ratio = MAX_WIDTH / img.width
            img = img.resize((MAX_WIDTH, int(img.height * ratio)), Image.LANCZOS)

        name = os.path.splitext(file)[0]
        output_path = os.path.join(OUTPUT_DIR, f"{name}.webp")

        img.save(output_path, "WEBP", quality=QUALITY, method=6)

        print("optimized:", output_path)
