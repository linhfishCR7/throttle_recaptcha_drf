from django.conf import settings
import requests

def verify_recaptcha(g_token: str) -> bool:
    data = {
        'response': g_token,
        'secret': settings.RE_CAPTCHA_SECRET_KEY
    }
    resp = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    result_json = resp.json()
    return result_json.get('success') is True
    