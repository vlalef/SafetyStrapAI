from safety_strap import predict  # Import your prediction function
import numpy as np

def test_predict():
    # Define input data
    sample_data = np.random.rand(224, 224, 3)  # Example input data shape
    
    # Call the prediction function
    prediction = predict(sample_data)
    
    # Check if the prediction is within expected range
    assert prediction is not None, "Prediction returned None"
    assert len(prediction) == 2, "Prediction should have 2 classes"
