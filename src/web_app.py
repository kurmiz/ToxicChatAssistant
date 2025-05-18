from flask import Flask, render_template, request, jsonify
from task_execution.task_router import route_task
from natural_language_processing.intent_recognition import recognize_intent

from text_to_speech.speech_synthesis import synthesize_speech

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'audio' in request.files:
        audio_file = request.files['audio']
        user_input = transcribe_audio(audio_file)
    else:
        user_input = request.json['input']
    
    intent = recognize_intent(user_input)
    response = route_task(intent, user_input)
    audio_response = synthesize_speech(response)
    
    return jsonify({'response': response, 'audio': audio_response})

if __name__ == '__main__':
    app.run(debug=True)
