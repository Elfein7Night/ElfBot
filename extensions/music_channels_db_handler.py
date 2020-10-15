import json
from discord.ext import commands
from utils.utils import log_event, db, MUSIC_CH_DB_NAME


def remove_server(gid):
    if db.get(MUSIC_CH_DB_NAME) is not None:
        music_channels = json.loads(db.get(MUSIC_CH_DB_NAME).decode('utf-8'))
        try:
            music_channels.pop(str(gid))
            db.set(MUSIC_CH_DB_NAME, json.dumps(music_channels))
        except KeyError:
            pass


class MusicChannelsDBHandler(commands.Cog):
    def __init__(self, _bot):
        self.bot = _bot

    @commands.Cog.listener()
    async def on_ready(self):
        log_event(f'{self.qualified_name} extension loaded')

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        remove_server(guild.id)
        log_event(f"left the server '{guild}'")

    @commands.command(brief="Set a text channel to a music spam channel")
    @commands.has_permissions(administrator=True)
    async def setmusic(self, ctx):
        if db.get(MUSIC_CH_DB_NAME) is None:
            music_channels = {}
        else:
            music_channels = json.loads(db.get(MUSIC_CH_DB_NAME).decode('utf-8'))

        music_channels[str(ctx.guild.id)] = ctx.channel.id
        db.set(MUSIC_CH_DB_NAME, json.dumps(music_channels))

        message = f"{ctx.channel.name} is now set as the music spam channel for the server '{ctx.guild}'"
        log_event(message)
        await ctx.send(f'{ctx.author.mention} {message}')

    @commands.command(brief="Delete the music spam setting for a server")
    @commands.has_permissions(administrator=True)
    async def delmusic(self, ctx):
        remove_server(ctx.guild.id)
        message = f"Music spam settings for the server '{ctx.guild}' have been deleted"
        log_event(message)
        await ctx.send(f'{ctx.author.mention} {message}')


# expected function for outside calling function 'load_extension()'
def setup(_bot):
    _bot.add_cog(MusicChannelsDBHandler(_bot))
