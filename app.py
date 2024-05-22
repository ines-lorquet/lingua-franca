from flask import Flask, request, render_template
from deepl import Translator

app = Flask(__name__)

LANGUAGES = {
    'en-US': 'Anglais',
    'fr': 'Français',
    'es': 'Espagnol',
    'de': 'Allemand',
    'it': 'Italien',
    'pt': 'Portugais',
    'nl': 'Néerlandais',
    'ru': 'Russe',
    'zh': 'Chinois',
    'ja': 'Japonais',  # Ajout du Japonais
    'ko': 'Coréen',
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
                translator = Translator('ba89e068-b6e5-498b-ac12-320d3959ad2c:fx')
                if source_lang == 'auto':
                    target_text = translator.translate_text(source_text, target_lang=target_lang, source_lang=None)
                else:
                    target_text = translator.translate_text(source_text, target_lang=target_lang, source_lang=source_lang)
            else:
                target_text = "Erreur: le texte source ne peut pas être vide."

        return render_template('index.html', source_text=source_text, target_text=target_text, source_lang=source_lang, target_lang=target_lang, languages=LANGUAGES)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
