import streamlit as st
import time
import numpy as np



st.header("图标示例")

st.subheader("Data Analytics")
st.text("演示使用numpy数据生成动态图标")
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

st.markdown("""
- chapter 01
- chapter 02
- chapter 03

 Emojis: :+1: :sunglasses:

From: [Github](https://github.com)""")

st.json({
    "pagination": {
        "total": 100,
        "per_page": 20,
        "page": 1,
    },
    "items": [
        {
            "id": 1,
            "name": "admin",
            "email": "admin@test.com",
            "is_superuser": True
        }
    ]
})
# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")