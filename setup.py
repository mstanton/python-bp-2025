from setuptools import setup, find_packages

setup(
    name="python-bp-2025",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    python_requires=">=3.8",
) 