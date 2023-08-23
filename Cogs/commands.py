import discord
from discord.ext import commands
from calculator import Calculator


class View(discord.ui.View):
    def __init__(self, calculator: Calculator, bot):
        super().__init__(
            timeout=None
        )
        self.calculator=calculator
        self.bot=bot


    @discord.ui.button(label="(", row=0, style=discord.ButtonStyle.primary)
    async def callback_open_bracket(self, button, interaction):
        calcu=await self.calculator.appead("(")
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="🧮｜計數機",
            description=f"```{calcu} ```"
        )
        await interaction.response.edit_message(
            embed=embed
        )


    @discord.ui.button(label=")", row=0, style=discord.ButtonStyle.primary)
    async def callback_close_bracket(self, button, interaction):
        calcu=await self.calculator.appead(")")
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="🧮｜計數機",
            description=f"```{calcu} ```"
        )
        await interaction.response.edit_message(
            embed=embed
        )


    @discord.ui.button(label="%", row=0, style=discord.ButtonStyle.primary)
    async def callback_percentage(self, button, interaction):
        calcu=await self.calculator.appead("/100")
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="🧮｜計數機",
            description=f"```{calcu} ```"
        )
        await interaction.response.edit_message(
            embed=embed
        )


    @discord.ui.button(label="C", row=0, style=discord.ButtonStyle.danger)
    async def callback_del(self, button, interaction):
        if "+" not in self.calaulator.calcu and "-" not in self.calaulator.calcu and "*" not in self.calaulator.calcu and "/" not in self.calaulator.calcu:
            self.calculator.calcu=""
            calcu=""
        else:
            calcu=await self.calculator.delete()
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="🧮｜計數機",
            description=f"```{calcu} ```"
        )
        await interaction.response.edit_message(
            embed=embed
        )


    @discord.ui.button(label="7", row=1, style=discord.ButtonStyle.secondary)
    async def callback_7(self, button, interaction):
        calcu=await self.calculator.appead("7")
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="🧮｜計數機",
            description=f"```{calcu} ```"
        )
        await interaction.response.edit_message(
            embed=embed
        )

    
    @discord.ui.button(label="8", row=1, style=discord.ButtonStyle.secondary)
    async def callback_8(self, button, interaction):
        calcu=await self.calculator.appead("8")
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="🧮｜計數機",
            description=f"```{calcu} ```"
        )
        await interaction.response.edit_message(
            embed=embed
        )
        

    @discord.ui.button(label="9", row=1, style=discord.ButtonStyle.secondary)
    async def callback_9(self, button, interaction):
        calcu=await self.calculator.appead("9")
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="🧮｜計數機",
            description=f"```{calcu} ```"
        )
        await interaction.response.edit_message(
            embed=embed
        )
        

    @discord.ui.button(label="÷", row=1, style=discord.ButtonStyle.primary)
    async def callback_divide(self, button, interaction):
        calcu=await self.calculator.appead("/")
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="🧮｜計數機",
            description=f"```{calcu} ```"
        )
        await interaction.response.edit_message(
            embed=embed
        )


    @discord.ui.button(label="4", row=2, style=discord.ButtonStyle.secondary)
    async def callback_4(self, button, interaction):
        calcu=await self.calculator.appead("4")
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="🧮｜計數機",
            description=f"```{calcu} ```"
        )
        await interaction.response.edit_message(
            embed=embed
        )


    @discord.ui.button(label="5", row=2, style=discord.ButtonStyle.secondary)
    async def callback_5(self, button, interaction):
        calcu=await self.calculator.appead("5")
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="🧮｜計數機",
            description=f"```{calcu} ```"
        )
        await interaction.response.edit_message(
            embed=embed
        )


    @discord.ui.button(label="6", row=2, style=discord.ButtonStyle.secondary)
    async def callback_6(self, button, interaction):
        calcu=await self.calculator.appead("6")
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="🧮｜計數機",
            description=f"```{calcu} ```"
        )
        await interaction.response.edit_message(
            embed=embed
        )


    @discord.ui.button(label="×", row=2, style=discord.ButtonStyle.primary)
    async def callback_multiply(self, button, interaction):
        calcu=await self.calculator.appead("*")
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="🧮｜計數機",
            description=f"```{calcu} ```"
        )
        await interaction.response.edit_message(
            embed=embed
        )


    @discord.ui.button(label="1", row=3, style=discord.ButtonStyle.secondary)
    async def callback_1(self, button, interaction):
        calcu=await self.calculator.appead("1")
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="🧮｜計數機",
            description=f"```{calcu} ```"
        )
        await interaction.response.edit_message(
            embed=embed
        )


    @discord.ui.button(label="2", row=3, style=discord.ButtonStyle.secondary)
    async def callback_2(self, button, interaction):
        calcu=await self.calculator.appead("2")
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="🧮｜計數機",
            description=f"```{calcu} ```"
        )
        await interaction.response.edit_message(
            embed=embed
        )


    @discord.ui.button(label="3", row=3, style=discord.ButtonStyle.secondary)
    async def callback_3(self, button, interaction):
        calcu=await self.calculator.appead("3")
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="🧮｜計數機",
            description=f"```{calcu} ```"
        )
        await interaction.response.edit_message(
            embed=embed
        )


    @discord.ui.button(label="-", row=3, style=discord.ButtonStyle.primary)
    async def callback_reduce(self, button, interaction):
        calcu=await self.calculator.appead("-")
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="🧮｜計數機",
            description=f"```{calcu} ```"
        )
        await interaction.response.edit_message(
            embed=embed
        )


    @discord.ui.button(label=".", row=4, style=discord.ButtonStyle.primary)
    async def callback_point(self, button, interaction):
        calcu=await self.calculator.appead(".")
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="🧮｜計數機",
            description=f"```{calcu} ```"
        )
        await interaction.response.edit_message(
            embed=embed
        )


    @discord.ui.button(label="0", row=4, style=discord.ButtonStyle.secondary)
    async def callback_0(self, button, interaction):
        calcu=await self.calculator.appead("0")
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="🧮｜計數機",
            description=f"```{calcu} ```"
        )
        await interaction.response.edit_message(
            embed=embed
        )


    @discord.ui.button(label="=", row=4, style=discord.ButtonStyle.success)
    async def callback_(self, button, interaction):
        calcu=await self.calculator.equal_to()
        if calcu == "ERROR!":
            self.calculator.calcu=""
        else:
            self.calculator.calcu=calcu
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="🧮｜計數機",
            description=f"```{calcu} ```"
        )
        await interaction.response.edit_message(
            embed=embed
        )


    @discord.ui.button(label="+", row=4, style=discord.ButtonStyle.primary)
    async def callback_plus(self, button, interaction):
        calcu=await self.calculator.appead("+")
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="🧮｜計數機",
            description=f"```{calcu} ```"
        )
        await interaction.response.edit_message(
            embed=embed
        )


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.slash_command(name="help", description="指令列表")
    async def help(self, ctx):
        await ctx.defer()
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="指令列表",
            description=f"[此指令會顯示機械人所有指令!](https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/)"
        )
        embed.add_field(name="</calculator:1234567890>", value="計數機", inline=True)
        await ctx.respond(
            embed=embed
        )


    @commands.slash_command(name="calculator", description="計數機")
    async def calculator(self, ctx):
        await ctx.defer()
        calculator=Calculator()
        embed=discord.Embed(
            color=discord.Colour.embed_background(),
            title="🧮｜計數機",
            description="``` ```"
        )
        await ctx.respond(
            embed=embed, 
            view=View(calculator=calculator, bot=self.bot)
        )
        

def setup(bot):
    bot.add_cog(Commands(bot))
