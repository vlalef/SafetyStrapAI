from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.optimizers import Adam


def prepare_data(train_directory, val_directory):
    """
    Prepare the data generators for training and validation datasets.

    Parameters:
        train_directory (str): Path to the training data directory.
        val_directory (str): Path to the validation data directory.

    Returns:
        train_gen, val_gen: Data generators for training and validation.
    """
    # Data augmentation and normalization for training
    train_datagen = ImageDataGenerator(
        rescale=1. / 255,  # Normalize pixel values
        shear_range=0.2,  # Shear transformations
        zoom_range=0.2,  # Zoom transformations
        horizontal_flip=True  # Random horizontal flips
    )

    # Only rescaling for validation data
    val_datagen = ImageDataGenerator(rescale=1. / 255)

    # Create the training data generator
    train_gen = train_datagen.flow_from_directory(
        train_directory,
        target_size=(224, 224),  # Resize images to 224x224
        batch_size=32,
        class_mode='binary'  # Binary classification
    )

    # Create the validation data generator
    val_gen = val_datagen.flow_from_directory(
        val_directory,
        target_size=(224, 224),  # Resize images to 224x224
        batch_size=32,
        class_mode='binary'  # Binary classification
    )

    return train_gen, val_gen


def build_model():
    """
    Build and compile the CNN model.

    Returns:
        model: Compiled CNN model.
    """
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),  # First convolutional layer
        MaxPooling2D(pool_size=(2, 2)),  # First pooling layer
        Conv2D(64, (3, 3), activation='relu'),  # Second convolutional layer
        MaxPooling2D(pool_size=(2, 2)),  # Second pooling layer
        Conv2D(128, (3, 3), activation='relu'),  # Third convolutional layer
        MaxPooling2D(pool_size=(2, 2)),  # Third pooling layer
        Flatten(),  # Flatten the feature map
        Dense(128, activation='relu'),  # Fully connected layer
        Dense(1, activation='sigmoid')  # Output layer for binary classification
    ])

    # Compile the model
    model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])
    return model


def train_model(train_gen, val_gen, save_model_path):
    """
    Train the CNN model using the training and validation data.

    Parameters:
        train_gen: Data generator for training data.
        val_gen: Data generator for validation data.
        save_model_path (str): Path to save the trained model.
    """
    model = build_model()  # Build the model

    # Train the model
    model.fit(
        train_gen,
        epochs=10,
        validation_data=val_gen
    )

    # Save the trained model
    model.save(save_model_path)


if __name__ == '__main__':
    # Define the paths to the training and validation data directories
    train_directory = 'dataset/train'
    val_directory = 'dataset/validation'
    model_save_path = 'models/seatbelt_detector.h5'  # Path to save the trained model

    # Prepare the data generators
    train_generator, val_generator = prepare_data(train_directory, val_directory)

    # Train and save the model
    train_model(train_generator, val_generator, model_save_path)
