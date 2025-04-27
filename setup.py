"""
Setup script for ai-token-counter package.

Purpose:
    Configures installation, dependencies and console entry point.
"""

from setuptools import setup, find_packages

setup(
    name="ai-token-counter",
    version="1.0.0",
    author="Alex Pro",
    description="A token counter for AI models utility",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "tiktoken>=0.4.0",
        "pytest>=7.0.0",
        "black>=23.9.1",
        "pylint>=2.17.5",
    ],
    entry_points={
        "console_scripts": [
            "ai-token-counter = ai_token_counter.main:main",
        ],
    },
    python_requires=">=3.10",
)
