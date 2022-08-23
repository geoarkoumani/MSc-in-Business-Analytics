# Import all the required libraries
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

# Initialize names,usernames & passwords
names = ["Georgia Arkoumani", "Myrto Poulou", "Faey Zaragka", "Anastasia Koutsodimitropoulou", "guest"]
usernames = ["geoark", "myrtop", "faeyzrg", "anastasiak", "guest"]
# For the first run the passwords were defined and stored into the file hashed_pw.pkl
# For security reasons once they were created they are now hidden
passwords = ["XXX", "XXX", "XXX", "XXX", "XXX"]
# Use a hasher module to convert the plain text passwords to hashed passwords
hashed_passwords = stauth.Hasher(passwords).generate()
# Store the hashed passwords into the file ‘hashed_pw.pkl’
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)