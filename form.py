import webbrowser

webbrowser.open('D:\Python\Python_pgm\GFG.html')
f = open('D:\Python\Python_pgm\GFG.html', 'w')

# the html code which will go in the file GFG.html
html_template = ("<html>\n"
                 "<head>\n"
                 "<title>Title</title>\n"
                 "</head>\n"
                 "<body>\n"
                 "<h2>Welcome To GFG</h2>\n"
                 "\n"
                 "<p>Default code has been loaded into the Editor.</p>\n"
                 "\n"
                 "</body>\n"
                 "</html>\n")
# writing the code into the file
f.write(html_template)

# close the file
f.close()