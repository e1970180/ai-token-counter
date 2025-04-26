"""
Setup script for ai-token-counter package.

Purpose:
    Configures installation, dependencies and console entry point.
"""

from setuptools import setup, find_packages

setup(
    name="ai-token-counter",
    version="0.1.0",
    description="Lightweight token counter for AI models using tiktoken",
    author="",
    license="MIT",
    packages=find_packages(),  # Automatically find ai_token_counter
    install_requires=[
        "tiktoken>=0.4.0",
        "pytest>=7.0.0",
        "black>=23.9.1",
        "pylint>=2.17.5",
    ],
    entry_points={
        "console_scripts": [
            "ai-token-counter = ai_token_counter.__main__:main",
        ],
    },
    python_requires=">=3.10",
)
