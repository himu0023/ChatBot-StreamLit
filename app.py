import os
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))

try:
    nltk.download("punkt")
except:
    pass

intents = [
    {
        "tag":"greeting",
        "patterns":['Hi', 'Hey', 'Hello', 'How are you', "What's up"],
        "responses":['Yoo', "What's up shorty", "Sexy what about you", "I am always up"]
    },
    {
        "tag":"goodbye",
        "patterns":["Bye", "See you later", "Goodbye","Take care"],
        "responses":["See you Shorty", "Catch me", "Never say Bye", "I am all good, you take care"]
    },
    {
        "tag":"thanks",
        "patterns":["Thank you","Thanks","Thanks a lot", "I appreciate it"],
        "responses":["Not to worry, glad to help anytime", "Not to worry, glad to help anytime", "Not to worry, glad to help anytime","I appreciate you most"]
    },
    {
        "tag":"about",
        "patterns":["Who are you", "What can you do","What are you", "What is your purpose"],
        "responses":["I am a ChatBot", "I can assist you", "I am a ChatBot build by Himu23", "My purpose is to assist you and provide help"]
    },
    {
        "tag":"help",
        "patterns":["Help", "I need help","Can you help me", "What should I do"],
        "responses": ["Sure, what do you need help with?", "I'm here to help. What's the problem?", "What's the problem?", "How can I assist you?"]
    },
    {
        "tag":"age",
        "patterns":["What is your age", "How old are you"],
        "responses":["I wasn’t born, so I don’t really have an age like a person does.","As an AI, I don’t age — I was developed by OpenAI and released in 2024.","I’m not a living being, so the concept of age doesn’t exactly apply to me.","I’m a machine learning model created in 2024 — you could think of that as my launch date.","Humans count age by years alive; since I’m software, I don’t follow that timeline."]
    },
    {
        "tag":"weather",
        "patterns":["What's the weather like", "How's the weather today"],
        "responses":["I can't check live weather, but a weather app can help!","Not sure about the current weather — try Google or your phone assistant.","I don’t have real-time updates, but you can easily find it online."]
    },
    {
        "tag":"fitness",
        "patterns":["How can I stay fit", "What sould I do to reduce my weight","What is healty food can I eat","What exercies can I do to stay fit"],
        "responses":["Eat clean, move daily, sleep well, and stay consistent that the forumla","Healthy eating, daily exercise, and discipline are key to fitness and weight loss","Fule ypur body with real food, stay physically active, and keep your goals in sight.","Cut the junk, move your body, and stay consistent result will follow"]
    },
    {
        "tag":"life",
        "patterns":["What is life","Why we are living life","What is the purpose of living","Are we really real"],
        "responses":["We live to experience, to question, and to give our own meaning to this strange thing called life.","Wheather real or not, life is what we make of it purpose comes from how we choose to live.","Life may be mystrery, but our thoughts, choices, and actions make it real enough","Even if realuty is uncertain, the meaning we give to life is what makes it matter."]
    }
]


# Creating the vectorizer and classifier 
vectorizer = TfidfVectorizer()
clf = LogisticRegression(random_state=0, max_iter=10000)

tags = []
patterns = []
for intent in intents:
  for pattern in intent['patterns']:
    tags.append(intent['tag'])
    patterns.append(pattern)

X = vectorizer.fit_transform(patterns)
y = tags
clf.fit(X,y)

def chatbot(input_text):
  input_text = vectorizer.transform([input_text])
  tag = clf.predict(input_text)[0]
  for intent in intents:
    if intent['tag']== tag:
      response = random.choice(intent['responses'])
      return response

counter = 0 
def main():
  global counter
  st.title("Chatbot")
  st.write("Welcome. Please write a querry and press Enter to start the Convo.")

  counter+=1
  user_input = st.text_input("You", key = f"user_input_{counter}")

  if user_input:
    response = chatbot(user_input)
    st.text_area("Chatbot:", value=response, height=100, max_chars=None, key=f"chatbot_response_{counter}")

    if response.lower() in ['goodbye','bye']:
      st.write("Thank you for chatting with me. Have a greate day!")
      st.stop()

if __name__ == '__main__':
  main()
