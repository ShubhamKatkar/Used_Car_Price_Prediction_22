import base64
import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("     Used Car Price Prediction")

from PIL import Image
image = Image.open('sk.jpeg')
st.image(image, caption='Don’t Only Dream it, Just Drive It')


#'year', 'manufacturer', 'condition', 'cylinders', 'fuel', 'odometer','transmission', 'drive', 'size', 'type', 'paint_color'

#build
year = st.selectbox('year',[1995,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021])

odometer = st.selectbox('odometer',[1000,5000,10000,20000,30000,40000,50000,100000,150000,200000,250000])




#Categorical

manufacturer = st.selectbox('Car Manufacturer',df['manufacturer'].unique())
condition = st.selectbox('Car Condition',df['condition'].unique())
cylinders = st.selectbox('Engine Cylinders',df['cylinders'].unique())
fuel = st.selectbox('Fuel Type',df['fuel'].unique())
transmission = st.selectbox('Transmission',df['transmission'].unique())
drive = st.selectbox('Drive',df['drive'].unique())
size = st.selectbox('Size',df['size'].unique())
type = st.selectbox('Type',df['type'].unique())
paint_color = st.selectbox('Car Color',df['paint_color'].unique())

if st.button('Predict Price'):
    # query
    query = np.array([year,manufacturer,condition,cylinders,fuel,odometer,transmission,drive,size,type,paint_color])

    query = query.reshape(1,11)
    #st.title("The predicted price of this configuration is " + str((np.exp(pipe.predict(query)[0]))))
    st.title("The Predicted Price of CAR is "+str(int(pipe.predict(query)[0]))+"$")
