import argparse
import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
import numpy as np


def load_model(model_path):
    """
    Load the trained model from the specified path.

    Parameters:
        model_path (str): Path to the trained model file.

    Returns:
        model: Loaded Keras model.
    """
    print(f"Loading model from {model_path}...")
    return tf.keras.models.load_model(model_path)


def process_images(input_folder, output_folder, model_path):
    """
    Process images to detect seatbelts using the trained model.

    Parameters:
        input_folder (str): Path to the input images folder.
        output_folder (str): Path to the output folder.
        model_path (str): Path to the trained model file.
    """
    model = load_model(model_path)  # Load the trained model

    # Create the output directory if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load and preprocess the images
    datagen = ImageDataGenerator(rescale=1. / 255)
    for subdir, _, files in os.walk(input_folder):
        for file in files:
            img_path = os.path.join(subdir, file)
            img = load_img(img_path, target_size=(224, 224))
            img_array = img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = datagen.standardize(img_array)

            # Predict using the model
            prediction = model.predict(img_array)

            # Save the result
            # Corrected logic
            result_text = 'with_seatbelt' if prediction[0] > 0.5 else 'without_seatbelt'
            output_file_path = os.path.join(output_folder, f"{file}_{result_text}.jpg")
            img.save(output_file_path)

            print(f"Saved result to {output_file_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process images for seatbelt detection.')
    parser.add_argument('--input_folder', type=str, required=True, help='Path to the input images folder.')
    parser.add_argument('--output_folder', type=str, required=True, help='Path to the output folder.')
    parser.add_argument('--model', type=str, required=True, help='Path to the trained model file.')

    args = parser.parse_args()
    process_images(args.input_folder, args.output_folder, args.model)
