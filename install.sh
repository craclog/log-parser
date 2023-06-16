#!/bin/bash
set +x
LINK="/usr/local/bin/log_parser"

# Check symlink already exists
if [ -f "$LINK" ] || [ -L "$LINK" ]; then
    echo "LINK: $LINK"
    echo "Error: Symbolic link for log_parser already exists"
    ls -al "$LINK"
    exit 0
fi

# Get absolute path of this script. This is needed to make symlink
SCRIPT_PATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
TARGET="src/log_parser.py"
TARGET_ABSOLUTE_PATH="$SCRIPT_PATH/$TARGET"
if [ ! -f "$TARGET_ABSOLUTE_PATH" ]; then
    echo "log_parser path: $TARGET_ABSOLUTE_PATH"
    echo "Error: log_parser not found"
    exit 1
fi

# Make link and Check ln command executed successfully
if ! ln -fs "$TARGET_ABSOLUTE_PATH" "$LINK"; then
    echo "Error: ln command failed"
    echo "log_parser path: $TARGET_ABSOLUTE_PATH"
    echo "link path: $LINK"
    exit 1
fi

echo "log_parser installed successfully"
ls -al "$LINK"
