from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="gitghost",
    version="1.1.0",
    author="Sakshi Kale",
    author_email="sakshiskale.2405@gmail.com",
    description="Cinematic GitHub profile README generator — powered by Claude AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Techie-Sakshi24/gitghost",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "anthropic>=0.25.0",
        "requests>=2.28.0",
        "rich>=13.0.0",
        "click>=8.0.0",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "gitghost=gitghost.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="github readme generator ai claude anthropic developer-tools cli",
)