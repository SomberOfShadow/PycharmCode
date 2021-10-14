import argparse

import requests
from bs4 import BeautifulSoup
import re
import json
from elasticsearch import Elasticsearch

parser = argparse.ArgumentParser(description='The script is to collect specific mje version jar size and send to '
                                             'elasticsearch.')
parser.add_argument('--mjeVersion', '-m', default="", type=str,
                    help='Specific mje version')

args = parser.parse_args()
mjeVersion = args.mjeVersion

# old url before E2C migration
# mjeVersion = "1.8.9092"
# url = "https://arm2s10-eiffel026.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/jcat-releases/content" \
#       "/com/ericsson/msran/jcat/msran-jcat-extension-with-dependencies/" + mjeVersion

# new url after E2C migration
mjeVersion = "1.8.9194"
url = "https://arm2s10-eiffel026.eiffel.gic.ericsson.se:8443/nexus/service/local/repositories/mje_releases/content" \
      "/com/ericsson/msran/jcat/msran-jcat-extension-with-dependencies/" + mjeVersion
indexName = "send-mje-version-size-test4"

type = "type"

mappingsWithType = {
    'type':{
        'properties' : {
                'lastModified':{'type':'text'},
			    'mjeVersion':{'type':'text' },
			    'sizeOnDisk':{'type':'long' }
        }
    }
}

mappings = {
  'properties' : {
        'lastModified':{'type':'text'},
		'mjeVersion':{'type':'text' },
		'sizeOnDisk':{'type':'long' }
        }
}


es = Elasticsearch(
    ['mje-es.sero.wh.rnd.internal.ericsson.com'],
    http_auth=('esuser', 'Z8A6v9xG1oS3ufU'),
    scheme="https",
    port=443
)

def getStringFromUrl(url):
    try:
        print("Start to get string from url!")
        response = requests.get(url)
        data = response.content
        # convert bytes to string
        data = data.decode('utf-8')
        # print("data:\n", data)
    except:
        print("Fail to get string from url for mje version: ", mjeVersion)

    print("Succeed to get String from url for mje version: ", mjeVersion)
    return data


def getJsonData(data):
    # convert string to xml
    soup = BeautifulSoup(data, "lxml-xml")

    textAll = soup.findAll("text")
    sizeOnDiskAll = soup.findAll("sizeOnDisk")
    lastModifiedAll = soup.findAll("lastModified")

    # match jar and record location
    flag = 0
    for text in textAll:
        if re.match("msran-jcat-extension-with-dependencies-1.8.\d\d\d\d.jar", text.text):
            break
        flag += 1

    # print("index: ", flag)
    # print("sizeOnDisk:", sizeOnDiskAll[flag].text)
    # print("lastModified:", lastModifiedAll[flag].text)
    sizeOnDisk = sizeOnDiskAll[flag].text
    lastModified = lastModifiedAll[flag].text

    # load as json object
    jsonData = json.dumps({"mjeVersion": mjeVersion, "sizeOnDisk": int(sizeOnDisk), "lastModified": lastModified},
                          sort_keys=True, indent=4, separators=(',', ': '))
    # print("json data:\n", jsonData)
    return jsonData


def send(jsonData):
    # send json data to elasticsearch


    # body is the data need to send
    try:
        # es.index(index="send-mje-version-size-test", body=jsonData)
        # Specific id to avoid data duplication and each mje version should have a unique id
        exists = es.indices.exists(index=indexName)
        print("Start to create index:", indexName)
        if not exists:
            create = es.indices.create(index=indexName, include_type_name=True)
            # print("create:", create)
            if create.get("acknowledged"):
                print("Succeed to create index:", indexName)
                print("Start to put mappings for index:", indexName)
                # if include_type_name=True, mappings must be with type and must specific doc_type
                # if no include_type_name=True , mappings with type and specific doc_type are both optional
                # mapping = es.indices.put_mapping(index=indexName, body=mappings, include_type_name=True, doc_type=type)

                mapping = es.indices.put_mapping(index=indexName, body=mappings,include_type_name=True)
                # print("mapping:", mapping)
                if mapping.get("acknowledged"):
                    print("Succeed to put mappings!")
                    print("Start to send json data!")
                    es.index(index=indexName, body=jsonData, id=mjeVersion)
                    print("Succeed to send json data!")

                # print("Start to send json data!")
                # es.index(index=indexName, body=jsonData, id=mjeVersion)
                # print("Succeed to send json data!")

        else:
            print(indexName + " already exists!")
            print("Start to send json data!")
            es.index(index=indexName, body=jsonData, id=mjeVersion)
            print("Succeed to send json data!")

    except:
        print("Fail to send json data!")


if __name__ == '__main__':
    data = getStringFromUrl(url)
    jsonData = getJsonData(data)
    send(jsonData)
