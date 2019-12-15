import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cuteuid", # Replace with your own username
    version="1.0.1",
    author="Alex Redmon",
    author_email="alexandriadredmon@gmail.com",
    description="Generate cute UIDs, i.e. unique(ish) identifiers that are similar in appearance to UUIDs.",
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexdredmon/cuteuid",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
