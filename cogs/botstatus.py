from discord.ext import commands

class StatusBot(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot started!")

def setup(client):
    client.add_cog(StatusBot(client))