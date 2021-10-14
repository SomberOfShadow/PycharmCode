from xml.dom.minidom import parseString


import requests

url = "https://arm2s10-eiffel026.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/jcat-releases/content/com/ericsson/msran/jcat/msran-jcat-extension-with-dependencies/1.8.9092/"

response = requests.get(url)
data = response.content

# xml_data = xmltodict.parse(response.content)
# print("xml data:\n", xml_data)

#将bytes转换成字符串
data = data.decode('utf-8')


dom = parseString(data)


textList = dom.getElementByTagName("text")
print("text list:", textList)
