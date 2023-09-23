import requests
y = 0
def GetProxies():
    with open('proxies.txt', 'r') as temp_file:
        proxies = [line.rstrip('\n') for line in temp_file]
    return proxies

link = input('Discord Invite Link: ')
amount = input('Number of users to join: ')
amount = int(amount)
if len(link) > 6:
    link = link[19:]
apilink = "https://discordapp.com/api/v9/invite/" + str(link)

print (link)

with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            if y == amount:
                print("All valid tokens have joined!")
            else:
                try:
                    token = x.rstrip()
                    headers={
                        'Authorization': token
                        }
                    requests.post(apilink, headers=headers, proxies={"https://': 'http://" + GetProxies()})
                    y = y + 1
                    print(f"==>  joined {x} to {link}")
                except Exception as e:
                    print(f"==>  Error with {x}, full error is: {e")
        
