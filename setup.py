try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Persistence for reddit',
    'author': 'Carl Burks',
    'url': 'http://www.github.com/crb02005',
    'download_url': 'http://www.github.com/crb02005.',
    'author_email': 'crb02005@gmail.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['RedditPersister'],
    'scripts': [],
    'name': 'RedditPersister'
}

setup(**config)