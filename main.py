import streamlit as st
from PIL import Image
import os

st.set_page_config("Donate for a cause")
st.title("DONATE FOR A CAUSE")
st.subheader("The idea is not to live forever ...but maybe to help another live a little longer")
st.write("Welcome, The aim of our website is to provide a platform to people like you, who want to donate to help those who need medicines, oxygen cylinders or clothes etc.")
st.write("All you have to do is give us some information about the things you want to donate, your address, name, mail id etc and we will transfer your given information to the related NGO's and then they will contact you and collect it from you. ")

st.subheader("Priority Equipments")
st.write("1. **Oxygen Concentrators** of 10lpm capacity) with CE and ISO certifications and 220 V power system with Indian plug system. ")
st.write("2. **D-type Oxygen Cylinders** (40-47L capacity), preferably filled, along with regulator and humidifier so as to able to directly supply oxygen at desired flow to patients on low oxygen. ")
st.write("3. **Finger tip Pulse Oximeters** with Digital display, screen size 14*28 mm, battery operated, To Measure SpO2 level with accuracy level of 70 to 99 +- 2% and Pulse range between 25 to 250 BPM.")

st.image(".\images\Donate.jpeg")

with st.container():
  st.write("---")
  st.header("DONATE HERE")
  st.write("https://forms.gle/P9J1wwFXZZcHndUg6")
  st.write("##")
  st.write("Any help or donation, no matter how small, will be deeply appreciated and is much needed.")

  st.subheader("Donate medicines")
  image_column, text_column = st.columns((1,2))
  with text_column:
      st.write("By clicking on the link above, you can help those who need medicines but are not able to buy it, by donating all those medicines that are of no use to you and are not expired")
  with image_column:
      st.image(".\images\Med.jpg")

with st.container():
    st.write("##")
    st.write("\"We make a living by what we get, but we can make a life by what we give.\"")
    st.subheader("Donate medical equipment ")
    image_column, text_column = st.columns((1,2))
    with text_column:
        st.write("You can donate the medical equipment such as Finger tip Pulse oximeters, oxygen cylinders etc. ,that you have but are of no use to you. By doing this you may save a life of a person who doesn't have enough money to buy an oxygen cylinder or other much needed equipment for themselves")
    with image_column:
        st.image(".\images\Oxy.jpg")

with st.container():
    st.write("##")
    st.write("\"It's not how much we give, but how much love we put into giving.\"")
    st.subheader("Donate clothes ")
    image_column, text_column = st.columns((1,2))
    with text_column:
        st.write("There are many poor people on the streets that are wearing worn out clothes but dont have enough money to buy new clothes for themselves or their kids. You can donate your old clothes here which are of no use to you now but they must be in good condition inorder to help the poor")
    with image_column:
        st.image(".\images\Clothes.jpg")

with st.container():
    st.write("##")
    st.write("\"No one has ever become poor by giving.\"")
    st.subheader("Donate food ")
    image_column, text_column = st.columns((1,2))
    with text_column:
        st.write(" There are many poor people who sleep with an empty stomach everyday or die every month just because they didn't have enough money to buy food for themselves. You can donate any type of food here which has not expired yet.")
    with image_column:
        st.image(".\images\Food.jpg")

with st.container():
    st.write("##")
    st.write("\"Alone we can do so little, but together we can do so much.\"")
    st.subheader("Donate books ")
    image_column, text_column = st.columns((1,2))
    with text_column:
        st.write("You can donate any types of books here. They can be school books, college books, novels etc. Every book you donate here will be given to a child who needs it but don't have enough money to afford it  ")
    with image_column:
        st.image(".\images\Book.jpg")

st.write("##")
st.write("\"Never get tired of doing little things for others, sometimes those little things occupy the biggest parts of their hearts.\"")
st.subheader("Thank You!")
st.image(".\images\Ty.jpg")

st.write("##")
st.write("##")
st.subheader("About us")
st.write("We are just few Indians who are trying to help our fellow Indians who are not capable enough to help themselves.")

with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/kartikrocks019@gmail.com" method="POST">
      <input type="hidden" name="_captcha" value="false">
      <input type="text" name="name" placeholder="your name" required>
      <input type="email" name ="email" placeholder="Your email" required>
      <textarea name="message" placeholder="Your message here" required></textarea>
      <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns((2,1))
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


#streamlit run C:/Users/karti/PycharmProjects/hackathon/main.py
