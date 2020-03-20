import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="html2md-IstvanOri",
    version="0.0.1",
    author="Istvan Ori",
    author_email="ori@east1.hu",
    description="HTML to MD Converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IstvanOri/HTML2MD",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Beer License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)