from altair import Datasets
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px 
from PIL import Image

st.set_page_config(page_title="Video game sales", page_icon=":tada:", layout="wide")

#Intro
with st.container():
    st.subheader("Welcome :wave:")
    st.title("BUSINESS IT 🌐")
    st.write("Our interactive web application project")
    
#Content
with st.container():
    st.write("---")
st.header("What we do")
st.write("##") 
st.write(
            """
            On our project, we are creating application for people who
            - interesting in video games
            - would like to learn about video games sale all around the world
            - want to learn about Data Analysis & Data Science 
            
            If this sounds interesting to you, consider contact me via my email: 10622020@student.vgu.edu.vn"""
        )
st.write("[Contact More >](https://www.facebook.com/profile.php?id=100006319325422)")

with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        # insert image
     with text_column:
        st.subheader("")

#import file excel(đang bị lỗi)+thanh filter
dataset = pd.read_excel('/Users/sunny/Desktop/Python Web/vgsales.xlsx' )
st.sidebar.header("Please Filter Here:")
Genre = st.sidebar.multiselect(
   "Select the Genre:",
   options=dataset["Genre"].unique(),
   default=dataset["Genre"].unique())

Platform = st.sidebar.multiselect(
   "Select the Platform:",
   options=dataset["Platform"].unique(),
   default=dataset["Platform"].unique())

df_selection = dataset.query(
   "Genre == @Genre & Platform == @Platform"
)

st.dataframe(df_selection)
 
#Bar chart
st.markdown("---")

Global_Sales_by_Genre=(df_selection.groupby(by=["Genre"]).sum()[["Global_Sales"]])

Global_Sales_by_Genre_barchart=px.bar(Global_Sales_by_Genre,
                                      x="Global_Sales",
                                      y=Global_Sales_by_Genre.index,
                                      title= "Global Sales By Genre",
                                      color_discrete_sequence=["#17f50c"],
                                      )
Global_Sales_by_Genre_barchart.update_layout(plot_bgcolor = "rgba(0,0,0,0)",xaxis=(dict(showgrid=False)))

#Pie chart
Global_Sales_by_Genre_piechart= px.pie(Global_Sales_by_Genre, names= Global_Sales_by_Genre.index,
                                       values="Global_Sales",
                                       title= "Global Sales Percent By Genre",
                                       hole=.3, 
                                       color=Global_Sales_by_Genre.index,
                                       color_discrete_sequence=px.colors.sequential.RdPu_r)

left_column,right_column=st.columns(2)
left_column.plotly_chart(Global_Sales_by_Genre_barchart,use_container_width=True)
right_column.plotly_chart(Global_Sales_by_Genre_piechart,use_container_width=True)

#Duy
tab1, tab2  = st.tabs([ "Category versus Global Sales", "Sales versus Publisher"])

with tab1:
    col1, col2 = st.columns([1,3])
    with col1:
        st.write("##")
        by_y = st.radio(
            "Choose a category:",
            ('Genre', 'Publisher', 'Platform', "Name" ),
            key = "r1")
    with col2:
        fig1 = px.scatter(dataset, x = "Global_Sales" , y = by_y,
                  labels={"Global_Sales": "Global Sales"},
                  size = "NA_Sales", 
                  marginal_x="histogram", marginal_y="histogram",
                  title = "Category versus Global Sales")
        st.plotly_chart(fig1, theme = "streamlit", use_container_width=True)

    fig1a = px.scatter(dataset, x= "Global_Sales", y= by_y, 
                         labels={"Global_Sales": "Global Sales"},
                       )
    st.plotly_chart(fig1a, theme = "streamlit", use_container_width=True)

with tab2:
    col1, col2 = st.columns([1,3])
    with col1:
        st.write("##")
        by_x = st.radio(
            "Choose a numeric:",
            ('NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'),
            key = "r2")
    with col2:
        fig2 = px.scatter(dataset, x = by_x , y = "Publisher",
                  labels={"Publisher": "Publisher"},
                  size = "NA_Sales", 
                  marginal_x="histogram", marginal_y="histogram",
                  title = "Sales versus Publisher")
        st.plotly_chart(fig2, theme = "streamlit", use_container_width=True)

    fig2a = px.scatter(dataset, x= by_x, y= "Publisher", 
                         labels={"Publisher": "Publisher"},
                       )
    st.plotly_chart(fig2a, theme = "streamlit", use_container_width=True)
#form điền
with st.container():
   st.write("---")
   st.header("Keep In Touch With Me!")
   st.write("##")

   contact_form = """
   <form action="https://formsubmit.co/10622020@student.vgu.edu.vn" method="POST">
     <input type="hidden" name="_capcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""

left_column, right_column = st.columns(2)
with left_column:
   st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
   st.empty()

def local_css(file_name):
   with open(file_name) as f:
      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("/Users/sunny/Desktop/Style/Style.txt") 