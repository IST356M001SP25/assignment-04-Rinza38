'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal Data Browser")

# File uploader with explicit error feedback
file = st.file_uploader("Upload a file:", type=["csv", "xlsx", "json"])
if file:
    try:
        file_type = pl.get_file_extension(file.name)
        if not file_type:
            st.error("Uploaded file has no extension!")
            st.stop()
        
        df = pl.load_file(file, file_type)
        cols = pl.get_column_names(df)
        selected_cols = st.multiselect("Select columns to display", cols, default=cols)
        
        if not selected_cols:
            st.warning("No columns selected. Showing all.")
            selected_cols = cols
        
        df_show = df[selected_cols]
        
        if st.toggle("Filter data"):
            stcols = st.columns(3)
            text_cols = pl.get_columns_of_type(df, 'object')
            if text_cols:
                filter_col = stcols[0].selectbox("Select column to filter", text_cols)
                vals = pl.get_unique_values(df, filter_col)
                val = stcols[1].selectbox("Select value to filter on", vals)
                df_show = df[df[filter_col] == val][selected_cols]
            else:
                st.warning("No text columns available for filtering.")
        
        st.dataframe(df_show)
        st.dataframe(df_show.describe())
    
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")