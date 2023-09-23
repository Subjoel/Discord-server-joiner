import requests
def GetProxies():
    with open('proxies.txt', 'r') as temp_file:
        proxies = [line.rstrip('\n') for line in temp_file]
    return proxies

link = input('Discord Invite Link: ')
if len(link) > 6:
    link = link[19:]
apilink = "https://discordapp.com/api/v9/invite/" + str(link)

print (link)

with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            requests.post(apilink, headers=headers, proxies={"https://': 'http://" + GetProxies()})
        print ("All valid tokens have joined!")
