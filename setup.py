import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cadence-client",
    version="0.0.1",
    author="Mohammed Firdaus",
    author_email="firdaus.halim@gmail.com",
    description="Python framework for Cadence Workflow Service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/firdaus/cadence-python",
    packages=setuptools.find_packages(exclude=["cadence.tests", "cadence.spikes"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True
)