import subprocess
import os

def test_train_model():
    # Ensure the script completes without errors
    result = subprocess.run(['python', 'train_model.py'], capture_output=True, text=True)
    assert result.returncode == 0, f"Training script failed with error: {result.stderr}"

    # Check if the model was saved correctly
    assert os.path.isfile('models/model.h5'), "Model file was not created"

