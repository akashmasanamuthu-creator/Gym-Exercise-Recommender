import streamlit as st
import pickle
import pandas as pd


with open('gym_recommender_model.pkl', 'rb') as f:
    package = pickle.load(f)

model   = package['model']
le_dict = package['le_dict']
df      = package['df']


st.set_page_config(page_title="Gym Exercise Recommender", page_icon="🏋️")

st.title("🏋️ Gym Exercise Recommender")
st.write("Fill in your preferences and get personalized exercise recommendations!")


col1, col2 = st.columns(2)

with col1:
    workout_type = st.selectbox("💪 Workout Type", sorted(df['Type'].unique()))
    body_part    = st.selectbox("🎯 Body Part",    sorted(df['BodyPart'].unique()))

with col2:
    equipment = st.selectbox("🏠 Equipment", sorted(df['Equipment'].unique()))
    level     = st.selectbox("📊 Level",     sorted(df['Level'].unique()))


if st.button("🔍 Get Recommendations"):

    user_input = {
        'Type_encoded':      le_dict['Type'].transform([workout_type])[0],
        'BodyPart_encoded':  le_dict['BodyPart'].transform([body_part])[0],
        'Equipment_encoded': le_dict['Equipment'].transform([equipment])[0],
        'Level_encoded':     le_dict['Level'].transform([level])[0]
    }

    user_df = pd.DataFrame([user_input])
    distances, indices = model.kneighbors(user_df)
    results = df.iloc[indices[0][1:]][['Title', 'BodyPart', 'Equipment', 'Level', 'Desc']]
    results = results.reset_index(drop=True)

    st.success("Here are your recommended exercises! 💪")

    for i, row in results.iterrows():
        with st.expander(f"Exercise {i+1}: {row['Title']}"):
            st.write(f"**Body Part:** {row['BodyPart']}")
            st.write(f"**Equipment:** {row['Equipment']}")
            st.write(f"**Level:** {row['Level']}")
            st.write(f"**Description:** {row['Desc']}")