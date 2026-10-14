import os
import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

class MyBot(discord.Client):
    def __init__(self, *, intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        synced = await self.tree.sync()
        print(f"Synced {len(synced)} slash command(s)")

client = MyBot(intents=intents)

class LetterSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="Open when you're anxious",
                value="anxious",
                emoji="💗"
            ),
            discord.SelectOption(
                label="Open when you miss me",
                value="miss_me",
                emoji="😔"
            ),
            discord.SelectOption(
                label="Open when you're having a bad day",
                value="bad_day",
                emoji="🌧️"
            )
        ]

        super().__init__(
            placeholder="Choose a letter to open... ♡",
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        letters = {
            "anxious": (
                "💗 Open me when you're anxious",
                "Wether it's about us, or school, or literally anything, I'm here for you.\n\n"
                "Even if not physically, I'm always in your heart.\n\n"
                "Take a deep breath, everything will be okay."
            ),
            "miss_me": (
                "😔 Open me when you miss me",
                "I wish I could be with you right now.\n\n"
                "I love you from your head to your toes\n\n"
                "I can't wait to see you next\n\n"
                "Even when we're apart, you're always in my heart (ewww it's so cheesy)"
            ),
            "bad_day": (
                "🌧️ Open me when you're having a bad day",
                "I'm sorry you've had a bad day, get some rest, love.\n\n"
                "One bad day doesn't define you. Always remember, I love you."
            )
        }

        title, message = letters[self.values[0]]

        embed = discord.Embed(
            title=title,
            description=message,
            color=discord.Color.from_rgb(255, 182, 193)
        )

        embed.set_footer(text="Made with love ♡")

        await interaction.response.send_message(
            embed=embed,
            view=BackToLettersView(),
            ephemeral=True
        )

    async def on_error(self, interaction, error, item):
        print(f"Select menu error: {error}")

class LetterMenuView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=180)
        self.add_item(LetterSelect())

class BackToLettersView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=180)

    @discord.ui.button(
        label="Back to letters",
        style=discord.ButtonStyle.secondary
    )
    async def back_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        await interaction.response.send_message(
            "Choose another letter ♡",
            view=LetterMenuView(),
            ephemeral=True
        )

class LetterView(discord.ui.View):
    @discord.ui.button(
        label="Open a letter 💌",
        style=discord.ButtonStyle.primary
    )
    async def open_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        await interaction.response.send_message(
            "Which letter would you like to open? ♡",
            view=LetterMenuView(),
            ephemeral=True
        )

@client.tree.command(name="open", description="Open a little letter 💌")
async def open_letter(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Your little letter box is here!",
        view=LetterView(),
        ephemeral=True
    )
client.run(TOKEN)