import discord
import random
from discord.ext import commands
import os
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)



@bot.command()
async def info(ctx):
    embed = discord.Embed( 
    title="Команды бота", 
    description="Список всех доступных команд для использования бота.", 
    color= discord.Color.blue ()  # Выбираем цвет 
    ) 
    embed.add_field( 
    name="Случайные проблемы", 
    value="Команда - !problems", 
    inline=False  
    ) 
    embed.add_field( 
    name="Переработка мусора", 
    value="Команда - !recycling. Выдаёт список команд для переработки отдельных видов мусора.", 
    inline=False  
    ) 
    await ctx.send(embed=embed) 


@bot.command()
async def problems(ctx):
    imag = os.listdir('images')
    ran_im = random.choice(imag)
    problems = {
        'flood.jpg':'Наводнение. Очень распространенная проблема. Наводнеие на момент 2024 года, случилось во многих городах мира. Страдают города такие как - Оренбург, Россия ; Дубай, ОАЭ и прочие.',
        'klimat.jpg':'Изменение климата. Самая страшная и опасная проблема. Изменение климата это колебания климата Земли в целом или отдельных её регионов с течением времени, выражающиеся в статистически достоверных отклонениях параметров погоды.',
        'navodn.jpg':'Повышение уровня моря. Процесс наблюдаемый с середины XIX века, в результате которого на протяжении одного лишь XX века глобальный уровень моря повысился на 17 см. С 1993 года уровень моря ежегодно повышается на 3,2 мм.'
    }
    rare = problems.get(ran_im)
    with open(f'images/{ran_im}','rb') as f:
        pictures = discord.File(f)
        await ctx.send(f'''```                              ====--==-Команда Случайная Проблема-==--====
Случайная Проблема - {rare}```''')
        await ctx.send(file=pictures)
