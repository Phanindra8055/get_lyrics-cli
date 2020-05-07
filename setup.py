from setuptools import setup

setup(
    name = 'get_lyrics',
    version = '0.1.0',
    packages = ['get_lyrics'],
    entry_points = {
        'console_scripts': [
            'get_lyrics = get_lyrics.__main__:main'
        ]
    })
