This helps to control the website better

# Sever HTML File PATH:
/usr/share/nginx/html

# Prerequisite
- python3 are required, anaconda is recommanded
- jemdoc is required to generate the html file

# Required file(at least 5 files)
- jemdoc:	for compiling the jemdoc file(can be put at /usr/bin)
- MENU:		for controlling the sidebar
- jemdoc.css 	for css control
- deconf.conf 	for configuration control, make this easy
- NAME.jemdoc 	the source code for generating the html, here NAME = index

# Generating a webpage
- jemdoc index.jemdoc // without conf, not recommand
- jemdoc -c deconf.conf index.jemdoc // with conf file, math formula can be elegant

# Quick Start of Contents
- # jemdoc: menu{MENU}{index.html}, nofooter //for control menue and the corresponding html
- "==" to generate topic head
- "+content+" put contents in ++ to highlight

# Quick Cheatsheet for jemdoc
