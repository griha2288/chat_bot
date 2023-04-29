import discord
import logging
import random

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

TOKEN = "MTEwMTc2Mjg1NTEyNjE4ODEyMw.GISdye.w8Ny4p8C78aG5EY1m-uq4CNvJDzFOMnNo3lTWY"

fun_stories_file_path = 'data/fun_stories.txt'
memes_path = 'data/memes/'

greetings = [
    'привет',
    'здравтсв',
    'не хворать',
    'добрый день',
    'здарова'
]

fun_story_requests = [
    'анекдот',
    'шутк',
    'истор',
    'шутеечк'
]

meme_requests = [
    'мем',
    'мемчик',
    'картинк',
    'мемас',
    'мемчик',
    'изобра',
    'фотку',
    'фоточку',
    'фото'
]

fun_stories_file = open(fun_stories_file_path, 'r', encoding='utf8')
fun_stories = [i[:-1] for i in fun_stories_file]
fun_stories_file.close()

memes = [memes_path + str(i) + '.jpg'for i in range(1, 41)]

class YLBotClient(discord.Client):
    async def on_ready(self):
        logger.info(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            logger.info(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Привет, {member.name}!'
        )

    async def on_message(self, message):
        global greetings
        if message.author == self.user:
            return
        current_message = message.content.lower()
        for i in greetings:
            if i in current_message:
                await message.channel.send('Приветсвую')
                return
        for i in fun_story_requests:
            if i in current_message:
                s = fun_stories[random.randint(1, len(fun_stories) - 1)]
                await message.channel.send(s)
                return
        for i in meme_requests:
            if i in current_message:
                image = discord.File(memes[random.randint(0, 40)])
                await message.channel.send(file=image)
                return
        if 'алё' in current_message or 'але' in current_message:
            await message.channel.send('але')
        elif 'новост' in current_message:
            await message.channel.send('все стабильно')
        elif '?' in current_message:
            await message.channel.send('не понял вопроса, я ток мемы с анекдотами кидаю')
        else:
            await message.channel.send('непон')


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = YLBotClient(intents=intents)
client.run(TOKEN)