#streamlit 
import streamlit as st

st.set_page_config(page_title= "Growth Mindset Project", project_icon="★")
st.title("Growth Mindset Challange: web App with Streamlit")

st.header("⏳ Welcome to Your Growth Journey!")
st.write("Embrace Challange, learn from mistakes, and unlock your full potential. This AI-powered ap helps you build a growth mindset with reflection, challanges, and achievement!🌞")


#quote section
st.header("💫 Today's Growth Mindset Quote")
st.write("〞Success is not, final, failure is not fatal: it is the courage to continue that counts.〝- winston churchhill")


st.header("🔧 What's your Challange Today?")
user_input = st.text_input("Describe a challange you're facing:")

#condition
if user_input:
    st.success(f"💪 You're facing: {user_input}. keep pushing forward towards your goal:📣")
else:
    st.warning("Tell us about your challange to get started!")
#reflection
    st.header("Reflect on your Learning")
    reflection = st.text_area("write your reflections here:")

    if reflection:
        st.success(f"✨ Great insight! Your reflection: {reflection}")
    else:
        st.info("Reflecting on past experience help you grow! Share your difficulties")


        #achievements
        st.header("👏 Celebrate Your Wins!")
        achievement = st.text_input("Share something you're recently accomplished:")


        if achievement:
            st.success(f"💯 Amazing! You achieved! {achievement}")
        else:
            st.info("Big or small , every achievement counts! Share one now 😍")


#footer
        st.write("- - -")
        st.write("👍 Keep believing in yourself. Growth is a journey, not a destination! 🌟")
        st.write("Ⓒ Created by Ghulam Nasir**")     