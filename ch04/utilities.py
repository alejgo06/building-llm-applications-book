import json
import re

def extract_json(text):
    idx_brace = text.find('{')
    idx_bracket = text.find('[')

    # ¿Cuál aparece primero: { o [ ?
    if idx_bracket != -1 and (idx_brace == -1 or idx_bracket < idx_brace):
        start, close_char = idx_bracket, ']'
    elif idx_brace != -1:
        start, close_char = idx_brace, '}'
    else:
        raise ValueError("No se encontró JSON en la respuesta")

    end = text.rfind(close_char)
    if end == -1 or end < start:
        raise ValueError("JSON malformado (no se encontró cierre)")

    json_str = text[start:end + 1]

    # Eliminar comas finales antes de } o ]
    json_str = re.sub(r',\s*([\}\]])', r'\1', json_str)

    return json.loads(json_str)

def to_obj(s):
    try:
        return extract_json(s)
    except Exception:
        return {}