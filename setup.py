"""
Setup configuration for Agentic Framework
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="or-af",
    version="0.1.0",
    author="OR-AF Team",
    author_email="contact@or-af.dev",
    description="Operations Research Agentic Framework - A lightweight framework for creating AI agents with tool-calling capabilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iaakashRoy/or-af",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "openai>=1.0.0",
        "python-dotenv>=1.0.0",
        "pydantic>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
    },
    keywords="operations research ai agent llm openai tools framework optimization",
    project_urls={
        "Bug Reports": "https://github.com/iaakashRoy/or-af/issues",
        "Source": "https://github.com/iaakashRoy/or-af",
    },
)
