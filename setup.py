from distutils.core import setup

from os import path

README = path.abspath(path.join(path.dirname(__file__), 'README.md'))

setup(
   name='norecaptcha-python3',
   version='1.0',
   packages=['norecaptcha3'],
   description='Python 3 client for google No CAPTCHA reCAPTCHA services.',
   long_description=open(README).read(),
   author='Zeioth.',
   author_email='null@gmail.com',
   url='https://github.com/Zeioth/norecaptcha-python3',
   license='MIT'
)
