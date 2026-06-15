# Internet speed tester
# Python program to test
# internet speed

import speedtest


st = speedtest.Speedtest()

print(st.download())

print(st.upload())


servernames = []

st.get_servers(servernames)

print(st.results.ping)
