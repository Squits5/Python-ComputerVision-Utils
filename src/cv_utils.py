import cv2
import numpy as np
from PIL import Image
import os

def load_image(image_path, color_mode='rgb'):
    """Loads an image from the specified path."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    if color_mode == 'rgb':
        img = Image.open(image_path).convert('RGB')
    elif color_mode == 'grayscale':
        img = Image.open(image_path).convert('L')
    else:
        raise ValueError("color_mode must be 'rgb' or 'grayscale'")
    return np.array(img)

def save_image(image_array, output_path):
    """Saves an image to the specified path."""
    img = Image.fromarray(image_array.astype(np.uint8))
    img.save(output_path)
    print(f"Image saved to {output_path}")

def resize_image(image_array, size=(128, 128)):
    """Resizes an image to the given size."""
    return cv2.resize(image_array, size, interpolation=cv2.INTER_AREA)

def rotate_image(image_array, angle):
    """Rotates an image by the given angle."""
    h, w = image_array.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image_array, M, (w, h))

def apply_gaussian_blur(image_array, kernel_size=(5, 5)):
    """Applies Gaussian blur to an image."""
    return cv2.GaussianBlur(image_array, kernel_size, 0)

def convert_to_grayscale(image_array):
    """Converts an RGB image to grayscale."""
    if len(image_array.shape) == 3 and image_array.shape[2] == 3:
        return cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
    return image_array # Already grayscale or not RGB

def edge_detection(image_array, low_threshold=100, high_threshold=200):
    """Performs Canny edge detection on an image."""
    gray_image = convert_to_grayscale(image_array)
    return cv2.Canny(gray_image, low_threshold, high_threshold)

# Example usage (requires a dummy image for testing)
if __name__ == "__main__":
    # Create a dummy image for testing
    dummy_image_path = "dummy_image.png"
    dummy_image = np.zeros((200, 200, 3), dtype=np.uint8)
    cv2.circle(dummy_image, (100, 100), 50, (255, 0, 0), -1) # Blue circle
    cv2.rectangle(dummy_image, (20, 20), (80, 80), (0, 255, 0), -1) # Green square
    save_image(dummy_image, dummy_image_path)
    print(f"Created dummy image at {dummy_image_path}")

    try:
        # Load image
        img = load_image(dummy_image_path)
        print(f"Original image shape: {img.shape}")

        # Resize image
        resized_img = resize_image(img, (64, 64))
        print(f"Resized image shape: {resized_img.shape}")
        save_image(resized_img, "resized_dummy_image.png")

        # Rotate image
        rotated_img = rotate_image(img, 45)
        save_image(rotated_img, "rotated_dummy_image.png")

        # Apply Gaussian blur
        blurred_img = apply_gaussian_blur(img)
        save_image(blurred_img, "blurred_dummy_image.png")

        # Convert to grayscale and perform edge detection
        edges_img = edge_detection(img)
        save_image(edges_img, "edges_dummy_image.png")

        print("All operations completed and results saved.")

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up dummy image
        if os.path.exists(dummy_image_path):
            os.remove(dummy_image_path)
            print(f"Cleaned up {dummy_image_path}")
