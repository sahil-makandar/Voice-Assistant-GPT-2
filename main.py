import speech_recognition as sr
import pyttsx3
from transformers import AutoModelForCausalLM, AutoTokenizer
import os

# Initialize the GPT-2 model and tokenizer
model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognizer and microphone
recognizer = sr.Recognizer()
microphone = sr.Microphone()

def clear_screen():
    """Clear the screen"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def recognize_speech():
    """Listen to speech and recognize it using Google Speech Recognition."""
    clear_screen()
    with microphone as source:
        print('Listening...')
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio_data = recognizer.listen(source)  # Listen to the audio
        try:
            # Recognize the speech using Google Speech Recognition
            text = recognizer.recognize_google(audio_data)
            print(f'You said: {text}')
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

def generate_response(prompt):
    """Generate a response from the GPT-2 model."""
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    gen_tokens = model.generate(
        input_ids,
        do_sample=True,
        temperature=0.9,
        max_length=100,
    )
    gen_text = tokenizer.decode(gen_tokens[0], skip_special_tokens=True)
    return gen_text

def main():
    text = recognize_speech()
    if text:
        response = generate_response(text)
        clear_screen()
        print(f'GPT Response: {response}')
        engine.say(response)
        engine.runAndWait()

if __name__ == "__main__":
    main()
