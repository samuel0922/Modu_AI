
import streamlit as st
import numpy as np
import pandas as pd

#from st_aggrid import AgGrid

# import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('Agg')       #서버에서, 화면에 표시하기 위해서 필요
# import seaborn as sns
# import altair as alt               ##https://altair-viz.github.io/
# import plotly.express as px

st.write("Hello, Streamlit!")
st.write("------------------------------------------------------------------")
st.write("                      Project 1. CSV Plotting                     ")
st.write("------------------------------------------------------------------")
st.write("                 1. 파일업로드                                    ")
st.write("                 2. CSV → Pandas df                              ")
st.write("                 3. df ploitting                                  ")
st.write("                 4. multiselect → df[’col’] 컬럼명             ")
st.write("                 5. 선택된 컬럼만 표시                            ")
st.write("------------------------------------------------------------------")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
#      # To read file as bytes:
#      bytes_data = uploaded_file.getvalue()
#      st.write(bytes_data)

#      # To convert to a string based IO:
#      stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#      st.write(stringio)

#      # To read file as string:
#      string_data = stringio.read()
#      st.write(string_data)

     # Can be used wherever a "file-like" object is accepted:
    df_test = pd.read_csv(uploaded_file)
#    st.write(dataframe)

    AgGrid(df_test)


    df_columns = df_test.columns
    st.write(df_columns)

    options = st.multiselect(
         'What are your columns',
         df_columns)
    
    
    # 슬라이스
    
    from datetime import datetime

    start_time = st.slider(
         "When do you start?",
        value=datetime(2020, 1, 1, 9, 30),
        format="YYYY")
    st.write("Start time:", start_time)
    
    if st.button("View Data"):
        st.write("Data Loading..")
        
        #AgGrid(dataframe)
        st.write(df_test[options])

        import matplotlib.pyplot as plt
        import numpy as np

        df_chart = df_test[options]
        st.write("----")
        
        fig, ax = plt.subplots()
        ax.hist(df_chart)

        st.pyplot(fig)
# checkbox_btn = st.checkbox('Checktbox Button')

# if checkbox_btn:
#       st.write('Great!')
        
# checkbox_btn2 = st.checkbox('Checktbox Button2', value=True)

# if checkbox_btn2:
#       st.write('Button2')

# values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
# st.write('Values:', values)
