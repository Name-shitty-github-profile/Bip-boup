import requests
from os import environ
guild_id: int = 995006646558396476
url: str = 'https://discord.com/api/v10'
def add_role(member_id, role_id):
  requests.put(f'{url}/guilds/{guild_id}/members/{member_id}/roles/{role_id}', headers={'authorization': 'Bot ' + environ['token']})

def rem_role(member_id, role_id):
  requests.delete(f'{url}/guilds/{guild_id}/members/{member_id}/roles/{role_id}', headers={'authorization': 'Bot ' + environ['token']})
