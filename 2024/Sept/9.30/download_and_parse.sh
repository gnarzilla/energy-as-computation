#!/bin/bash

# Simple script to download a webpage and clean the body tag
url="$1"

# Use wget to download the page and save it as page.html
wget -q -O page.html "$url"

# Call the C program to parse and clean the HTML
./parse_body page.html
