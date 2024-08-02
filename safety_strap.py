import os
import cv2
import numpy as np
import tensorflow as tf
import argparse


def load_model(model_path):
    """
    Load the trained TensorFlow model from the specified path.

    Parameters:
        model_path (str): Path to the trained model file.

    Returns:
        tf.keras.Model: Loaded TensorFlow model.
    """
    return tf.keras.models.load_model(model_path)


def preprocess_image(image_path):
    """
    Preprocess the image to prepare it for prediction.

    Parameters:
        image_path (str): Path to the image file.

    Returns:
        np.ndarray: Preprocessed image ready for prediction.
    """
    image = cv2.imread(image_path)  # Read the image from the given path
    image = cv2.resize(image, (224, 224))  # Resize the image to match the model's input size
    image = image / 255.0  # Normalize pixel values to [0, 1]
    image = np.expand_dims(image, axis=0)  # Add a batch dimension
    return image


def detect_seatbelt(model, image_path):
    """
    Use the model to detect if a seatbelt is present in the image.

    Parameters:
        model (tf.keras.Model): The trained TensorFlow model.
        image_path (str): Path to the image file.

    Returns:
        bool: True if the seatbelt is detected, False otherwise.
    """
    image = preprocess_image(image_path)  # Preprocess the image
    prediction = model.predict(image)  # Get the model's prediction
    return prediction[0][0] > 0.5  # Assume 0.5 as the threshold for seatbelt detection


def process_images(input_folder, output_folder, model_path):
    """
    Process all images in the input folder and save the results in the output folder.

    Parameters:
        input_folder (str): Path to the folder containing input images.
        output_folder (str): Path to the folder where results will be saved.
        model_path (str): Path to the trained model file.
    """
    model = load_model(model_path)  # Load the trained model
    results = []  # List to store the results

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):  # Check if the file is an image
            image_path = os.path.join(input_folder, filename)  # Get the full path of the image
            has_seatbelt = detect_seatbelt(model, image_path)  # Detect seatbelt in the image
            results.append((filename, has_seatbelt))  # Append the result to the list

    # Write the results to an output file
    output_file = os.path.join(output_folder, 'results.txt')
    with open(output_file, 'w') as f:
        for filename, has_seatbelt in results:
            f.write(f'{filename}: {"With Seatbelt" if has_seatbelt else "Without Seatbelt"}\n')


if __name__ == '__main__':
    # Argument parser for command-line options
    parser = argparse.ArgumentParser(description='Seatbelt Detection Application')
    parser.add_argument('--input_folder', required=True, help='Path to the input folder containing images')
    parser.add_argument('--output_folder', required=True, help='Path to the output folder for results')
    parser.add_argument('--model', default='models/default_model.h5', help='Path to the trained model')
    args = parser.parse_args()  # Parse the command-line arguments

    # Process the images and generate results
    process_images(args.input_folder, args.output_folder, args.model)
