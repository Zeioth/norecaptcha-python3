'''
    NO-CAPTCHA VERSION: 1.0
    PYTHON VERSION:     3.x
 '''

import json
from urllib.request import Request, urlopen
from urllib.parse import urlencode


VERIFY_SERVER = "www.google.com"


class RecaptchaResponse(object):

    def __init__(self, is_valid, error_code=None):
        self.is_valid = is_valid
        self.error_code = error_code

    def __repr__(self):
        return "Recaptcha response: %s %s" % (
            self.is_valid, self.error_code)

    def __str__(self):
        return self.__repr__()


def displayhtml(site_key, language=''):
    """Gets the HTML to display for reCAPTCHA

    site_key -- The site key
    language -- The language code for the widget.
    """

    return """<script src="https://www.google.com/recaptcha/api.js?hl=%(LanguageCode)s" async="async" defer="defer"></script>
      <div class="g-recaptcha" data-sitekey="%(SiteKey)s"></div>
""" % {
        'LanguageCode': language,
        'SiteKey': site_key,
    }


def submit(response,
           secret_key,
           remote_ip,
           verify_server=VERIFY_SERVER):
    """
    Submits a reCAPTCHA request for verification. Returns RecaptchaResponse
    for the request

    response -- The value of response from the form
    secret_key -- your reCAPTCHA secret key
    remote_ip -- the user's ip address
    """

    if not(response and len(response)):
        return RecaptchaResponse(is_valid=False, error_code='incorrect-captcha-sol')

    def encode_if_necessary(s):
        if isinstance(s, str):
            return s.encode('utf-8')
        return s

    params = urlencode({
        'secret': encode_if_necessary(secret_key),
        'remoteip': encode_if_necessary(remote_ip),
        'response': encode_if_necessary(response),
    })

    params = params.encode('utf-8')

    request = Request(
        url="https://%s/recaptcha/api/siteverify" % verify_server,
        data=params,
        headers={
            "Content-type": "application/x-www-form-urlencoded",
            "User-agent": "reCAPTCHA Python"
        }
    )
    httpresp = urlopen(request)

    return_values = json.loads(httpresp.read().decode('utf-8'))
    httpresp.close()

    return_code = return_values['success']

    if return_code:
        return RecaptchaResponse(is_valid=True)
    else:
        return RecaptchaResponse(is_valid=False, error_code=return_values['error-codes'])
