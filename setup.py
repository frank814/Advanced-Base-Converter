"""
Advanced Number Base Converter - Setup Script
Author: Frank Arthur
Version: 2.0.0
"""

from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="advanced-number-base-converter",
    version="2.0.0",
    author="Frank Arthur",
    author_email="frank@example.com",
    url="https://github.com/frank814/advanced-number-base-converter",
    description="Advanced tool for converting between decimal, binary, octal, hexadecimal, and other number systems",
    long_description="""
Advanced Number Base Converter
A professional tool for converting between decimal, binary, octal, hexadecimal, and other number systems.

Features:
- Supports bidirectional conversion between all number bases (2-16)
- Handles negative numbers with proper two's complement representation
- Comprehensive floating-point number conversions
- ASCII and Unicode character conversion
- Comprehensive input validation and error handling
- User-friendly command-line interface with clear formatting
- Step-by-step conversion explanations for educational purposes
- Efficient implementation with manual algorithms
- Multiple output formats
- Dark mode support

Author: Frank
Version: 2.0.0
    """,
    long_description_content_type="text/markdown",
    url="https://github.com/Frank/advanced-number-base-converter",
    py_modules=["bin_dec_converter"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Topic :: Education",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "number-converter=bin_dec_converter:main",
        ],
    },
    keywords="number-base-converter binary decimal octal hexadecimal ascii unicode floating-point",
    project_urls={
        "Bug Reports": "https://github.com/frank814/advanced-number-base-converter/issues",
        "Source": "https://github.com/frank814/advanced-number-base-converter",
        "Documentation": "https://github.com/frank814/advanced-number-base-converter#readme",
    },
)
