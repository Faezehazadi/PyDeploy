import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sidebar info
st.sidebar.title("📌 About this App")
st.sidebar.write("""
This is a **Simple Data Science App** built with **Streamlit**.
- Upload a CSV file
- View the data as a table
- Visualize it as a chart
""")

# Title
st.title("📊 Simple Data Science App")

# File Upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Convert to pandas dataframe
    df = pd.read_csv(uploaded_file)
    
    # Show dataframe
    st.subheader("🔍 Preview of your data")
    st.dataframe(df)
    
    # Show chart
    st.subheader("📈 Data Visualization")
    
    # Select numeric columns for chart
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    if len(numeric_columns) >= 2:
        x_axis = st.selectbox("Select X-axis", numeric_columns)
        y_axis = st.selectbox("Select Y-axis", numeric_columns)
        
        fig, ax = plt.subplots()
        ax.plot(df[x_axis], df[y_axis], marker='o')
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f"{y_axis} vs {x_axis}")
        
        st.pyplot(fig)
    else:
        st.warning("Please upload a dataset with at least two numeric columns.")
else:
    st.info("Please upload a CSV file to get started.")