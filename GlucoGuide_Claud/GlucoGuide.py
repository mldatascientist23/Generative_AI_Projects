import streamlit as st
import anthropic

# Initialize API key from secrets
api_key = st.secrets["claude_api_key"]

# Function to call Claude AI API and get a personalized meal plan
def get_meal_plan(api_key, fasting_sugar, pre_meal_sugar, post_meal_sugar, dietary_preferences):
    client = anthropic.Anthropic(api_key=api_key)
    
    prompt = (
        f"My fasting sugar level is {fasting_sugar} mg/dL, "
        f"my pre-meal sugar level is {pre_meal_sugar} mg/dL, "
        f"and my post-meal sugar level is {post_meal_sugar} mg/dL. "
        f"My dietary preferences are {dietary_preferences}. "
        "Please provide a personalized meal plan that can help me manage my blood sugar levels effectively."
    )
    
    # Call Claude AI API
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=250,
        temperature=0.7,
        system="You are a world-class nutritionist who specializes in diabetes management.",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    raw_context = message.content
    itinerary = raw_context[0].text
    return itinerary

# Apply custom CSS for a polished dashboard look
st.markdown(
    """
    <style>
    .header {
        text-align: center;
        margin-bottom: 20px;
    }
    .header .creator {
        font-size: 1.2rem;
        color: #888888;
        margin-bottom: 5px;
    }
    .header .creator a {
        color: #4CAF50;
        text-decoration: none;
    }
    .header .creator a:hover {
        text-decoration: underline;
    }
    .main-title {
        text-align: center; 
        color: #4CAF50;
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .sub-title {
        text-align: center; 
        color: #666666;
        font-size: 1.25rem;
        margin-bottom: 2rem;
    }
    .sidebar-title {
        color: #4CAF50;
        font-size: 1.5rem;
    }
    .generate-button {
        background-color: #4CAF50;
        color: white;
        font-size: 1.25rem;
        padding: 0.75rem;
        text-align: center;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        width: 100%;
        margin-top: 1rem;
    }
    .generate-button:hover {
        background-color: #45A049;
    }
    .meal-plan {
        background-color: #F0F8FF;
        padding: 1.5rem;
        border-radius: 8px;
        margin-top: 1.5rem;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        font-size: 1rem;
        color: #888888;
    }
    .footer a {
        color: #4CAF50;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True
)

# Header with creator's name and LinkedIn profile
st.markdown(
    """
    <div class="header">
        <p class="creator">Created by <strong>Engr. Hamesh Raj</strong></p>
        <p class="creator"><a href="https://www.linkedin.com/in/datascientisthameshraj/" target="_blank">Connect with me on LinkedIn</a></p>
    </div>
    """, unsafe_allow_html=True
)

# Streamlit app title with emojis
st.markdown(
    """
    <h1 class="main-title">
    🍽️ GlucoGuide: Your Personalized Diabetes Meal Planner 🍽️
    </h1>
    """, unsafe_allow_html=True
)

st.markdown(
    """
    <p class="sub-title">
    **GlucoGuide** is a personalized meal planning tool designed specifically for diabetic patients. 
    By entering your sugar levels and dietary preferences, GlucoGuide generates meal plans that are 
    tailored to help you manage your blood sugar levels effectively.
    </p>
    """, unsafe_allow_html=True
)

# Sidebar inputs for sugar levels and dietary preferences
st.sidebar.markdown("<h2 class='sidebar-title'>Enter Your Details</h2>", unsafe_allow_html=True)

fasting_sugar = st.sidebar.number_input("Fasting Sugar Levels (mg/dL)", min_value=0, max_value=500, step=1)
pre_meal_sugar = st.sidebar.number_input("Pre-Meal Sugar Levels (mg/dL)", min_value=0, max_value=500, step=1)
post_meal_sugar = st.sidebar.number_input("Post-Meal Sugar Levels (mg/dL)", min_value=0, max_value=500, step=1)

dietary_preferences = st.sidebar.text_input("Dietary Preferences (e.g., vegetarian, low-carb)")

# Generate meal plan button with custom style
if st.sidebar.button("🍽️ Generate My Meal Plan 🍽️"):
    meal_plan = get_meal_plan(api_key, fasting_sugar, pre_meal_sugar, post_meal_sugar, dietary_preferences)
    st.markdown("<div class='meal-plan'><h3>Here is your personalized meal plan:</h3></div>", unsafe_allow_html=True)
    st.markdown(meal_plan)