# pyfiles
Pyfiles allows you to easily manage and download files

## Installing the module
To install the module do the following:
```sh
# Linux/macOS
python3 -m pip install py-files

# Windows
py -3 -m pip install py-files
```

## Example usage
**WARNING: not implemented, a showcase what this module will do**
```py
import pyfiles as files

file_manager = files.FileManager(path="./") # initialize file manager
file_manager.download("https://example.com/downloads/file.txt")
file_manager.showtree() # show directory tree
````
You can also use this module directly in the terminal
```sh
python3 -m pyfiles tree
```