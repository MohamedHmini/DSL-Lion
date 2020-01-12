from setuptools import setup



setup(
    name = 'lion-cli',
    version = '0.1.0',
    packages = ['lion'],
    entry_points = {
        'console_scripts': [
            'lion = lion.__main__:main'
        ]
    })