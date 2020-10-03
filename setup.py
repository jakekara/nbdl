import setuptools

setuptools.setup(
    name="nbdlang-jakekara", # Replace with your own username
    version="0.0.1",
    author="Jake Kara",
    author_email="jake@jakekara.com",
    description="A notebook description language parser",
    url="https://github.com/jakekara.com/nbdl",
    packages=setuptools.find_packages(),
    install_requires=[
        "lark-parser==0.10.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    python_requires='>=3.6',
)