# installed libraries
import plotly.express as px  # interactive charts
import numpy as np
import streamlit as st
# local files
import remote_data_mock as remote_data


st.set_page_config(
    page_title="Rice Bran Oil Dashboard",
    layout="wide",
)

st.title("Real-Time monitor of Rice Bran Factory")

data = remote_data.mock_data()
fig = None
# fig = px.line(data.df)
#
# st.plotly_chart(fig)
# empty container? idk what this is
placeholder = st.empty()

while True:
    data.get_data()

    with placeholder.container():  # or this

        if not fig:
            fig = px.line(data.df, x="Time", y="Ory")
        else:
            fig.data[0]['x'] = data.df.index
            fig.data[0]['y'] = data.df["Ory"]
        st.write(fig)
    print(data.df)
    print(type(fig))
    print(type(fig.data))
    print(fig.data)
    # st.dataframe(data.df)
    # st.plotly_chart(fig)
