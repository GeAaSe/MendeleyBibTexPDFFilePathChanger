# -*- coding: utf-8 -*-

import os
import re
filename='PathToBibTexFile.bib'
   
    
with open(filename, "r", encoding="utf-8") as f:
    read_data = f.readlines()
    
for line in range(len(read_data)):
    Suche=read_data[line]
    if re.search("file = {", Suche):
	Suche=Suche.replace("{:", "{")
	Suche=Suche.replace("\:/", ":/")
        r = os.path.normpath("\\")
        Suche=Suche.replace('/', r )
        Suche=Suche.replace(':pdf', "" )
        read_data[line]=Suche.replace(':PDF', "" )
        
with open(filename, "w", encoding="utf-8") as f:
    for Line in read_data:
        f.write(Line)

