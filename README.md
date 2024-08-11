# Voice Assistant Using GPT-2

This project is a Python-based voice assistant that uses the GPT-2 model for natural language processing. The assistant listens to your voice input, processes it using the GPT-2 model, and then responds with a generated text output, which is spoken back to you using text-to-speech.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [How It Works](#how-it-works)
- [Error Handling](#error-handling)
- [Contributing](#contributing)

## Description

This project integrates multiple Python libraries to create a simple voice assistant. The assistant listens to your voice input via a microphone, converts the speech to text, and then uses the GPT-2 model from Hugging Face Transformers to generate a response. Finally, it uses a text-to-speech engine to speak the generated response back to you.

The project is an example of how to combine speech recognition, natural language processing, and text-to-speech technologies into a seamless voice interaction system.

## Features

- **Speech Recognition**: Converts spoken language into text using the Google Web Speech API.
- **Natural Language Processing**: Utilizes the GPT-2 model to generate coherent and contextually relevant text responses.
- **Text-to-Speech**: Uses `pyttsx3` to convert text responses into speech.
- **Error Handling**: Handles errors related to speech recognition and model response generation.

## Installation

Follow these steps to set up the project on your local machine:

### Clone the Repository

```bash
git clone https://github.com/sahil-makandar/Voice-Assistant-GPT-2.git
cd Voice-Assistant-GPT-2
```

## Create a Virtual Environment (Optional but Recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

## Install Dependencies

Install the necessary packages listed in the `requirements.txt` file using pip:

```bash
pip install -r requirements.txt
```

## Additional Setup

Ensure you have an active internet connection as the Google Web Speech API is used for speech recognition, and the GPT-2 model will be downloaded from Hugging Face's model repository during execution.

## Usage

Once the setup is complete, you can run the script using:

```bash
python main.py
```

## Interaction

- The assistant will start by listening for your voice input.
- Speak clearly into the microphone.
- The assistant will process your input, generate a response, and speak it back to you.

## Requirements

The project relies on several Python libraries, which are listed in the `requirements.txt` file. Below are the primary dependencies:

- `speech_recognition`: For converting spoken words into text.
- `pyttsx3`: For converting text responses into speech.
- `transformers`: For loading the GPT-2 model and tokenizer.

## How It Works

### Initialization:
- The script initializes the GPT-2 model and tokenizer using the `transformers` library.
- It also initializes the text-to-speech engine using `pyttsx3` and sets up the speech recognizer and microphone.

### Listening:
- The script listens to the user's voice input using the microphone.
- The speech recognizer adjusts for ambient noise to improve accuracy.

### Speech Recognition:
- The user's speech is converted to text using the Google Web Speech API.

### Processing:
- The recognized text is used as a prompt for the GPT-2 model.
- The GPT-2 model generates a response based on the input text.

### Text-to-Speech:
- The generated response is converted into speech using `pyttsx3` and spoken back to the user.

## Error Handling

- **UnknownValueError**: Occurs when the speech recognizer cannot understand the audio.
- **RequestError**: Occurs when there is an issue with the Google Web Speech API request.

In either case, appropriate error messages are printed to the console to inform the user.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request with your changes. Make sure your contributions are well-documented and tested.

