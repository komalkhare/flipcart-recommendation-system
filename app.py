import streamlit as st
import pandas as pd
import ast
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the data and model
data = pd.read_csv("flipkart_com-ecommerce_sample.csv")

# Load the cosine similarity matrix
cosine_sim = joblib.load('cosine_sim.joblib')

# Combine relevant columns for recommendation
data['product_category_tree'] = data['product_category_tree'].apply(lambda x: ' '.join(ast.literal_eval(x)) if isinstance(x, str) else '')
data['combined_features'] = data['product_name'].astype(str) + ' ' + \
                            data['description'].astype(str) + ' ' + \
                            data['product_category_tree'].astype(str)

# Fill missing values
data['combined_features'] = data['combined_features'].fillna('')

# Function to recommend products
def recommend_products(keyword, data, cosine_sim, top_n=5):
    matching_indices = data[data['combined_features'].str.contains(keyword, case=False, na=False)].index

    if len(matching_indices) == 0:
        return ["No products found for the given keyword."]
    
    idx = matching_indices[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get top N similar products
    top_indices = [i[0] for i in sim_scores[1:top_n+1]]
    return data.iloc[top_indices][['product_name', 'product_url']]

# Streamlit UI elements
st.title("Product Recommendation System")
st.write("Enter a keyword to search for similar products.")

# User input for keyword
keyword = st.text_input("Search for products:", "")

if keyword:
    st.write(f"Searching for products related to: **{keyword}**")
    recommendations = recommend_products(keyword, data, cosine_sim)

    if isinstance(recommendations, str):
        st.write(recommendations)
    else:
        st.write("Top Recommendations:")
        for i, row in recommendations.iterrows():
            st.write(f"**{row['product_name']}**")
            st.write(f"URL: {row['product_url']}")

else:
    st.write("Please enter a keyword to start the search.")
