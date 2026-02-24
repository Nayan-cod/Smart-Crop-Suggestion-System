# AgriAI Integrated System

A unified web application for **Smart Crop Suggestion** using machine learning.
Built entirely as a standalone **Streamlit** application.

---

## Features

1. **Smart Crop Suggestion:** Recommends the most suitable crop to plant based on soil nutrients (N, P, K), weather (temperature, humidity, rainfall), and pH level using a retrained Machine Learning Model (Gaussian Naive Bayes).

---

## Prerequisites

- **Python 3.8+**


## Installation & Setup

1. Open a terminal and navigate to the project directory:
   ```bash
   cd AgriAI_Integrated_System
   ```
2. Create and activate a Virtual Environment:
   **Windows:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Application:
   ```bash
   python -m streamlit run app.py
   ```

## Usage

1. Open your browser and navigate to `http://localhost:8501`.
2. Enter the necessary parameters based on your farm and click "Predict Recommended Crop".

## Architecture Modifications

- **Model Compatibility**: To solve unpickling conflicts between old versions of `scikit-learn`, the `SmartCrop` model was completely retrained with current dependency versions.
- **Standalone App**: Features are completely self-contained within Python without requiring complex REST API pipelines, using Streamlit for dynamic front-end rendering and direct scikit-learn calls.

Link: https://smart-crop-suggestion-system.streamlit.app/

