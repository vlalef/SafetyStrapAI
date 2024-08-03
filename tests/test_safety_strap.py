import os
from safety_strap import preprocess_image  # Import your function here

def test_preprocess_image():
    # Define input and output paths
    input_image = 'dataset/train/with_seatbelt/sample.jpg'
    output_image = 'dataset/train/with_seatbelt/sample_processed.jpg'
    
    # Call the preprocessing function
    preprocess_image(input_image, output_image)
    
    # Check if the output image file was created
    assert os.path.isfile(output_image), "Processed image was not created"
    
    # Additional checks can be added to verify image contents or format
