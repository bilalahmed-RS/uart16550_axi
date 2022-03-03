# uart_axi

Non-Python  files needed for the IP UART 16550 packaged into a Python module so they can be used with Python libraries and tools.

This is useful for usage with tools like [LiteX](https://github.com/enjoy-digital/litex.git).

The data files can be found under the Python module `uart_axi`. The
`uart_axi.data_location` value can be used to find the files on the file
system.

Example of getting the data file directly;
```python
import uart_axi

my_data_file = "abc.txt"

with open(os.path.join(uart_axi.data_location, my_data_file)) as f:
    print(f.read())
```

Example of getting the data file using `litex.data.find` API;
```python
from uart_axi import data_file

my_data_file = "abc.txt"

with open(data_file(my_data_file)) as f:
    print(f.read())
```


The data files come from [UART IP](https://github.com/RapidSilicon/UART_16550)
and are imported using `git subtrees` to the directory
[uart_axi/verilog](uart_axi/verilog).


## Installing from git repository

## Manually

You can install the package manually, however this is **not** recommended.

```
git clone https://github.com/RapidSilicon/UART_16550.git
cd pythondata-ip_uart16550
sudo python setup.py install
```
