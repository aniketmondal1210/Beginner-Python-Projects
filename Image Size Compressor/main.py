from PIL import Image

def compress_image(image_path, output_path, quality=20):
    try:
        # Open the image
        image = Image.open(image_path)
        
        # Convert to RGB if the image is in RGBA mode
        if image.mode == 'RGBA':
            image = image.convert('RGB')
    
        # Compress the image
        image.save(output_path, "JPEG", quality=quality)
        print("Image compressed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

input_image = input("Enter the path of the image you want to compress: ")  # Example: "C:/Users/ASUS/Pictures/image.jpg"
output_image = input("Enter the path to save the compressed image: ")  # Example: "C:/Users/ASUS/Pictures/compressed_image.jpeg"

# Call the function
compress_image(input_image, output_image)
