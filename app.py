from flask import Flask, request, render_template
from translate import Translator

app = Flask(__name__)

LANGUAGES = {
    'auto': 'Détection automatique',
    'en': 'Anglais',
    'fr': 'Français',
    'es': 'Espagnol',
    'de': 'Allemand',
    'it': 'Italien',
    'pt': 'Portugais',
    'nl': 'Néerlandais',
    'ru': 'Russe',
    'zh': 'Chinois',
    'ja': 'Japonais',
    # Ajoutez d'autres langues selon vos besoins
}

@app.route('/', methods=['GET', 'POST'])
def translate_text():
    source_text = ''
    target_text = ''
    source_lang = 'auto'
    target_lang = 'en'
    try:
        if request.method == 'POST':
            source_text = request.form.get('source_text')
            source_lang = request.form.get('source_lang')
            target_lang = request.form.get('target_lang')

            if source_text:
                translator = Translator(to_lang=target_lang)
                target_text = translator.translate(source_text)
            else:
                target_text = "Erreur: le texte source ne peut pas être vide."

        return render_template('index.html', source_text=source_text, target_text=target_text, source_lang=source_lang, target_lang=target_lang, languages=LANGUAGES)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
