#!/bin/bash
try() {
    "$@" || { local line="$LINENO"; echo "Failed at $line: $BASH_COMMAND"; exit 1; }
}

catch() {
    local line="$1"
    local message="$2"
    echo "Failed at $line: $message"
    exit 1
}