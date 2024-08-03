
# SafetyStrapAI/README.md

### Index
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Configuration](#configuration)
6. [Example](#example)
7. [Dependencies](#dependencies)
8. [License](#license)
9. [Contact](#contact)

### Introduction
A Python-based tool designed to identify whether drivers in a set of images are wearing seat belts. <br> Given a folder containing images, the application processes each image and generates <br> a report indicating which drivers are wearing seat belts and which are not.
 
### Features
- Batch Processing: Processes multiple images in a single run.
- Accurate Detection: Utilizes advanced machine learning models to ensure high accuracy.
- Detailed Reports: Generates comprehensive reports of the results.
- User-Friendly: Simple command-line interface for easy interaction.

### Installation

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/vlalef/SafetyStrapAI.git
    cd SafetyStrapAI
    ```

2. **Create and Activate a Virtual Environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

4. **Install Dependencies:**
    Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```


### Usage

1. **Prepare your dataset:**
    Ensure that the images are organized into the appropriate directories under dataset/train and dataset/validation as it follows.
    ```
    dataset/ 
    ├── train/
    │   ├── with_seatbelt/
    │   │   ├── 1.jpg
    │   │   ├── 2.jpg
    │   │   ├── 3.jpg
    │   │   ├── 4.jpg
    │   │   ├── 5.jpg
    │   │   ├── 6.jpg
    │   │   ├── 7.jpg
    │   │   ├── 8.jpg
    │   │   ├── 9.jpg
    │   │   └── 10.jpg
    │   └── without_seatbelt/
    │       ├── 1.jpg
    │       ├── 2.jpg
    │       ├── 3.jpg
    │       ├── 4.jpg
    │       ├── 5.jpg
    │       ├── 6.jpg
    │       ├── 7.jpg
    │       ├── 8.jpg
    │       ├── 9.jpg
    │       └── 10.jpg
    └── validation/
        ├── with_seatbelt/
        │   ├── 1.jpg
        │   ├── 2.jpg
        │   ├── 3.jpg
        │   ├── 4.jpg
        │   └── 5.jpg
        └── without_seatbelt/
            ├── 1.jpg
            ├── 2.jpg
            ├── 3.jpg
            ├── 4.jpg
            └── 5.jpg
    ```
   

2. **Train the model:**

    ```
    sh
    python train_model.py
    ```

   This command will train the model using the images in the `train` directory and validate it using images from the `validation` directory.

4. **Run the application:**

   ```
   python safety_strap.py --input_folder path/to/your/images --output_folder path/to/save/results
   ```

6. **Review the Results:**

    The application will generate a report in the specified output folder detailing which images contain drivers using seat belts and which do not.

    **Example Report:**

    ```
    image1.jpg: Using seat belt
    image2.jpg: Not using seat belt
    image3.jpg: Using seat belt
    ```

### Configuration

The application can be configured via command-line arguments:

- `--input_folder`: Path to the directory containing the images.
- `--output_folder`: Path to the directory where results will be saved.
- `--model`: (Optional) Path to a custom model file if you wish to use a different model.

### Example:

```
sh
python SafetyStrapAI.py --input_folder ./images_input --output_folder ./results --model ./custom_model.pth
```

### Dependencies

- Python 3.9+
- OpenCV
- TensorFlow or PyTorch (depending on the model used)
- NumPy
- Other dependencies listed in requirements.txt

### License 
 This project is licensed under the GPL-3.0 license. Se the `LICENSE` file for more details

### Contact
- Author: Alef L. Vaz
- Email: Alef.Vaz.Contato@gmail.com
- GitHub: vlalef

[![LinkedIn][linkedin-shield]][linkedin-url]

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/alef-vaz
