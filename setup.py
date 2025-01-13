from setuptools import setup, find_packages

setup(
    name="hybrid_llm_scraper",
    version="0.1.0",
    package_dir={"": "projects/hybrid_llm_scraper"},
    packages=find_packages(where="projects/hybrid_llm_scraper"),
    install_requires=[
        'requests>=2.31.0',
        'beautifulsoup4>=4.12.0',
        'selenium>=4.15.0',
        'playwright>=1.40.0',
        'pandas>=2.1.0',
        'numpy>=1.24.0',
        'transformers>=4.35.0',
        'torch>=2.1.0',
        'scikit-learn>=1.3.0',
        'mlflow>=2.8.0',
    ],
    python_requires='>=3.9',
) 