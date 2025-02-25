import disnake
from disnake.ext import commands


async def test_autocomp(inter, string):
    return ["XD", ":D", ":)", ":|", ":("]


class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.slash_command()
    async def hello(self, inter: disnake.AppCmdInter):
        await inter.response.send_message("Hello world!")

    @commands.slash_command()
    async def auto(self, inter: disnake.AppCmdInter, mood: str):
        """
        Has an autocomplete option.

        Parameters
        ----------
        mood: Dude
        """
        await inter.send(mood)

    @auto.autocomplete("mood")
    async def test_autocomp(self, inter: disnake.AppCmdInter, string: str):
        return ["XD", ":D", ":)", ":|", ":("]

    @commands.slash_command()
    @commands.guild_permissions(768247229840359465, roles={815866581233041428: False})
    async def alt_auto(
        self,
        inter: disnake.AppCmdInter,
        mood: str = commands.Param(autocomp=test_autocomp),
    ):
        await inter.send(mood)

    @commands.slash_command()
    async def current(
        self,
        inter: disnake.GuildCommandInteraction,
        user: disnake.Member = commands.Param(commands.Current),
        channel: disnake.abc.GuildChannel = commands.Param(commands.Current, desc="channel"),
        guild: disnake.Guild = commands.Current,
    ):
        await inter.send(f"user: {user.mention} channel: {channel.mention} guild: {guild.name}")


def setup(bot):
    bot.add_cog(SlashCommands(bot))
    print(f"> Extension {__name__} is ready\n")
