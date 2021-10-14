import os
file = open(".xml", "r")
file_add = open(".xml", "r")
content = file.read()
# content_add = file_add.read()
content_add = "\n\nhello, everybody\n"
pos = content.find("\n")
if pos != -1:
        content = content[:pos] + content_add + content[pos:]
        file = open(".xml", "w")
        file.write(content)
        file.close()
        file_add.close()
