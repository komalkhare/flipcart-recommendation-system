# Product Recommendation System - Streamlit App

This repository contains a Streamlit application for a product recommendation system based on product features and cosine similarity. The app allows users to search for products by keyword and receive recommendations for similar products.

## Prerequisites

Before running the app, make sure you have the following:

- Python 3.x
- Required libraries (listed below)

## Installation

Follow these steps to set up and run the application:

1. **Clone the repository (if applicable)** or download the files:


2. **Install required libraries** using `pip`:

Create a virtual environment (optional but recommended):


Install the dependencies:


Or manually install the required libraries:


3. **Download the data file and saved model**:

- Ensure that you have the dataset file `flipkart_com-ecommerce_sample.csv` in the same directory as `app.py`.
- Ensure that the cosine similarity matrix `cosine_sim.joblib` is also present in the directory. This file can be generated from the model training phase of the recommendation system (as done in the original code).

## Running the App

To run the app, follow these steps:

1. Navigate to the directory containing `app.py` in the terminal.

2. Run the following command to start the Streamlit app:


3. The app should open automatically in your default web browser. If it doesn't, you can manually open `http://localhost:8501` in your browser.

## Using the App

- The app displays a search bar where users can enter a keyword.
- After entering a keyword, it returns a list of top recommended products based on the cosine similarity of their features (such as product name, description, and category).
- The recommendations include the product name and a clickable URL for more details.

## Code Explanation

### Backend Logic:
- **Data Preprocessing:** The dataset is preprocessed by combining relevant columns (product name, description, and category) into a new column (`combined_features`) that is used for similarity calculation.
- **TF-IDF Vectorization:** The combined features are vectorized using TF-IDF (Term Frequency-Inverse Document Frequency).
- **Cosine Similarity:** The cosine similarity between product features is calculated using the vectorized features.
- **Recommendation Function:** The app includes a function to recommend products based on a keyword search. It finds products that contain the keyword and then calculates their similarity to others using the precomputed cosine similarity matrix.

### Frontend (Streamlit):
- The app uses Streamlit to create an interactive user interface where the user can input keywords and view recommendations.
- Results are displayed as product names with URLs linking to more information.

## Files in the Repository

- **`app.py`**: The main Streamlit application file.
- **`flipkart_com-ecommerce_sample.csv`**: Sample product data file.
- **`cosine_sim.joblib`**: Precomputed cosine similarity matrix (saved model).

## Contributing

If you'd like to contribute to this project:

1. Fork the repository.
2. Make your changes and improvements.
3. Create a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
