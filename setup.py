import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

from uart_axi import version_str

setuptools.setup(
    name="uart_axi",
    version=version_str,
    author="Bilal Ahmed"
    author_email="bilal.ahmed@rapidsilicon.com",
    description="""\
Python module containing verilog files for UART 16550.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="git@github.com:RapidSilicon/UART_16550.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    zip_safe=False,
    packages=setuptools.find_packages(),
    package_data={
    	'ip_uart16550': ['ip_uart16550/verilog/**'],
    },
    include_package_data=True,
    project_urls={
        "Bug Tracker": "git@github.com:RapidSilicon/UART_16550.git/issues",
        "Source Code": "git@github.com:RapidSilicon/UART_16550.git",
    },
)
