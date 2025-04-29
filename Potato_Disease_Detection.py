import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import io
#command for run
#streamlit run c:/Users/DELL/Downloads/python/Potato_leaf_Diesase_detection.py
#python -m streamlit run c:/Users/DELL/Downloads/python/Potato_leaf_Diesase_detection.py
#st.markdown("<h1 style='text-align: center; color: blue;'>Potatp Disease Detection System</h1>", unsafe_allow_html=True)
st.set_page_config(page_title="Potato Disease Detection", layout="wide")

# Add background image
import base64

def set_bg_image(local_image_path):
    with open(local_image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("data:image/jpg;base64,{encoded_image}") no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_image("pexels-kelly-1179532-2453551.jpg")  # Ensure this file exists in the correct path

#st.markdown("<h1 style='color: blue;'>Potato Disease Detection System</h1>", unsafe_allow_html=True)


# Function for Footer
def add_footer():
    st.markdown("""
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 5px;
            font-size: 14px;
            color: black;
        }
        </style>
        <div class="footer">
            <p>© 2025 Potato Disease Detection System | Developed by our team</p>
        </div>
    """, unsafe_allow_html=True)


# Apply Custom CSS for Sidebar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #2E8B57; /* Green background */
        color: white;
        padding: 20px;
    }
    
    [data-testid="stSidebarNav"] {
        font-size: 18px;
        font-weight: bold;
        color: white;
    }

    .css-1d391kg {  /* Sidebar title */
        color: white !important; 
        font-size: 24px !important;
        font-weight: bold !important;
    }

    /* Style for Selectbox */
    .stSelectbox div[data-baseweb="select"] {
        background-color: white !important;
        color: black !important;
        border: 2px solid #ffffff !important; /* White border */
        font-weight: bold !important;
    }

    /* Highlight Selected Option */
    .stSelectbox div[data-baseweb="selected"] {
        background-color: #ffffff !important;
        color: #2E8B57 !important; /* Green text */
        font-weight: bold !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Content
st.sidebar.title("🌿 Dashboard")  # Add emoji for better look
app_mode = st.sidebar.selectbox("📌 Select Page", ["About", "Home", "ChatBox", "Disease Recognition"])


#Home Page:
if app_mode == "Home":
    # Stylish header with white text and center alignment
    st.markdown("<h1 style='text-align: center; color: white;'>🥔 Potato Leaf Disease Recognition System 🌿</h1>", unsafe_allow_html=True)

    # Add a horizontal line for better UI
    st.markdown("<hr style='border: 1px solid white;'>", unsafe_allow_html=True)

    # Add an image banner (Change the URL to any image you like)
    #st.image("https://www.agrifarming.in/wp-content/uploads/2021/04/Potato-Plant.jpg", use_container_width=True)

    # Add white text inside a dark box for contrast
    st.markdown("""
    <div style='background-color: #222; padding: 15px; border-radius: 10px; color: white;'>
    <h3>🌱 Welcome to the Future of Plant Health Monitoring!</h3>
    <p>Our mission is to help in identifying <b>Potato diseases</b> efficiently. Upload an image and our system will analyze it to detect any signs of diseases.</p>
    
    <h4>🚀 How It Works</h4>
    <ol>
        <li><b>Upload Image:</b> Go to the <b>Disease Recognition</b> page and upload an image.</li>
        <li><b>Analysis:</b> Our AI-powered system will analyze the image to detect potential diseases.</li>
        <li><b>Results:</b> View the predictions and recommendations for treatment.</li>
    </ol>

    <h4>💡 Why Choose Us?</h4>
    <ul>
        <li>🔍 <b>Accuracy:</b> State-of-the-art machine learning techniques.</li>
        <li>🎨 <b>User-Friendly:</b> Simple and intuitive interface.</li>
        <li>⚡ <b>Fast and Efficient:</b> Get results within seconds.</li>
    </ul>

    <h4>➡️ Get Started</h4>
    <p>Click on the <b>Disease Recognition</b> page in the sidebar to upload an image and experience the power of our AI-driven Potato Disease Recognition System.</p>

    <h4>📢 About Us</h4>
    <p>Learn more about the project, our team, and our goals on the <b>About</b> page.</p>
    </div>
    """, unsafe_allow_html=True)

#About Project
elif app_mode == "About":
    # Header with styling
    st.markdown("<h1 style='text-align: center; color: white;'>About the Dataset</h1>", unsafe_allow_html=True)

    # Stylish divider
    st.markdown("<hr style='border: 1px solid white;'>", unsafe_allow_html=True)

    # Background box with white text for better visibility
    st.markdown("""
    <div style="background-color: #222; padding: 15px; border-radius: 10px; color: white;">
    
    <h3 style="color: #FFD700;">📂 Dataset Overview</h3>
    <p>This dataset is <b>recreated using offline augmentation</b> from the original dataset.  
    The original dataset can be found on this <a href="https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset" style="color: #00FF00;">Kaggle</a>.</p>

    <h4 style="color: #FFA500;">📊 Dataset Composition</h4>
    <p>It consists of approximately <span style="color: cyan;"><b>87,000 RGB images</b></span> of both <b>healthy</b> and <b>diseased</b> crop leaves.</p>
    <p>The dataset is categorized into <span style="color: lime;"><b>3 different classes</b></span>, ensuring a structured distribution.</p>

    <h4 style="color: #FF6347;">📁 Data Split</h4>
    <ul>
        <li>📌 <b>Training Set:</b> <span style="color: yellow;">910 images</span></li>
        <li>📌 <b>Test Set:</b> <span style="color: yellow;">300 images</span></li>
        <li>📌 <b>Validation Set:</b> <span style="color: yellow;">300 images</span></li>
    </ul>

    <h4 style="color: #1E90FF;">🔬 Purpose of Dataset</h4>
    <p>A new directory containing <span style="color: #FF69B4;"><b>33 test images</b></span> has been created later for prediction purposes.</p>

    </div>
    """, unsafe_allow_html=True)


#Prediction Page
elif app_mode == "Disease Recognition":
    st.markdown("<h1 style='text-align: center; color: white;'>Capture or Upload Image for Disease Recognition</h1>", unsafe_allow_html=True)
    #st.header("📷 Capture or Upload Image for Disease Recognition")

    # Camera Input for Capturing Image
    captured_image = st.camera_input("")

    # File Uploader for Uploading an Image
    uploaded_image = st.file_uploader("Or Upload an Image:", type=["jpg", "jpeg", "png"])

    image_to_process = None

    if captured_image:
        image_to_process = Image.open(captured_image)
    elif uploaded_image:
        image_to_process = Image.open(uploaded_image)

    if image_to_process:
        st.image(image_to_process, caption="Selected Image", use_container_width=True)
        
        image_to_process = image_to_process.resize((128, 128))
        image_array = tf.keras.preprocessing.image.img_to_array(image_to_process)
        image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

        # Predict when the "Diagnose" button is clicked
        if st.button("Predict"):
            st.snow()
            model = tf.keras.models.load_model("My_model.keras")  # Load model
            predictions = model.predict(image_array)
            confidence = np.max(predictions) * 100  # Convert to percentage
            result_index = np.argmax(predictions)

            class_name = ['Potato_Early___blight', 'Potato_Late___blight', 'Potato___healthy']
            predicted_class = class_name[result_index]

            # Display Result with Confidence Score
            st.markdown(f"""
                <div style='background-color:#4CAF50; padding:10px; border-radius:10px; color:white; font-size:20px; text-align:center;'>
                ✅ Model predicts: <b>{predicted_class}</b> <br> 
                🎯 Confidence: <b>{confidence:.2f}%</b>
                </div>""", unsafe_allow_html=True)

    else:
        st.markdown(f"""
                    <div style='background-color:white; padding:10px; border-radius:8px; color:red; font-size:17px;'>Please upload an image or capture one using the camera.</div>""",unsafe_allow_html=True)



#ChatBot
elif(app_mode=="ChatBox"):
    st.markdown("<h1 style='text-align: center; color: white;'>ChatBot</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>Hello! I am your AI chatbot. How can I help you today?</h3>", unsafe_allow_html=True)
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    
    def chatbot_response(user_input):
        responses = {
             "hello": "Hi there! How can I assist you?",
             "how are you": "I'm just a bot, but I'm functioning perfectly!",
             "bye": "Goodbye! Have a great day!",
             "good moring" : "Good Moring!",
             "good night" : "Good Night!",
             "good evening" : "Good Evening!",
             "name":["i am a chatbot, i dont have name!", "call me chatbot!", "i am just your chatbot!"],
             "early blight" :"Treatment: Use fungicides like Chlorothalonil, maintain proper spacing, and avoid overhead watering.",
             "soltion of early blight" :"Treatment: Use fungicides like Chlorothalonil, maintain proper spacing, and avoid overhead watering.",
             "give soltion of early blight" :"Treatment: Use fungicides like Chlorothalonil, maintain proper spacing, and avoid overhead watering.",
             "give answer of early blight" :"Treatment: Use fungicides like Chlorothalonil, maintain proper spacing, and avoid overhead watering.",
             "late blight" :"Treatment: Apply fungicides like Mancozeb, remove infected plants, and ensure good air circulation.",
             "solution of late blight" :"Treatment: Apply fungicides like Mancozeb, remove infected plants, and ensure good air circulation.",
             "give solution of late blight" :"Treatment: Apply fungicides like Mancozeb, remove infected plants, and ensure good air circulation.",
             "give answer of late blight" :"Treatment: Apply fungicides like Mancozeb, remove infected plants, and ensure good air circulation.",
             "i have question" : "Please, ask me",
             "what is late blight also called?":"Phytophthora infestans is an oomycete or water mold, a fungus-like microorganism that causes the serious potato and tomato disease known as late blight or potato blight.",
             "what fungicide is used for late blight of potatoes?": "If there is some sign of blight and the potatoes are not mature, use Dithane (mancozeb) MZ or you can also use Tattoo C or Acrobat MZ. Acrobat used later in the season reduces late blight spores. Use just before topkilling if there is blight in the crop.",
             "what temperature is early blight?": "Life cycle and appearance of Early blight Sporulation of Alternaria occurs at temperatures from 2-4 °C up to 28-30 °C (optimum temperatures lie between 15 and 28 °C) and at a relative humidity (RH) of over 90% or when the leaves are wet.",
             "what is the scientific Name for blight disease?":"Scientific Name. Phytophthora infestans (Montagne) Bary ( ITIS ) Late blight (LB), late blight disease, potato late blight, tomato late blight. Synonym. Peronospora infestans Montagne ( ITIS )",
             "what is the best treatment for late blight?":"Preventative fungicide sprays may be applied if late blight is present in your neighbourhood. Remove plants that show symptoms of the disease. Infected plants should be dug up, destroyed and disposed of properly to prevent the disease from spreading.",
             "is late blight caused by bacteria?":"Potato late blight is an extremely serious plant disease caused by the pathogen Phytophthora infestans. It's an oomycete, which are often described as 'water moulds' and are closely related to algae, not fungi as originally thought.",
             "what crop is affected by blight disease?":"This is the worst fungal disease which attacks the potato crop. It can seriously reduce yield by killing the foliage early; during periods of heavy rain the spores of the fungus can be washed into the soil and onto the tubers, so causing them to rot in the ground or during storage.",
             "Can blight affect humans?":"Blighted areas are associated with lead poisoning, public safety risks, and health issues. Neighborhood blight has been found to be a solid predictor of increased high risk sexual behavior, crime, drug use, and premature mortality due to malignant neoplasm's, diabetes, homicide, and suicide",
             "What is blight damage?" : "is a damage over time status effect similar to bleed. Heroes and enemies affected by blight will take health damage equal to the strength of the blight at the start of their turn. Most blights in the game last for 3 turns, or 5 turns if applied with a critical hit.",
             "What is called blight?" : "Blight is a rapid and complete chlorosis, browning, then death of plant tissues such as leaves, branches, twigs, or floral organs. Accordingly, many diseases that primarily exhibit this symptom are called blights",
             "Why is plant health important?": "Healthy plants provide safe and nutritious food for billions of people around the world, yet plant pests damage almost 40 percent of global crops. The most vulnerable populations suffer the most, particularly those already facing food insecurity from the impact of climate change, conflict or natural disasters.",

        }
        for key in responses:
            if key in user_input.lower():
             return responses[key]
        return "I'm not sure about that. Can you rephrase?"
    user_input = st.text_input("You:", "")

    if st.button("Send") and user_input:
        bot_response = chatbot_response(user_input)
        # Store messages in session state
        st.session_state["messages"].append(("You", user_input))
        st.session_state["messages"].append(("Bot", bot_response))
    
    
    
    # Display chat history
    for sender, msg in st.session_state["messages"]:
        if sender == "You":
            st.markdown(f"<div style='background-color: #0078FF; color: white; padding: 8px; border-radius: 10px; margin: 5px 0; width: fit-content;'><b>You:</b> {msg}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='background-color: #28A745; color: white; padding: 8px; border-radius: 10px; margin: 5px 0; width: fit-content;'><b>Bot:</b> {msg}</div>", unsafe_allow_html=True)
add_footer()
#streamlit run c:\Users\LENOVO\Downloads\Potato_Disease_Detection.py