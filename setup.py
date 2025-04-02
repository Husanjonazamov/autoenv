from setuptools import setup, find_packages

setup(
    name="autoenv",                 # Paket nomi
    version="0.1",                  # Paket versiyasi
    packages=find_packages(),       # Paketni aniqlash
    install_requires=[              # Talablar (agar boshqa paketlarga bog'liq bo'lsa)
        'requests',                 # Misol uchun, agar `requests` paketi kerak bo'lsa
    ],
    entry_points={                  # Komanda liniyasida ishlash
        'console_scripts': [
            'autoenv=autoenv.cli:autoenv',  # autoenv komandasi `autoenv.cli:autoenv` ga ulanishi kerak
        ],
    },
    long_description=open('README.md').read(),  # README faylini qo'shish
    long_description_content_type='text/markdown',  # README fayli markdown formatida
    url='https://github.com/your-username/autoenv',  # GitHub URL
    author='Your Name',                    # Muallif nomi
    author_email='your-email@example.com',  # Email manzili
    classifiers=[                          # PyPI uchun tasniflar
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
