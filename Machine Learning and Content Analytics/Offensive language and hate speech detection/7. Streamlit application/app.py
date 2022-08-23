# Import all the required libraries
import streamlit as st  
from textblob import TextBlob
import pandas as pd
import pickle
from pathlib import Path
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from PIL import Image
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit_authenticator as stauth

# Set page title and icon
st.set_page_config(page_title="hateless app", page_icon=":speech_balloon:")
# Include link and scripts with Bootstrap CDN and Google Fonts
st.markdown("""
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Source+Code+Pro:ital,wght@0,600;1,400&display=swap" rel="stylesheet">
	""" ,unsafe_allow_html=True)
# Include CSS Styles
styl = f"""
    <style>
        h1 {{
    		font-family: Source Sans Pro;
		}}

		.stApp {{
			color: rgba(0, 0, 0, 0.87);
			font-family: Source Sans Pro;
		}}

		.main .block-container {{
			padding-top: 52px;
		}}

		.card {{
			background-color: #0F2147;
			box-shadow: 0 5px 10px #00000029;
			border-radius: 24px;
			padding: 24px;
			border: none;
			margin-bottom: 40px;
			position: relative;
			padding-bottom: 48px;
		}}

		.card .card-body {{
			padding: 0;
		}}

		.card .card-title {{
			color: white;
			font-size: 21px;
			font-weight: 500;
			font-family: Source Sans Pro;
			margin-bottom: -10px;
		}}

		.card .card-subtitle {{
			color: #B7BDC8;
			font-size: 16px;
			font-weight: 400;
			font-family: Source Sans Pro;
		}}

		.card .card-img {{
			background-repeat: no-repeat;
			background-position: top;
			width: 100%;
			height: 100%;
			top: 0;
			position: absolute;
		}}

		.main div[data-testid="stImage"] img{{
			background-repeat: no-repeat;
			position: absolute;
			top: -135px;
			right: 30px;
			width: 120px !important;
			height: 120px !important;
			box-shadow: 0px 5px 10px #00000029;
			border-radius: 65px;
		}}

		.stButton {{
			display: flex;
			justify-content: flex-end;
		}}

		.stButton > button {{
			color: white;
			background-color: #E35F52;
			width: 80px;
			height: 42px;
			border-radius: 12px;
			border: none;
		}}

		.stTextArea > label {{
			font-size: 16px;
		}}

		.stButton > button:hover {{
			color: white;
			background-color: #C85348;
			width: 80px;
			height: 42px;
			border-radius: 12px;
			border: none;
		}}

		.stButton > button:focus:not(:active) {{
			color: white;
			background-color: #C85348;
			width: 80px;
			height: 42px;
			border-radius: 12px;
			border: none;
		}}


		div[data-testid='stForm'] {{
			border-radius: 24px;
			box-shadow: 0 5px 10px #00000029;
			border: none;
			padding: 24px;
			background-color: #ffffff;
		}}

		div[data-baseweb="textarea"] {{
			border: none;    ;
		}}

		button[kind="header"] {{
			background-color: transparent;
			color:rgb(180, 167, 141)
		}}

		.stAlert > div[role="alert"] {{
			background-color: #a3d7dc;
			border: none;
			color: white;
			font-size: 16px;
			border-radius: 10px;
			box-shadow: 0 5px 10px #00000029;
			margin-top: 32px;
		}}

		.stAlert > div[role="alert"] p{{
			color: white;
			font-size: 16px;
			font-weight: 600;
		}}

		@media(hover){{
			header[data-testid="stHeader"] {{
				display:none;
			}}
			section[data-testid='stSidebar'] > div {{
				width: 300px;
				position: relative;
				z-index: 1;
				top: 0;
				left: 0;
				background-color: white;
				box-shadow: 0 5px 10px #00000029;
				border-right: 1px solid #0000001f;
				overflow-x: hidden;
				transition: 0.5s ease;
				white-space: nowrap;
			}}
			button[kind="header"] {{
				display: none;
			}}
		}}

		.element-container button[title="View fullscreen"]{{
			display: none;
		}}

		.stMarkdown p {{
			color: #989898;
			padding-top: 16px;
		}}

		.badge {{
			padding: 6px;
			font-size: 16px;
			font-weight: 600;
		}}

		.badge .badge-success {{
			background-color: #169368;
		}}

		.badge .badge-danger {{
			background-color: #C15959;
		}}

		.neutral {{
			padding: 6px;
			font-size: 16px;
			font-weight: 600;
			color: white;
			border-radius: 4px;
			background-color: #d2b48c !important;
		}}

		.streamlit-expander {{
			background-color: #0000000a;
			border: none;
			color: #0000008a;
			font-size: 16px;
			border-radius: 10px;
			box-shadow: 0 5px 10px #00000029;
			padding: 0;
		}}

		.streamlit-expander:hover {{
			background-color: #0000001f;
		}}


		.streamlit-expanderHeader,
		.streamlit-expanderHeader:hover {{
			color: #0F2147;
			font-weight: 600;
			padding: 16px;
			font-size: 16px;
			margin-top: 32px;
		}}

		div[data-testid="stExpander"] .streamlit-expanderHeader:hover svg{{
			fill: #5CBCA9 !important;
		}}

		div[data-testid="stExpander"] .streamlit-expanderHeader svg{{
			fill: #5CBCA9 !important;
		}}

		.streamlit-expanderContent {{
			background-color: #ffffff;
			border-bottom-left-radius: 10px;
			border-bottom-right-radius: 10px;
		}}

		.vega-embed.has-actions {{
			padding-top: 16px;
		}}

		.vega-embed summary {{
			margin-top: 16px;
		}}

		div[data-testid="stJson"] {{
			padding-top: 16px;
		}}

		div[data-testid="stHorizontalBlock"] {{
			margin-top: 145px;
			padding: 16px;
		}}

		div[data-testid="stText"] {{
			color:  #0F2147;
			font-size: 21px;
			font-weight: 500;
			font-family: Source Sans Pro;
			margin-bottom: -24px;
			margin-top: -12px;
			white-space: normal;
			overflow-wrap: break-word;
		}}

		.hr-container {{
			width: 100px;
			position: absolute;
			right: 50%;
			left: 42%;
			top: 10%;
		}}

		#about-us,
		#we-are-qc-greece {{
			text-align: center;
			color:  #0F2147;
			letter-spacing: 1.16px;
		}}

		#we-are-qc-greece,
		#hateless-app,
		#what-makes-us-special,
		#meet-the-team {{
			color:  #0F2147;
			margin-bottom: -28px;
		}}

		#login {{
			color:  #0F2147;
			font-weight: 500;
			font-family: Source Sans Pro;
		}}

		.stTextInput label {{
			color:  #0F2147;
			font-size: 15px;
			font-family: Source Sans Pro;
		}}

		div[data-baseweb="input"] {{
			padding-right: 0;
			border: none;
		}}

		.stTextInput svg {{
			fill: #0F2147;
			margin-right: 6px;
		}}

		.stButton button[kind="primary"] {{
			position: absolute;
			bottom: -440px;
			right: 14px;
		}}

		#welcome-georgia-arkoumani {{
			position: absolute;
			top: -134px;
			right: -303px;
			font-size: 18px;
			color:  #0F2147;
			font-family: Source Sans Pro;
			font-weight: 500;

		}}

		.main footer {{
			display: none !important;
		}}
    </style>
"""
st.markdown(styl, unsafe_allow_html=True)

# USER AUTHENTICATION

# Initialize names and usernames for login
names = ["Georgia Arkoumani", "Myrto Poulou", "Faey Zaragka", "Anastasia Koutsodimitropoulou", "guest"]
usernames = ["geoark", "myrtop", "faeyzrg", "anastasiak", "guest"]
# Load hashed passwords from hashed_pw.pkl file
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file: # Open file
    hashed_passwords = pickle.load(file)
# The hashed passwords are used to create an authentication object that consists of a name for the JWT cookie that will be stored on the client’s browser and used to re-authenticate the user without re-entering their credentials. 
# A random key is provided to be used to hash the cookie’s signature as well as the number of days to use the cookie for.
authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "hate_analyzer_app", "abcdef", cookie_expiry_days=30)
# In order to render the login module a name for the login form is provided, and was specified where the form should be located i.e. main body or sidebar (with default to main body).
name, authentication_status, username = authenticator.login("Login", "main")
# The returned name and authentication status allow the verified user to proceed to any restricted content by checking for any missing or wrong passwords.
if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

# LOAD LOCAL CSS FILE -2nd way but it gives error on deployment - to be fixed
# with open("styles.css") as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# CONVERT DICTIONARY TO DF
def convert_to_df(sentiment):
	sentiment_dict = {'Polarity':sentiment.polarity,'Subjectivity':sentiment.subjectivity}
	sentiment_df = pd.DataFrame(sentiment_dict.items(),columns=['Metric','Value'])
	return sentiment_df

# TOKEN SENTIMENT ANALYZER USING VADER
def analyze_token_sentiment(docx):
	analyzer = SentimentIntensityAnalyzer() # Initialize the analyzer
	positive_list = [] # Initialize the lists
	negative_list = []
	neutral_list = []
	for i in docx.split(): # Split comment in tokens
		res = analyzer.polarity_scores(i)['compound'] # Compound score is a metric that calculates the sum of all the lexicon ratings which have been normalized between -1(most extreme negative) and +1 (most extreme positive).
		if res > 0.1: # Threshold 0.1
			positive_list.append(i)
			positive_list.append(res)

		elif res <= -0.1:
			negative_list.append(i)
			negative_list.append(res)
		else:
			neutral_list.append(i)
	result = {'positives':positive_list,'negatives':negative_list,'neutral':neutral_list}
	return result 

# MAIN
def main():
	if authentication_status:
		menu = ["Home","About"] # Sidebar menu options
		#logo_lg = Image.open('images/logos/logo.png')
		st.sidebar.image('images/logos/logo.png', use_column_width=True)
		authenticator.logout("Logout", "sidebar")
		# SIDEBAR
		with st.sidebar: # Sidebar menu styles inline
				choice = option_menu(
					"",
					menu,
					icons=['house', 'info-circle'],
					styles={
						"icon": {"color": "#50B8C1", "font-size": "18px"}, 
						"nav-link": {"font-size": "18px", "text-align": "left", "--hover-color": "#0000000a", "font-family": "Source Sans Pro"},
						"nav-link-selected": {"background-color": "#0F2147"},
					}
				)
		if choice == "Home": # Check menu choice = HOME
			st.markdown("""
				<div class="card">
					<div class="card-body">
						<p class="card-title">Welcome to hateless app</p>
						<p class="card-subtitle">Start your comment analysis below and be...nice!</p>
					</div>
				</div>
			""" ,unsafe_allow_html=True)
			#logo_round = Image.open('images/logos/company.png')
			st.image('images/logos/company.png', use_column_width=True)
			# FORM 
			with st.form(key='nlpForm'):
				raw_text = st.text_area("Enter the comment to be analyzed") # Text area for comments
				submit_button = st.form_submit_button('Analyze')
			if submit_button:
				# EXPAND/COLLAPSE COMPONENT
				with st.expander("Sentiment metrics"):
					sentiment = TextBlob(raw_text).sentiment # Sentiment scores with Text Blob
					if sentiment.polarity > 0:
						st.markdown("""Sentiment: <span class="badge badge-success">Positive</span> :smiley: """, unsafe_allow_html=True)
					elif sentiment.polarity < 0:
						st.markdown("""Sentiment: <span class="badge badge-danger">Negative</span> :angry: """, unsafe_allow_html=True)
					else:
						st.markdown("""Sentiment: <span class="neutral">Neutral</span> 😐 """, unsafe_allow_html=True)
					result_df = convert_to_df(sentiment) # Convert into a dataframe
					st.dataframe(result_df)
				with st.expander("Sentiment token metrics"):
					token_sentiments = analyze_token_sentiment(raw_text)
					st.write(token_sentiments)
				with st.expander("Sentiment metrics visualization"):
					fig = px.bar(result_df, x='Metric', y='Value', color = 'Metric', height= 500, width=680, color_discrete_sequence=["#5CBCA9", "#E35F52"])
					st.plotly_chart(fig)
		else: # Check menu choice = ABOUT US
			st.title("About Us")
			st.markdown("""<div class="hr-container"><hr style="height:2px;border:none;color:#0F2147;background-color:#0F2147;margin-top:-10px" /> </div>""", unsafe_allow_html=True)
			st.subheader("We are QC Greece")
			st.write("""
				A start up Information Technology and data-driven company established in 2021 from a group of friends, who wanted with their product to contribute to the elimination of offensive language in social media.
				Our company provides the ‘hateless’ app.
			""")
			st.write("""
				Our mission is to detect and eliminate offensive language from social media and various platforms through the internet. Also, we provide our services to our clients (smaller or bigger companies) in order to find effective solutions in the social media platforms, such as banning users whose comments are rather offensive to other community members.
			""")
			st.subheader("hateless app")
			st.write("""
				The application was created in order to identify hate speech across all platforms and applications.
			""")
			st.write("""
				Machine learning and neural network algorithms were implemented in order to analyze the corresponding comments and calculate scores that determine if a comment is offensive or not. A sentiment analysis was also implemented to determine if a comment is positive, negative, or neutral. 
			""")
			st.write("""
				The user logs in the application, writes the specific comment that he/she wants to be analyzed and then he/she gets as an output a list of scores (positive, negative, or neutral), sentence token scores and diagrams that demonstrate how pleasant or subjective the comment is.
			""")
			st.subheader("What makes us special?")
			st.write("""
				We are eager to create a proper environment across all platforms. 
				Our team is specialized in data analysis and representation with User Interfaces of the actual results in order to determine the corresponding solutions.
			""")
			st.subheader("Meet the team")
			col1, col2, col3, col4 = st.columns(4) # GRID
			with col1:
				# team1 = Image.open('images/geo.png')
				st.image('images/geo.png', use_column_width=True)
				st.text("Georgia Arkoumani")
				st.caption("Data Engineer & UI Specialist")
			with col2:
				# team2 = Image.open('myrto.png')
				st.image('images/myrto.png', use_column_width=True)
				st.text("Myrto Poulou")
				st.caption("Statistician & Data Analyst")
			with col3:
				# team3 = Image.open('anastasia.png')
				st.image('images/anastasia.png', use_column_width=True)
				st.text("Anastasia Koutsodimitropoulou")
				st.caption("Business & Data Analyst")
			with col4:
				# team4 = Image.open('faey.png')
				st.image('images/faey.png', use_column_width=True)
				st.text("Eftychia Zaragka")
				st.caption("Data Engineer & DB Specialist")

if __name__ == '__main__':
	main()

