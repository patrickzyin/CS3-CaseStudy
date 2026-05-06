# Helper function to parse speech text
def parse_speech_text(text):
    # Converts list-formatted text to a single string
    # Some speeches are stored as ["sentence 1", "sentence 2"]
    try:
        speech_list = ast.literal_eval(text)
        if isinstance(speech_list, list):
            return ' '.join(speech_list)
    except:
        pass
    return text


# Helper function to clean speech text
def clean_speech_text(text):
    # Removes audience reactions like (applause) and [laughter] from the text
    text = re.sub(r'\([^)]*\)', '', text)
    text = re.sub(r'\[(?!\'[^\]]*$)[^\]]*\]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


# Helper function to normalize titles
def normalize_title(title):
    # Removes "Part 2:", "Part 3:", etc. from titles
    normalized = re.sub(r'^Part\s+\d+[\s:‐\-–—]+', '', title, flags=re.IGNORECASE)
    return normalized.strip()


# Helper function to check if title is a continuation
def is_continuation(title):
    # Checks if a speech title indicates it's a continuation (Part 2)
    return bool(re.match(r'^Part\s+\d+', title, flags=re.IGNORECASE))