import json;
import sys;
import requests;
try:
    obj = requests.get(
        'http://rbs-g2-infobank.rnd.ki.sw.ericsson.se/infobank/rest/product/revision/CXS2010004_1/R49A132/confidence_level')
    # obj.encoding = 'utf-8'
    print("obj:", obj.text)
    print("type", type(obj))
    js = json.loads(obj.text)
    print("json length :", len(js))
    print("json type:", type(js))
    flag = 0
    for i in range(0, len(js)):
        if js[i]["confidenceLevel"]["confidenceLevelName"] == "1" and js[i]["increment"]["project"]["name"] == "ANY":
            flag += 1
    print(flag)
    print("Done!")
    if flag > 0:
        sys.exit(1);
    else:
        sys.exit(0)

except Exception as e:
    print ("[ERROR] check BBI version failed. PLS check error:")
    print (e)
    sys.exit(1)