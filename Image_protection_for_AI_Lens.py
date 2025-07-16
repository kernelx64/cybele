from PIL import Image

def strip_exif_data(image_path, output_path):
    try:
        img = Image.open(image_path)
        # Create a new image without EXIF data
        # 'data' argument ensures only pixel data is copied, not metadata
        new_img = Image.new(img.mode, img.size)
        new_img.putdata(list(img.getdata()))
        new_img.save(output_path)
        print(f"EXIF data stripped from {image_path} and saved to {output_path}")
    except Exception as e:
        print(f"Error stripping EXIF: {e}")

# Example Usage:
# strip_exif_data("cybele_private_photo.jpg", "cybele_private_photo_no_exif.jpg")

import numpy as np
from PIL import Image

def add_subtle_noise(image_path, output_path, noise_factor=0.01):
    try:
        img = Image.open(image_path).convert("RGB")
        img_array = np.array(img, dtype=np.float32)

        # Generate noise based on the image's dimensions
        noise = np.random.normal(0, 255 * noise_factor, img_array.shape).astype(np.float32)

        # Add noise and clip values to stay within 0-255
        noisy_img_array = img_array + noise
        noisy_img_array = np.clip(noisy_img_array, 0, 255)

        # Convert back to PIL Image and save
        noisy_img = Image.fromarray(noisy_img_array.astype(np.uint8))
        noisy_img.save(output_path)
        print(f"Subtle noise added to {image_path} and saved to {output_path}")
    except Exception as e:
        print(f"Error adding noise: {e}")

# Example Usage:
# add_subtle_noise("cybele_private_photo.jpg", "cybele_private_photo_noisy.jpg", noise_factor=0.005)

from PIL import Image

def quantize_colors(image_path, output_path, colors=64):
    try:
        img = Image.open(image_path).convert("RGB")
        # Reduce the number of colors
        quantized_img = img.quantize(colors=colors)
        quantized_img.save(output_path)
        print(f"Colors quantized for {image_path} and saved to {output_path}")
    except Exception as e:
        print(f"Error quantizing colors: {e}")

# Example Usage:
# quantize_colors("cybele_private_photo.jpg", "cybele_private_photo_quantized.jpg", colors=128)

import tensorflow as tf
import numpy as np
from PIL import Image
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

# Load a pre-trained model (e.g., ResNet50 for image classification)
model = ResNet50(weights='imagenet')

def generate_adversarial_example(image_path, output_path, epsilon=0.05):
    try:
        img = Image.open(image_path).resize((224, 224)) # ResNet50 input size
        img_array = np.expand_dims(np.array(img), axis=0) # Add batch dimension
        preprocessed_img = preprocess_input(img_array.astype(np.float32))

        # Convert to TensorFlow tensor
        image_tensor = tf.convert_to_tensor(preprocessed_img)

        with tf.GradientTape() as tape:
            tape.watch(image_tensor)
            prediction = model(image_tensor)
            # Find the true label index (for targeted attacks, specify desired target)
            # For untargeted, we want to maximize the loss of the original prediction
            true_label = tf.argmax(prediction[0])
            loss = tf.keras.losses.SparseCategoricalCrossentropy()(true_label, prediction[0])

        # Get the gradients of the loss with respect to the input image
        gradients = tape.gradient(loss, image_tensor)
        # Get the sign of the gradients
        signed_grad = tf.sign(gradients)

        # Create the adversarial image
        adversarial_image_tensor = image_tensor + epsilon * signed_grad
        adversarial_image_tensor = tf.clip_by_value(adversarial_image_tensor, -1, 1) # Clip to [-1, 1] for ResNet50 input

        # Convert back to uint8 image
        # Undo preprocessing for saving
        # ResNet's preprocess_input scales to [-1, 1], so we need to reverse it
        adversarial_image_array = (adversarial_image_tensor.numpy()[0] + 1) * 127.5
        adversarial_image_array = np.clip(adversarial_image_array, 0, 255).astype(np.uint8)

        # Save the adversarial image
        adv_img_pil = Image.fromarray(adversarial_image_array)
        adv_img_pil.save(output_path)

        print(f"Adversarial example generated for {image_path} and saved to {output_path}")

        # Optional: Verify the new prediction
        adv_preprocessed = preprocess_input(np.expand_dims(adversarial_image_array, axis=0).astype(np.float32))
        adv_prediction = model.predict(adv_preprocessed)
        print("Original prediction:", decode_predictions(prediction.numpy()))
        print("Adversarial prediction:", decode_predictions(adv_prediction))

    except Exception as e:
        print(f"Error generating adversarial example: {e}")

# Example Usage: (Requires a sample image, e.g., an image of a cat)
# make sure you have tensorflow installed: pip install tensorflow
# generate_adversarial_example("cat.jpg", "cat_adversarial.jpg", epsilon=0.01)

from PIL import Image
import random

def subtle_jitter(image_path, output_path, max_angle=0.5, max_shift=2):
    try:
        img = Image.open(image_path).convert("RGB")

        # Random rotation
        angle = random.uniform(-max_angle, max_angle)
        img_rotated = img.rotate(angle, resample=Image.BICUBIC, expand=False) # Keep same size

        # Random shift
        x_shift = random.randint(-max_shift, max_shift)
        y_shift = random.randint(-max_shift, max_shift)
        img_shifted = img_rotated.transform(
            img.size, Image.AFFINE, (1, 0, x_shift, 0, 1, y_shift)
        )

        img_shifted.save(output_path)
        print(f"Subtle jitter applied to {image_path} and saved to {output_path}")
    except Exception as e:
        print(f"Error applying jitter: {e}")

# Example Usage:
# subtle_jitter("cybele_private_photo.jpg", "cybele_private_photo_jittered.jpg")
