import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BFSG",
    version="1.0",
    author="Yezz123",
    author_email="yasserth19@protonmail.com",
    description="String bruteforce generator",
    long_description=long_description,
    packages=setuptools.find_packages(),
    install_requires=[
    ],
)
