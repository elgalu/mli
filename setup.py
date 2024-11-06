from setuptools import setup, find_packages

setup(
    name="mli",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mli=mli.main:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A package that redirects users to the correct installation method",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
