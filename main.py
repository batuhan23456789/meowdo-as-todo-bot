import os
import requests
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print("botunuz giriş yapmıştır!")

@bot.command()
async def mem(ctx):
    
    sayi = random.randint(1, 10)
    
    
    if 1 <= sayi <= 5:
        selected_file = "Aİ.jpg"
    elif 6 <= sayi <= 8:
        selected_file = "mizahlı.webp"
    elif sayi == 9:
        selected_file = "mizahsız.webp"
    else:
        selected_file = "orta.webp"

    
    dosya_yolu = f'images/{selected_file}'

    if os.path.exists(dosya_yolu):
        with open(dosya_yolu, 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    else:
        await ctx.send(f"Hata: {ad} dosyası klasörde bulunamadı!")


def get_duck_image_url():    
    url = "https://random.dog/woof.json"
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


bot.run("")
