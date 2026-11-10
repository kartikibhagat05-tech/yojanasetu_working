# chatbot/utils.py
from deep_translator import GoogleTranslator
import re
from schemes.models import Scheme

# -----------------------------
# Translator
# -----------------------------
def detect_language(text):
    """
    Detect the language of the input text.
    Returns language code like 'en', 'hi', 'mr', etc.
    """
    try:
        return GoogleTranslator(source='auto', target='en').detect(text)
    except:
        return 'en'

def translate_to_english(text):
    """Translate any text to English"""
    try:
        return GoogleTranslator(source='auto', target='en').translate(text)
    except:
        return text

def translate_to_user_lang(text, user_lang):
    """Translate English text back to user's language"""
    try:
        if user_lang and user_lang != 'en':
            return GoogleTranslator(source='en', target=user_lang).translate(text)
        return text
    except:
        return text

# -----------------------------
# Casual Responses
# -----------------------------
CASUAL_RESPONSES = {
    r'hi|hello|hey': "Hello! How can I help you today?",
    r'how are you': "I'm a bot, but I'm here to help you find government schemes!",
    r'thank you|thanks': "You're welcome! 🙂",
    r'bye|goodbye': "Goodbye! Stay safe and informed.",
}

def get_casual_response(text):
    text = text.lower()
    for pattern, response in CASUAL_RESPONSES.items():
        if re.search(pattern, text):
            return response
    return None

# -----------------------------
# Entity Extraction
# -----------------------------
def extract_entities(text):
    entities = {}

    # Extract age
    age_match = re.search(r'\b(\d{1,2})\b', text)
    if age_match:
        entities['age'] = int(age_match.group(1))

    # Extract state
    STATES = ["Maharashtra", "Delhi", "Karnataka", "Tamil Nadu", "Gujarat"]
    for state in STATES:
        if state.lower() in text.lower():
            entities['state'] = state

    # Extract occupation/role
    ROLES = ["student", "farmer", "business", "senior", "job seeker"]
    for role in ROLES:
        if role.lower() in text.lower():
            entities['occupation'] = role

    return entities

# -----------------------------
# Eligible Schemes Finder
# -----------------------------
def find_eligible_schemes(text):
    """
    Returns a queryset of schemes matching user's entities (age, occupation, state)
    """
    entities = extract_entities(text)
    schemes = Scheme.objects.filter(status="active")

    # Filter by age
    if 'age' in entities:
        schemes = schemes.filter(age_requirement__lte=entities['age'])

    # Filter by occupation/role
    if 'occupation' in entities:
        schemes = schemes.filter(category__icontains=entities['occupation'])

    # Filter by state (simplified: central/state type)
    if 'state' in entities:
        schemes = schemes.filter(type__in=["central", "state"])

    return schemes
