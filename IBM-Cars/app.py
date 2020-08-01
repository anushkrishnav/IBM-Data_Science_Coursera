import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
st.title('Data analytics with Python IBM')
@st.cache
def load_data():
    data=pd.read_csv('clean_df.csv')
    data['price'] = pd.to_numeric(data['price'].str.replace('?', ''))
    return data
data_load_state=st.text('Loading hold on..........It might take a couple of seconds')
data=load_data()
data_load_state.text('')
if st.checkbox('Show raw data'):
    st.header('raw data')
    st.write(data)
#----------------------------------------------------------------------------------
if st.checkbox('Show Meta data'):
    st.write(data.dtypes)
st.header('Correlation between variables')
st.write(data.corr())
#----------------------------------------------------------------------
st.header('Relationship between price and engine-size')
sns.regplot(x="engine-size", y="price", data=data)
plt.ylim(0,)
st.pyplot()
#----------------------------------------------------------------------------------

st.write('Positive Linear relationship')
st.header('correlation')
st.write(data[["engine-size", "price"]].corr())
st.header('Relationship between price and highway-mpg')
sns.regplot(x="highway-mpg", y="price", data=data)
st.pyplot()
#----------------------------------------------------------------------------------

st.header('correlation')
st.write(data[["highway-mpg", "price"]].corr())
st.write('As the highway milage per gallon goes up, the price goes down: this indicates an inverse/negative relationship between these two variables.')
#----------------------------------------------------------------------------------

st.header('Categorical variables')
st.subheader('Price and body-style(category)')
st.write('These are variables that describe a characteristic of a data unit, and are selected from a small group of categories.')
sns.boxenplot(x="engine-location", y="price", data=data)
st.pyplot()
st.write("Here we see that the distribution of price between these two engine-location categories, front and rear, are distinct enough to take engine-location as a potential good predictor of price.")
#---------------------------------------------------------------------------
st.subheader('Price and drive-wheels(category)')
st.write('These are variables that describe a characteristic of a data unit, and are selected from a small group of categories.')
sns.boxenplot(x="drive-wheels", y="price", data=data)
st.pyplot()
st.write("Here we see that the distribution of price between these two drive-wheels categories, front and rear, are distinct enough to take drive-wheels as a potential good predictor of price.")
st.header("Descriptive Statistical Analysis")
st.write(data.describe())
st.write(data.describe(include=['object']))