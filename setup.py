from setuptools import setup, find_packages

setup(
    name='SpotifyAPI',
    url='https://github.com/awsloth/spotifyAPI',
    author='Adam W',
    author_email='awslothhelp@gmail.com',
    packages=find_packages(),
    install_requires=['requests'],
    version='0.1',
    license='MIT',
    description='SpotifyAPI interactive code',
    long_description=open('README.md').read(),
)
