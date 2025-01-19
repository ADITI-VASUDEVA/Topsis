from setuptools import setup, find_packages

setup(
    name="Topsis-Aditi-102216097",
    version="0.1.0",
    author="Aditi Vasudeva",
    author_email="aditivasudeva2002@gmail.com",
    description="A dynamic invoice generator package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",  
    packages=find_packages(),
    install_requires=[
        "reportlab",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",  
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    test_suite="tests",
)
