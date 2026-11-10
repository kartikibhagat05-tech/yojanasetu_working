# chatbot/views.py
from django.shortcuts import render
from .utils import detect_language, translate_to_english, translate_to_user_lang, get_casual_response, find_eligible_schemes

def chatbot_page(request):
    """
    Handles GET request from user and returns chatbot response.
    """
    user_message = request.GET.get('message', '').strip()
    response_text = "Hello! Ask me about government schemes."  # default greeting

    schemes_list = []  # For displaying multiple schemes neatly

    if user_message:
        # Detect user language and translate message to English
        user_lang = detect_language(user_message)
        translated_msg = translate_to_english(user_message)

        # 1️⃣ Check for casual responses
        casual_response = get_casual_response(translated_msg)
        if casual_response:
            response_text = casual_response
        else:
            # 2️⃣ Find eligible government schemes
            schemes = find_eligible_schemes(translated_msg)
            if schemes.exists():
                response_text = "Here are some schemes you may be eligible for:"
                for scheme in schemes:
                    schemes_list.append({
                        "name": scheme.name,
                        "category": scheme.category,
                        "link": scheme.official_link
                    })
            else:
                response_text = "Sorry, I could not find any matching schemes."

        # Translate the response back to user's language
        response_text = translate_to_user_lang(response_text, user_lang)

    return render(request, "chatbot/chatbot.html", {
        "response": response_text,
        "schemes": schemes_list,
        "user_message": user_message
    })
