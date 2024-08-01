# SafetyStrapAI
### Introduction
A Python-based tool designed to identify whether drivers in a set of images are wearing seat belts. <br> Given a folder containing images, the application processes each image 1and generates <br> a report indicating which drivers are wearing seat belts and which are not.
 
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

3. **Install Dependencies:**
    Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

### Usage

1. **Prepare Your Images:**
   
   Ensure all images are in a directory, for example, `images_input/`.

2. **Run the Application:**

    ```sh
    python SafetyStrapAI.py --input_folder path/to/your/images --output_folder path/to/save/results
    ```

3. **Review the Results:**

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

### License 
 This project is licensed under the GPL-3.0 license. Se the `LICENSE` file for more details

**Example:**

```sh
python SafetyStrapAI.py --input_folder ./images_input --output_folder ./results --model ./custom_model.pth
```

[![LinkedIn][linkedin-shield]][linkedin-url]

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/alef-vaz
