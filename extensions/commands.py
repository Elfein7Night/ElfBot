from discord.ext import commands
from utils.utils import log_event, get_prefix_for_guild_id
import random


# a simple example of a custom check for a command
def is_creator(ctx):
    return 'elfein' in ctx.author.name.lower()


class ExtraCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        log_event(f'{self.qualified_name} extension loaded')

    @commands.command(aliases=['8ball'], brief="Play a game of 8ball")
    async def _8ball(self, ctx, *, question=None):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]
        pf = get_prefix_for_guild_id(ctx.guild.id)
        await ctx.send(
            f"{ctx.author.mention}\nPlease Enter a Question After '{pf}8ball'\nFor Example: '{pf}8ball are you dumb?'"
            if question is None else
            f'{ctx.author.mention}\nQuestion: {question}\nAnswer: {random.choice(responses)}'
        )


class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        log_event(f'{self.qualified_name} extension loaded')

    @commands.command(brief="Get the bot's latency")
    async def ping(self, ctx):
        await ctx.send(f'{ctx.author.mention} latency: ({round(self.bot.latency * 1000)}ms)')

    @commands.command(brief="Clear previous messages. Can be called with a specific amount")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=2):  # default 2 - clear this clear command and the previous one in the channel
        await ctx.channel.purge(limit=amount)

    # Example of Command-Specific Error Handling:
    #
    # @clear.error  # (@command_name.error)
    # async def clear_error(self, ctx, error):
    #     pass

    # an example for a command with a custom check
    @commands.command(hidden=True)
    @commands.check(is_creator)
    async def creator(self, ctx):
        await ctx.send(f'😎 {ctx.author.mention} 😎')

    @commands.command(brief="Link the bot's source code")
    async def repo(self, ctx):
        await ctx.send('Source Code:\nhttps://github.com/Elfein7Night/ElfBot')

    @commands.command(brief="Get an invite link to join the bot to your server")
    async def invite(self, ctx):
        await ctx.send(f'{ctx.author.mention} Invite me to your server here:\nhttps://bit.ly/31cs0qz')

    @commands.command(brief="Get the number of servers the bot is moderating")
    async def deployment(self, ctx):
        await ctx.send(f'{ctx.author.mention}'
                       f' {self.bot.user.name} Is Currently Moderating {len(self.bot.guilds)} Servers')


# expected function for outside calling function 'load_extension()'
def setup(_bot):
    _bot.add_cog(AdminCommands(_bot))
    _bot.add_cog(ExtraCommands(_bot))
