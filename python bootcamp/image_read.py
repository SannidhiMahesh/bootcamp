from PIL import Image

# Reading an image file
def read_image(file_path):
    img = Image.open("D:\Downloads\moon background.jpg")
    return img

# Writing an image file
def write_image(img, file_path):
    img.save("D:\Downloads\moon background.jpg")

# Example usage
image_file_path = 'image.jpg'
img = read_image(image_file_path)
img.show()  # Display the image
write_image(img, 'output_image.jpg')
