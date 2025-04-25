from setuptools import setup, find_packages

setup(
    name="ai-token-counter",
    version="0.1.0",
    author="Your Name",
    description="A token counter utility",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pytest",
        "black",
        "pylint"
    ],
    entry_points={
        "console_scripts": [
            "ai-token-counter = ai_token_counter.__main__:main",
        ],
    },
    python_requires=">=3.8",
)
