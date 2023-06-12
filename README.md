# log-parser
This python program helps analyzing any log files that you want.
After registering the required string patterns in the pattern.yaml file,
running this program will generate the parsed output of each pattern.

# Install
```sh
python3 -m pip install -r requirements.txt
```

# Run

```sh
# Example
python3 src/log_parser.py --file test/data/sample.log --out test/data --verbose
```

# Run unittest
```sh
python3 -m unittest discover
```