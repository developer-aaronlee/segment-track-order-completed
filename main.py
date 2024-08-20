import csv
import json
import requests

url = 'https://api.segment.io/v1/track'
API_KEY = 'Basic api_key'
headers = {
    'Content-Type': 'application/json',
    'Authorization': API_KEY
}

with open('batch_test_17.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
    for row in spamreader:
        if len(row) == 0:
            continue
        temp = row[0].split(",")

        item_count = len(temp) // 4

        products = []
        if temp[0] == "userId":
            continue

        for x in range(item_count): #x : 0,1,2,3
            dic = {}
            if temp[2+(4*x)] != "":
                dic["sku"] = temp[2+(4*x)]
            if temp[3+(4*x)] != "":
                dic["presentment_currency"] = temp[3+(4*x)]
            if temp[4+(4*x)] != "":
                dic["price"] = float(temp[4+(4*x)])
            if temp[5+(4*x)] != "":
                dic["quantity"] = int(temp[5+(4*x)])

            if len(dic) == 0:
                continue

            products.append(dic)

        new = {
               "userId": temp[0],
               "event": "Order Completed",
               "properties": {
                   "products": products
               },
               "timestamp": temp[1]
           }

        body = json.dumps(new)
        print(body)
        response = requests.post(url, data=body, headers=headers)
        print(response)


        # for x in range(item_count): #x : 0,1,2,3
        #     dic = {}
        #     if temp[1+(4*x)] != "":
        #         dic["sku"] = temp[1+(4*x)]
        #     if temp[2+(4*x)] != "":
        #         dic["presentment_currency"] = temp[2+(4*x)]
        #     if temp[3+(4*x)] != "":
        #         dic["price"] = float(temp[3+(4*x)])
        #     if temp[4+(4*x)] != "":
        #         dic["quantity"] = int(temp[4+(4*x)])
        #     products.append(dic)

        # new = {
        #        "userId": temp[0],
        #        "event": "Order Completed",
        #        "properties": {
        #            "products": products
        #        },
        #        "timestamp": temp[-1]
        #    }
