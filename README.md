# log-parser
This python program helps analyzing any log files that you want.
After registering the required string patterns in the pattern.yaml file,
running this program will generate the parsed output of each pattern.

# Install
```sh
# Install python packages
$ python3 -m pip install -r requirements.txt

# Make symbolic link to /usr/local/bin
$ sudo ./install.sh
```

# Run

```sh
# Example
$ log_parser --file test/data/sample.log --out test/data --verbose
```

# Run unittest
```sh
$ cd log-parser
$ python3 -m unittest discover
```