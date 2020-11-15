import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="skingrabber",
    version="0.1.1",
    author="MakufonSkifto",
    author_email="emirsurmen@gmail.com",
    license="MIT",
    description="A Python 3 wrapper for the Minecraft Skin API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MakufonSkifto/skingrabber",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
