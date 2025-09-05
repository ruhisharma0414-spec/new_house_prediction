# score.py
import os
import json
import joblib
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init():
    """Initialize the model and scaler when the container starts."""
    global model, scaler

    try:
        # Azure ML mounts model directory at this env variable
        model_dir = os.getenv("AZUREML_MODEL_DIR")

        # Paths to your artifacts
        scaler_path = os.path.join(model_dir, "model_assets", "scaler_model.pkl")
        model_path = os.path.join(model_dir, "model_assets", "Trained_model.pkl")

        logger.info(f"Loading scaler from: {scaler_path}")
        logger.info(f"Loading model from: {model_path}")

        # Load objects
        scaler = joblib.load(scaler_path)
        model = joblib.load(model_path)

        logger.info("Scaler and model loaded successfully.")
    except Exception as e:
        logger.error(f"Error during init: {str(e)}")
        raise

def run(raw_data):
    """Run a prediction request."""
    try:
        # Parse JSON
        data = json.loads(raw_data)
        inputs = data.get("data")

        if inputs is None:
            return {"error": "Input JSON must contain a 'data' key with a 2D array."}

        logger.info(f"Received input with shape: {np.array(inputs).shape}")

        # Scale inputs
        inputs_scaled = scaler.transform(inputs)

        # Predict
        predictions = model.predict(np.array(inputs_scaled))

        logger.info(f"Predictions: {predictions.tolist()}")

        return {"predictions": predictions.tolist()}
    except Exception as e:
        error_message = f"Error during run: {str(e)}"
        logger.error(error_message)
        return {"error": error_message}
