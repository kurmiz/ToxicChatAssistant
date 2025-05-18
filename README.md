# Toxic Assistant

A voice-controlled virtual assistant that can respond to various user queries through both voice and text interfaces. This project combines speech recognition, natural language processing, and text-to-speech technologies to create an interactive assistant experience.

## Features

- **Voice Recognition**: Converts spoken language to text
- **Natural Language Processing**: Identifies user intent from text input
- **Task Execution**: Performs various tasks based on user intent
- **Text-to-Speech**: Converts text responses to spoken language
- **Web Interface**: Browser-based UI for interacting with the assistant

## Supported Commands

The assistant can currently handle the following types of queries:
- Weather information
- Time queries
- Date queries
- Identity queries (asking about the assistant's name)
- General conversation

## Project Structure

```
project_root/
├── src/
│   ├── dialogue_management/    # Handles conversation flow
│   ├── natural_language_processing/  # Processes text input
│   ├── speech_recognition/     # Converts speech to text
│   ├── task_execution/         # Executes specific tasks
│   ├── text_to_speech/         # Converts text to speech
│   ├── utils/                  # Utility functions
│   ├── main.py                 # Main application entry point
│   └── web_app.py              # Web interface
├── templates/                  # HTML templates for web interface
├── tests/                      # Test files
└── requirements.txt            # Project dependencies
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/toxic-assistant.git
   cd toxic-assistant
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. For speech recognition functionality, you may need to install additional system dependencies:
   - On Windows: PyAudio should install automatically with pip
   - On macOS: `brew install portaudio`
   - On Linux: `sudo apt-get install python3-pyaudio`

## Usage

### Command Line Interface

Run the main application:
```
python src/main.py
```

The assistant will listen for voice commands through your microphone. Speak clearly and the assistant will respond both in text and speech.

### Web Interface

Run the web application:
```
python src/web_app.py
```

Then open your browser and navigate to `http://localhost:5000` to interact with the assistant through the web interface.

## Dependencies

- SpeechRecognition: For converting speech to text
- pyttsx3: For text-to-speech conversion
- PyAudio: For audio input/output
- Flask: For the web interface
- Requests: For making HTTP requests (e.g., weather data)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
