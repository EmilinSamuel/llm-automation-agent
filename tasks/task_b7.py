from PIL import Image

def task_b7(image_path: str, output_path: str, size: tuple):
    img = Image.open(image_path)
    img = img.resize(size)
    img.save(output_path)