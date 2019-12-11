#!/bin/bash 

Text="Copying file"
echo "Text" 

cp ~/Final_Exam/temp.cgi /usr/lib/cgi-bin/temp.cgi

Text2="Issuing +s chmod permissions"
echo "Text2"

sudo chmod +s /usr/lib/cgi-bin/temp.cgi
