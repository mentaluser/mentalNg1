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

## Overview

MentalNg is a Flask-based web application designed to aid in the diagnosis and understanding of mental health issues, specifically focusing on ADHD. By leveraging advanced machine learning models, such as XGBoost, LightGBM, and logistic regression, the application delivers insightful predictions based on user inputs through an intuitive web interface. Integrated with OpenAI's powerful API, MentalNg enhances its predictive capabilities, providing users with a seamless and informative experience.

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
## Create and Activate a Virtual Environment (Recommended)

- **For Unix/Linux systems:**
  - Run `python3 -m venv venv`
  - Activate the environment with `source venv/bin/activate`

- **For Windows:**
  - Create the environment with `python -m venv venv`
  - Activate it using `venv\Scripts\activate`

## Install Required Packages

- Install all dependencies listed in `requirements.txt` by running `pip install -r requirements.txt`.

## API Key Configuration

- Insert your OpenAI API key in the application's configuration. This can be done preferably as an environment variable or directly within `app.py`.

## Running the Application

- To start the MentalNg application, use the command `flask run`.
- Access the application by navigating to `http://localhost:5000` in your web browser.

## Usage

- **Homepage:** Start on the homepage, where navigation options for diagnosis or viewing the application's performance metrics are available.
- **Diagnosis Interface:** Fill out the form with the necessary details to receive a mental health condition prediction.
- **Prediction Results:** Diagnosis predictions and confidence levels are presented in a format that's easy to understand.

## Contributing

- Contributions are welcome! Please see `CONTRIBUTING.md` for guidelines on how to contribute effectively. Collaboration is encouraged to enhance MentalNg.

## License

- This project is licensed under the MIT License. Refer to the `LICENSE` file for more details.
