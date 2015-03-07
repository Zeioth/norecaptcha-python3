# norecaptcha-python3
 Python 3 server-side library for google No CAPTCHA reCAPTCHA services.

Installation
==============
    pip install norecaptcha-python3

Example of use
==============
   ```python
    from norecaptcha3.captcha import submit
    
    # Check captcha
    r = submit(remote_ip=user_ip,
               response=client_code,
               secret_key=captcha_secret)
    if not r.is_valid:
        raise Exception('Invalid captcha')
   ```
    
This project is a fork of: https://github.com/oursky/norecaptcha
