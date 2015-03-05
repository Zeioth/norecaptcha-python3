# norecaptcha-python3
 Python 3 client forGoogle No CAPTCHA reCAPTCHA services.

Installation
==============
sudo pip install norecaptcha-python3

Example of use
==============
    from norecaptcha3.captcha import submit
    
    # Check captcha
    r = submit(remote_ip=user_ip,
               response=client_code,
               secret_key=captcha_secret)
    if not r.is_valid:
        raise Exception('Invalid captcha')

Fork of: https://github.com/oursky/norecaptcha
to match the recently update of Google Captcha usage.
