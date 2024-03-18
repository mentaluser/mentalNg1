# MentalNg

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.8-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0.1-blue.svg)

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

MentalNg is a Flask-based web application designed to aid in the diagnosis and understanding of mental health issues, specifically focusing on ADHD. By leveraging advanced machine learning models, such as XGBoost, LightGBM, and logistic regression, the application delivers insightful predictions based on user inputs through an intuitive web interface. Integrated with OpenAI's powerful API, MIS Predictor enhances its predictive capabilities, providing users with a seamless and informative experience.

## Features

- **Predictive Analysis:** Utilizes XGBoost, LightGBM, and logistic regression models for accurate mental health diagnosis.
- **OpenAI API Integration:** Employs OpenAI's API for enhanced analytical precision.
- **User-Friendly Interface:** Easy-to-navigate web interface for both data input and interpretation of results.
- **Multi-Model Aggregation:** Combines predictions from multiple models for more reliable outcomes.

## Installation

Ensure you have Python 3.8+ installed on your machine. Then, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://your-repository-url.git
   cd your-repository-directory
Create and Activate a Virtual Environment (Recommended)

For Unix/Linux systems:
python3 -m venv venv
source venv/bin/activate
For Windows:
python -m venv venv
venv\Scripts\activate
Install Required Packages

Install all dependencies listed in requirements.txt:
pip install -r requirements.txt
API Key Configuration

Insert your OpenAI API key in the application's configuration, preferably as an environment variable or directly within app.py.
Running the Application
To start the MentalNg application, execute the following command:
flask run
Navigate to http://localhost:5000 in your web browser to access the application and explore its functionalities.

Usage
Homepage: Begin by visiting the homepage, where you'll find navigation options for diagnosis or to view the application's performance metrics.
Diagnosis Interface: Complete the form with the required details to receive a mental health condition prediction.
Prediction Results: View the diagnosis prediction and confidence levels, presented in an easily understandable format.
Contributing
Your contributions are welcome! Please refer to CONTRIBUTING.md for guidelines on how to contribute effectively. Let's collaborate to enhance MentalNg.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
