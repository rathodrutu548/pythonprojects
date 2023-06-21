from PIL import Image, ImageFilter

def resize_image(image_path, output_path, width, height):
    image = Image.open(image_path)
    resized_image = image.resize((width, height))
    resized_image.save(output_path)

def crop_image(image_path, output_path, left, top, right, bottom):
    image = Image.open(image_path)
    cropped_image = image.crop((left, top, right, bottom))
    cropped_image.save(output_path)

def rotate_image(image_path, output_path, angle):
    image = Image.open(image_path)
    rotated_image = image.rotate(angle)
    rotated_image.save(output_path)

def apply_filter(image_path, output_path, filter_type):
    image = Image.open(image_path)
    filtered_image = image.filter(filter_type)
    filtered_image.save(output_path)

# Example usage:
resize_image('input.jpg', 'resized.jpg', 800, 600)
crop_image('input.jpg', 'cropped.jpg', 100, 100, 500, 400)
rotate_image('input.jpg', 'rotated.jpg', 90)
apply_filter('input.jpg', 'filtered.jpg', ImageFilter.BLUR)
