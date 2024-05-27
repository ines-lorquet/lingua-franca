from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

LANGUAGES = {
    'en-US': 'Anglais',
    'fr': 'Français',
    'es': 'Espagnol',
    'de': 'Allemand',
    'it': 'Italien',
    'pt-BR': 'Portugais brésilien',
    'pt-PT': 'Portugais européen',
    'nl': 'Néerlandais',
    'ru': 'Russe',
    'zh': 'Chinois',
    'ja': 'Japonais',
    'ko': 'Coréen',
    # Ajoutez d'autres langues selon vos besoins
}

@app.route('/translate', methods=['POST'])
def translate_text():
    text = request.form['text']
    input_lang = request.form['input_language']
    output_lang = request.form['output_language']

    translator = Translator()

    if input_lang == 'auto':
        detected_lang = translator.detect(text).lang
        translation = translator.translate(text, dest=output_lang)
    else:
        translation = translator.translate(text, src=input_lang, dest=output_lang)

    return render_template('index.html', text=text, translation=translation.text, input_lang=input_lang, output_lang=output_lang, languages=LANGUAGES)
