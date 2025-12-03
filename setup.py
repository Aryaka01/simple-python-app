"""Setup configuration for simple-python-app."""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="simple-python-app",
    version="1.0.0",
    author="Aryaka Agarwal",
    author_email="Aryaka0018@gmail.com",
    description="A simple Python application for Jenkins pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aryaka01/simple-python-app",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "flake8>=5.0.0",
            "black>=22.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "simple-python-app=myapp.cli:main",
        ],
    },
)
