import numpy as np
import pandas as pd
import joblib as jl
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='white', font_scale=5)

@st.cache
def load_data():
    return pd.read_csv('insurance_regression.csv')

insurance_df = load_data()

### Set title
st.title("Insurance Pricing App")
st.write("""From the data below, we built a machine learning-based pricing model to get quotation for each client based on their demographics.""")

### Set Sidebar Options
st.sidebar.title('About')
st.sidebar.info('Change parameters to see how insurance prices change.')
st.sidebar.title('Parameters')

# Age
age = st.sidebar.slider('Age', 0, 100, 24)

# BMI
bmi = st.sidebar.slider('BMI', 13, 40, 31)

# Number of Children
num_children = st.sidebar.slider('Number of Children', 0, 12, 1)

# Sex
sex = st.sidebar.radio('Sex', ('Female', 'Male'))

if sex == 'male':
    is_female = 0
else:
    is_female = 1

# is smoker
smoker = st.sidebar.radio('Smoker?', ('yes', 'no'))

if smoker == 'yes':
    is_smoker = 1
else:
    is_smoker = 0



