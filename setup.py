from setuptools import setup, find_packages

setup(
    name="modeval",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[

    ],
    extras_require={
        "test": [
            "pytest",
            "flake8",
            "pytest-cov"
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
