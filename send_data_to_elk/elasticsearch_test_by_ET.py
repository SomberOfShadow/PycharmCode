import requests
import xml.etree.ElementTree as ET



url = "https://arm2s10-eiffel026.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/jcat-releases/content/com/ericsson/msran/jcat/msran-jcat-extension-with-dependencies/1.8.9092/"

response = requests.get(url)
data = response.content

# xml_data = xmltodict.parse(response.content)
# print("xml data:\n", xml_data)

#将bytes转换成字符串

data = data.decode('utf-8')

# head = "<?xml version=\"1.0\"?\\>"
# content = (head + data)
tree = ET.fromstring(data)
print("tree text:", tree.text)
#print(tree.tag, ":", tree.attrib)

# for child in tree:
#     print (child.tag, child.attrib)
#
# contentItemAll = tree.findall("text")
# print("type: ", type(contentItemAll))
# print("length: ", len(contentItemAll))








