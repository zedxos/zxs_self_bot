import os, discord, re, json, requests, asyncio
from discord_webhook import DiscordWebhook, DiscordEmbed
TOKEN= ""
ZXS_CONDO_WEBHOOK= ""
CONDO_CLUB_WEBHOOK= ""
ORACLE_CONDO_WEBHOOK= ""
class zxs_client(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.channel.id == 996226426741194852:
                try:
                        # _gate_way = requests.get(f"https://zxscondos.repl.co/send_sniped_condo?_auth=/g[]xv&_link={message.content}&_guild={message.guild.name}")
                        _link = message.content
                        _condo_link = re.findall(r'(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?', _link)
                        # print(json.dumps(_condo_link[0][1]))
                        if json.dumps(_condo_link[0][1]).__contains__("www.roblox.com"):
                            if json.dumps(_condo_link[0][2]).split("/")[2]:
                                __get_game__ = requests.get(f"https://api.roblox.com/universes/get-universe-containing-place?placeid={json.dumps(_condo_link[0][2]).split('/')[2]}").text
                                __get_id__ = json.loads(__get_game__)
                                _checker = requests.get(f"https://games.roblox.com/v1/games/multiget-playability-status?universeIds={__get_id__['UniverseId']}")
                                # print(json.loads(_checker.text)[0]["playabilityStatus"])
                                if json.loads(_checker.text)[0]["playabilityStatus"] == "Playable" or "GuestProbihited":
                                    # print("https://www.roblox.com" + json.dumps(_condo_link[0][2]).replace('"', ""))
                                    _get_info = f"https://games.roblox.com/v1/games?universeIds={__get_id__['UniverseId']}"
                                    __get_info__ = requests.get(url=_get_info).text
                                    __get_game_info__ = json.loads(__get_info__)
                                    _current_playing = __get_game_info__["data"][0]["playing"]
                                    _max_players = __get_game_info__["data"][0]["maxPlayers"]
                                    _avatar_type = __get_game_info__["data"][0]["universeAvatarType"]
                                    
                                    _link_condo = "https://www.roblox.com" + json.dumps(_condo_link[0][2]).replace('"', "")
                                    _zxs_condo_webhook = DiscordWebhook(url=ZXS_CONDO_WEBHOOK)#, content="https://www.roblox.com" + json.dumps(_condo_link[0][2]).replace('"', ""))
                                    _embed = DiscordEmbed(title='Sniped a condo!', color='ff0000', description=f":telescope: ZxS Condos :crescent_moon: \n `Sent in`: *{message.guild.name}* \n `Current Players`: *{_current_playing}* \n `Max Players`: *{_max_players}* \n `Avatar Type`: *{_avatar_type}* \n `Link`: *{_link_condo}*")
                                    _embed.set_timestamp()
                                    _zxs_condo_webhook.add_embed(_embed)
                                    _zxs_condo_webhook.execute()
                                    """
                                        [[
                                            Condo Club Webhook
                                        ]]
                                    """
                                    _condo_club_webhook = DiscordWebhook(url=CONDO_CLUB_WEBHOOK)#, content="https://www.roblox.com" + json.dumps(_condo_link[0][2]).replace('"', ""))
                                    """
                                    _embed.add_embed_field(name='Sent in', value=message.guild.name)
                                    _embed.add_embed_field(name='Current Players', value=_current_playing)
                                    _embed.add_embed_field(name='Max Players', value=_max_players)
                                    _embed.add_embed_field(name='Avatar Type', value=_avatar_type)
                                    _embed.add_embed_field(name='Link', value="https://www.roblox.com" + json.dumps(_condo_link[0][2]).replace('"', ""))
                                    """
                                    _condo_club_webhook.add_embed(_embed)
                                    _condo_club_webhook.execute()
                                    """
                                        [[
                                            Oracle Condo Webhook
                                        ]]
                                    """
                                    _oracle_condo_webhook = DiscordWebhook(url=ORACLE_CONDO_WEBHOOK)#, content="https://www.roblox.com" + json.dumps(_condo_link[0][2]).replace('"', ""))
                                    _oracle_condo_webhook.add_embed(_embed)
                                    _oracle_condo_webhook.execute()
                                    await asyncio.sleep(15)
                                    """
                                    data = {
                                    }

                                    #https://discordapp.com/developers/docs/resources/channel#embed-object
                                    _link_condo = "https://www.roblox.com" + json.dumps(_condo_link[0][2]).replace('"', "")
                                    data["embeds"] = [
                                        {
                                    
                                            "color": "ff0000",
                                            "description" : f":telescope: ZxS Condos :crescent_moon: \n `Sent in`: *{message.guild.name}* \n `Current Players`: *{_current_playing}* \n `Max Players`: *{_max_players}* \n `Avatar Type`: *{_avatar_type}* \n `Link`: *{_link_condo}*"
                                        }
                                    ]

                                    _zxs_condo_webhook = requests.post(ZXS_CONDO_WEBHOOK, json = data)

                                    try:
                                        _zxs_condo_webhook.raise_for_status()
                                    except requests.exceptions.HTTPError as err:
                                        print(err)
                                        await asyncio.sleep(30)
                                    else:
                                        print("Payload delivered successfully, code {}.".format(_zxs_condo_webhook.status_code))
                                        """
                                else:
                                    pass
                except:
                    pass

        if message.channel.id == 957113159284576286:
                try:
                        _link = message.content
                        _condo_link = re.findall(r'(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?', _link)
                        if json.dumps(_condo_link[0][1]).__contains__("www.roblox.com"):
                            if json.dumps(_condo_link[0][2]).split("/")[2]:
                                __get_game__ = requests.get(f"https://api.roblox.com/universes/get-universe-containing-place?placeid={json.dumps(_condo_link[0][2]).split('/')[2]}").text
                                __get_id__ = json.loads(__get_game__)
                                _checker = requests.get(f"https://games.roblox.com/v1/games/multiget-playability-status?universeIds={__get_id__['UniverseId']}")
                                # print(json.loads(_checker.text)[0]["playabilityStatus"])
                                if json.loads(_checker.text)[0]["playabilityStatus"] == "Playable" or "GuestProbihited":
                                    # print("https://www.roblox.com" + json.dumps(_condo_link[0][2]).replace('"', ""))
                                    _get_info = f"https://games.roblox.com/v1/games?universeIds={__get_id__['UniverseId']}"
                                    __get_info__ = requests.get(url=_get_info).text
                                    __get_game_info__ = json.loads(__get_info__)
                                    _current_playing = __get_game_info__["data"][0]["playing"]
                                    _max_players = __get_game_info__["data"][0]["maxPlayers"]
                                    _avatar_type = __get_game_info__["data"][0]["universeAvatarType"]
                                    
                                    _link_condo = "https://www.roblox.com" + json.dumps(_condo_link[0][2]).replace('"', "")
                                    _zxs_condo_webhook = DiscordWebhook(url=ZXS_CONDO_WEBHOOK)#, content="https://www.roblox.com" + json.dumps(_condo_link[0][2]).replace('"', ""))
                                    _embed = DiscordEmbed(title='Sniped a condo!', color='ff0000', description=f":telescope: ZxS Condos :crescent_moon: \n `Sent in`: *{message.guild.name}* \n `Current Players`: *{_current_playing}* \n `Max Players`: *{_max_players}* \n `Avatar Type`: *{_avatar_type}* \n `Link`: *{_link_condo}*")
                                    _embed.set_timestamp()
                                    _zxs_condo_webhook.add_embed(_embed)
                                    _zxs_condo_webhook.execute()
                                    """
                                        [[
                                            Condo Club Webhook
                                        ]]
                                    """
                                    _condo_club_webhook = DiscordWebhook(url=CONDO_CLUB_WEBHOOK)#, content="https://www.roblox.com" + json.dumps(_condo_link[0][2]).replace('"', ""))
                                    _condo_club_webhook.add_embed(_embed)
                                    _condo_club_webhook.execute()
                                    """
                                        [[
                                            Oracle Condo Webhook
                                        ]]
                                    """
                                    _oracle_condo_webhook = DiscordWebhook(url=ORACLE_CONDO_WEBHOOK)#, content="https://www.roblox.com" + json.dumps(_condo_link[0][2]).replace('"', ""))
                                    _oracle_embed = DiscordEmbed(title='Sniped a condo!', color='ff0000', description=f":telescope: Oracle Condos :crescent_moon: \n `Sent in`: *{message.guild.name}* \n `Current Players`: *{_current_playing}* \n `Max Players`: *{_max_players}* \n `Avatar Type`: *{_avatar_type}* \n `Link`: *{_link_condo}*")
                                    _oracle_embed.set_timestamp()
                                    _oracle_condo_webhook.add_embed(_oracle_embed)
                                    _oracle_condo_webhook.execute()
                                    await asyncio.sleep(15)
                                else:
                                    pass
                except:
                    pass

zxs = zxs_client()
zxs.run(TOKEN)

