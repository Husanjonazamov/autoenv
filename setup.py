from setuptools import setup, find_packages

setup(
    name="autoenv",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'requests',
        'environs',
    ],
    entry_points={
        'console_scripts': [
            'autoenv=autoenv.cli:autoenv',
        ],
    },
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Husanjonazamov/autoenv',
    author='Husanjon Azamov',
    author_email='azamovhusanboy@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
