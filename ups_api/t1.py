import urllib.request, urllib.error


combined_data = ""

with open("AccessRequest.xml") as f:
    read_data = f.read()
    with open("RatingServiceSelectionRequest.xml") as g:
        read_data_2 = g.read()

        combined_data = read_data + read_data_2

# print(data)

try:
    httpresq = urllib.request.Request(url="https://wwwcie.ups.com/ups.app/xml/Rate", data=combined_data.encode('utf_8'), headers={'Content-Type': 'application/x-www-form-urlencoded'})
    response = urllib.request.urlopen(httpresq)
    return_values = response.read()
    print(type(return_values))
    with open("response.xml", "wb") as r:
        r.write(return_values)
    print(return_values)
except urllib.error.URLError as e:
    error = "urllib.error.URLError exception was raised: %s" % e
    print(error)