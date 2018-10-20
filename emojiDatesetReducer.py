import json

out_data = ""
output = open('./output.json', 'w+')
with open('emojis.json') as json_data:
    d = json.load(json_data)
    print("[", file=output);
    for i in range(len(d) - 1):
        print("{\n\t\"keywords\": %s," % (d[i]['keywords']), file=output);
        print("\t\"unicode\": \"%s\"\n}," % (d[i]['unicode']), file=output);
    print("{\n\t\"keywords\": %s," % (d[len(d) - 1]['keywords']), file=output);
    print("\t\"unicode\": \"%s\"\n}" % (d[len(d) - 1]['unicode']), file=output);
    print("]", file=output);

