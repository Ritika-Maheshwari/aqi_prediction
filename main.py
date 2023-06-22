import streamlit as st
from PIL import Image
import pickle
import pandas as pd

model = pickle.load(open('model.pkl', 'rb'))


def run():
    img1 = Image.open('aqi.jpeg')
    # img1 = img1.resize((156,145))
    st.image(img1, use_column_width=False)
    st.title("AQI Prediction")

    # T value
    T = st.number_input('T Value', 7.4)

    # TM value
    TM = st.number_input('TM Value', 9.8)

    # Tm value
    Tm = st.number_input('Tm Value', 4.8)

    # SLP value
    SLP = st.number_input('SLP Value', 1017)

    # H value
    H = st.number_input('H Value', 93)

    # VV Value
    VV = st.number_input('VV Value', 0.5)

    # V value
    V = st.number_input('V Value', 4.3)

    # VM value
    VM = st.number_input('VM Value', 9.4)

    if st.button("Submit"):
        # features = [[T, TM, Tm, SLP, H, VV, V, VM]]
        # features = [[float(i) for i in features[0]]]
        df = pd.DataFrame({'T': [T], 'TM': [TM], 'Tm': [Tm], 'SLP': [SLP], 'H': [H], 'VV': [VV], 'V': [V], 'VM': [VM]})
        print('---------------')
        print(df)
        prediction = model.predict(df)
        lc = [str(i) for i in prediction]
        ans = "".join(lc)
        if ans == 0:
            st.error(
                'Error'
            )
        else:
            st.success(
                f"AQI Prediction: {ans}"
            )


run()
