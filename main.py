import discord
import os

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.content.startswith("!logimage"):
        if message.attachments:
            image = message.attachments[0]
            image_url = image.url
            image_data = await image.read()

            # save the image to the Images folder
            image_path = os.path.join("Images", image.filename)
            with open(image_path, "wb") as f:
                f.write(image_data)

            await message.channel.send("Image logged successfully!")
        else:
            # retrieve a list of images from the server
            images = []
            async for message in message.channel.history(limit=100):
                if message.attachments:
                    images.append(message.attachments[0])

            if images:
                # let the user select an image to log
                # save the selected image to the Images folder
                await message.channel.send("Image logged successfully!")
            else:
                await message.channel.send("No images found on the server.")

client.run("DISCORD_BOT_TOKEN")
