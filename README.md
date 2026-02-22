# YAWS (Yet Another Web-scraper)
A versatile CLI web scaper tool written in python 

# Rationale
This app is beign made with the express intent of learning how to better use python to interact
both with the web and the linux file system, and a way for me as a student to gather data independently.
There is no malicious intent at play here and i do not condone the use of this software for illegal gathering
of information.

# Functionality
the app will be divided into a couple of different modes:
* Mode 1 - parses the HTML of a webpage and allows the user to write it's contents to a HTML file
* Mode 2 - parses specific HTML tags and allows the user to write it's contents to a text file 
* TUI - A simple tex based interface will appear guiding the user through the process
* Arguments - a list of arguments will be displayed if the app is run with the ```--help``` command
```
usage: yaws [-h] [--url URL] [--mode {raw,tag}] [--tag TAG]

Yet Another Web-Scraper | A tool by Pablo Loschi
(Mechaspirit1)

options:
  -h, --help        show this help message and exit
  --url URL         URL to be scraped (must contain https://)
  --mode {raw,tag}  Scrape mode
  --tag TAG         HTML tag to be scraped, used with tag mode - (<a> tags will fetch only the
                    contents of href)
```

# Installation
* Install dependencies - ```pip install requests bs4```
* Clone this repository and open directory
* Make script executable ```chmod +x yaws.py```
* Copy or move it to a $PATH directory (```cp yaws.py /usr/your/directory```) or (```mv yaws.py /usr/your/directory```)

# Notes
- Files will always be generated at the current working directory.
- Previous issue concerning file nomenclature is fixed, files now will be named according to the current date and time

