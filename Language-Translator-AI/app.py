from flask import Flask, render_template, request, redirect, url_for
from modules.language_detect import detect_language
from modules.speech_recognition import recognize_speech
from modules.translation import translate_text
from modules.text_to_speech import text_to_speech
from modules.emergency import send_emergency_message
from modules.offline_mode import offline_speech_recognition
from modules.image_translation import image_to_text
from modules.community import add_message, view_messages
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        speech_text = recognize_speech()
        detected_lang = detect_language(speech_text)
        target_lang = request.form.get('target_language', 'en')
        translated_text = translate_text(speech_text, target_lang)
        text_to_speech(translated_text)
        return render_template('translation.html', speech_text=speech_text, translated_text=translated_text, detected_lang=detected_lang)
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/emergency', methods=['GET', 'POST'])
def emergency():
    if request.method == 'POST':
        try:
            send_emergency_message()
            return render_template('emergency.html', message="Emergency Alert Sent Successfully!")
        except Exception as e:
            return f"Error: {str(e)}"
    return render_template('emergency.html')

@app.route('/community', methods=['GET', 'POST'])
def community():
    if request.method == 'POST':
        try:
            name = request.form.get('name', 'Anonymous')
            language = request.form.get('language', 'en')
            message = request.form.get('message', '')
            if not message.strip():
                return render_template('community.html', error="Message cannot be empty.")
            add_message(name, language, message)
            return redirect(url_for('community'))
        except Exception as e:
            return f"Error: {str(e)}"
    messages = view_messages()
    return render_template('community.html', messages=messages)

@app.route('/image-translate', methods=['POST'])
def image_translate():
    try:
        if 'image' not in request.files:
            return "No image uploaded."
        
        image_file = request.files['image']
        if image_file.filename == '':
            return "No selected image."
        
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
        image_file.save(image_path)
        
        target_language = request.form.get('target_language', 'en')
        translated_text = image_to_text(image_path, target_language)
        
        return render_template('translation.html', speech_text='Image Text', translated_text=translated_text, detected_lang='N/A')
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
