# Milk Quality Prediction App

This is a web application built with Streamlit that predicts milk quality based on various parameters. The app uses a machine learning model trained with PyCaret to classify milk quality into three grades: High, Medium, and Low.

## Features

- Interactive web interface for input parameters
- Real-time prediction
- Support for 7 milk quality parameters:
  - pH level
  - Temperature
  - Taste
  - Odor
  - Fat content
  - Turbidity
  - Color

## Installation

1. Clone this repository
2. Create a virtual environment:
```bash
python -m venv venv
```
3. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate
```
4. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```
2. Enter the milk quality parameters in the input fields
3. Click "Predict Milk Quality" to see the prediction

## Required Parameters

| Parameter    | Range/Values | Description |
|-------------|--------------|-------------|
| pH          | 0-14        | pH level of milk |
| Temperature | Any positive | Temperature in Celsius |
| Taste       | 0 or 1      | Binary indicator for taste |
| Odor        | 0 or 1      | Binary indicator for odor |
| Fat         | 0 or 1      | Binary indicator for fat content |
| Turbidity   | 0 or 1      | Binary indicator for turbidity |
| Color       | Any positive | Color value |

## Dependencies

- Python 3.8+
- streamlit
- pandas
- pycaret

## Model

The application uses a pre-trained model (`best_milk_quality_model`) created using PyCaret's classification module.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
