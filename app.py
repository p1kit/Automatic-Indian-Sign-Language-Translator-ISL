import streamlit as st
import speech_recognition as sr
import numpy as np
import tempfile
import os
from PIL import Image
import string
from audio_recorder_streamlit import audio_recorder

def transcribe_audio(file_path):
    r = sr.Recognizer()
    isl_gif = ['any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', 'be careful',
               'can we meet tomorrow', 'did you book tickets', 'did you finish homework', 'do you go to office', 'do you have money',
               'do you want something to drink', 'do you want tea or coffee', 'do you watch TV', 'dont worry', 'flower is beautiful',
               'good afternoon', 'good evening', 'good morning', 'good night', 'good question', 'had your lunch', 'happy journey',
               'hello what is your name', 'how many people are there in your family', 'i am a clerk', 'i am bore doing nothing',
               'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i dont understand anything', 'i go to a theatre', 'i love to shop',
               'i had to say something but i forgot', 'i have headache', 'i like pink colour', 'i live in nagpur', 'lets go for lunch', 'my mother is a homemaker',
               'my name is john', 'nice to meet you', 'no smoking please', 'open the door', 'please call me later',
               'please clean the room', 'please give me your pen', 'please use dustbin dont throw garbage', 'please wait for sometime', 'shall I help you',
               'shall we go together tommorow', 'sign language interpreter', 'sit down', 'stand up', 'take care', 'there was traffic jam', 'wait I am thinking',
               'what are you doing', 'what is the problem', 'what is todays date', 'what is your father do', 'what is your job',
               'what is your mobile number', 'what is your name', 'whats up', 'when is your interview', 'when we will go', 'where do you stay',
               'where is the bathroom', 'where is the police station', 'you are wrong', 'address', 'agra', 'ahemdabad', 'all', 'april', 'assam', 'august', 'australia', 'badoda', 'banana', 'banaras', 'banglore',
               'bihar', 'bihar', 'bridge', 'cat', 'chandigarh', 'chennai', 'christmas', 'church', 'clinic', 'coconut', 'crocodile', 'dasara',
               'deaf', 'december', 'deer', 'delhi', 'dollar', 'duck', 'febuary', 'friday', 'fruits', 'glass', 'grapes', 'gujrat', 'hello',
               'hindu', 'hyderabad', 'india', 'january', 'jesus', 'job', 'july', 'july', 'karnataka', 'kerala', 'krishna', 'litre', 'mango',
               'may', 'mile', 'monday', 'mumbai', 'museum', 'muslim', 'nagpur', 'october', 'orange', 'pakistan', 'pass', 'police station',
               'post office', 'pune', 'punjab', 'rajasthan', 'ram', 'restaurant', 'saturday', 'september', 'shop', 'sleep', 'southafrica',
               'story', 'sunday', 'tamil nadu', 'temperature', 'temple', 'thursday', 'toilet', 'tomato', 'town', 'tuesday', 'usa', 'village',
               'voice', 'wednesday', 'weight', 'please wait for sometime', 'what is your mobile number', 'what are you doing', 'are you busy']

    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    with sr.AudioFile(file_path) as source:
        audio = r.record(source)
        try:
            transcribed_text = r.recognize_google(audio).lower()
            transcribed_text = ''.join(char for char in transcribed_text if char not in string.punctuation)

            if transcribed_text == 'goodbye' or transcribed_text == 'good bye' or transcribed_text == 'bye':
                st.warning("Goodbye!")
            elif transcribed_text in isl_gif:
                st.image(f"ISL_Gifs/{transcribed_text}.gif", use_column_width=True)
            else:
                for char in transcribed_text:
                    if char in arr:
                        image = Image.open(f"letters/{char}.jpg")
                        st.image(image, caption=f"Letter: {char.upper()}", use_column_width=True)
                    else:
                        continue
            return transcribed_text
        except sr.UnknownValueError:
            return "Sorry, I could not understand what you said."
        except sr.RequestError as e:
            return f"Could not request results; {e}"

def main():
    st.title("Hearing Impairment Assistant")

    audio_data = audio_recorder()

    if audio_data:
        st.audio(audio_data, format="audio/wav")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            f.write(audio_data)
            temp_file_path = f.name

        transcribed_text = transcribe_audio(temp_file_path)
        os.remove(temp_file_path)

        st.success(f"You said: {transcribed_text}")

if __name__ == "__main__":
    main()
