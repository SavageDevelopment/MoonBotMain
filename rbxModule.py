import requests

def rbx_getId(rbxUsr):
  getResp = requests.get(f'https://api.roblox.com/users/get-by-username?username={rbxUsr}')
  resp = getResp.json()
  return(resp['Id'])


def rbx_getGroupRoles(rbxId):
  getResp = requests.get(f'https://groups.roblox.com/v2/users/{rbxId}/groups/roles')
  resp = getResp.json()
  found = False
  check = 0
  while found == False:
    try:
      if resp['data'][check]['group']['name'] == "·Moon's Restaurant·":
        found = True
        return(resp['data'][check]['role']['name'])
    except:
      return('Username not Found: Please join the group!')

    else:
      check = check + 1

def set_role(rbxId, rankId):
  getResp = requests.get(f'https://ranking-bot.savagemusicyt.repl.co/ranker?userid={rbxId}&rank={rankId}')
