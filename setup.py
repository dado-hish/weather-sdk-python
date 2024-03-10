from setuptools import setup, find_packages

setup(
    name='weather-sdk-nikita-alekseev',
    version='0.1',
    packages=find_packages(),
    description='SDK for accessing weather data from OpenWeatherMap API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your@email.com',
    url='https://github.com/yourusername/weather-sdk',
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
