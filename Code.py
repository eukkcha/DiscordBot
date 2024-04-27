import discord
from discord.ext import commands

# 봇 설정
token = 'llama bot Token'
intents = discord.Intents.default() # 기본 인텐트 설정
bot = commands.Bot(command_prefix='라마 ', intents=discord.Intents.all()) # 명령어 접두사 설정, 모든 인텐트 활성화

# 봇이 준비되었을 때
@bot.event
async def on_ready(): 
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("라마 명령어"))
    print(f'긴급공멸 우라늄폭풍 {bot.user} 프로토콜이 가동준비임을 알림.')
    
@bot.command()
async def 명령어(ctx, cmd: str = None):
    if cmd is None:
        # 기본 도움말 메시지
        help_text = "### 본국 제1 본정보부 첩보부서에서 그동안 작전해온 기밀들을 낱낱히 공개함\n"
        commands_list = {
            "say": "본국이 해당 메세지를 말해줌.",
            "명령어": "본국을 사용하는 방법을 알려줌."
        }
        for command, description in commands_list.items():
            help_text += f"`라마 {command}` - {description}\n"
        await ctx.send(help_text)
    else:
        # 특정 명령어에 대한 도움말
        commands_desc = {
            "say": "사용법: `라마 say <message>`\n본국이 해당 메세지를 말해줌.",
            "명령어": "사용법: `라마 명령어 [command]`\n본국을 사용하는 방법을 알려줌."
        }
        if cmd in commands_desc:
            await ctx.send(commands_desc[cmd])
        else:
            await ctx.send("그런 커맨드는 본국의 긴급공멸 우라늄폭풍에 의해 존재하지 않음.")

@bot.command() 
async def 꼬추2피코미터(message): 
    await message.channel.send('핵전쟁을 하겠다는 군사도발행위로밖에 해석되지 않는 공격적행보에 본국은 비대칭전략무기로 대응할것임.')
    
@bot.command() 
async def 응디(message):
    await message.channel.send('아 응디')
    await message.channel.send('응디')
    await message.channel.send('응디')
    await message.channel.send('응디')
    await message.channel.send('응디')
    
@bot.command() 
async def 안녕(message): 
    await message.channel.send('안녕하세요 베스킨라빈스입니다')
        
# say 명령어
@bot.command()
async def say(ctx, *, message: str):
    await ctx.message.delete()  # 사용자의 메시지 삭제 
    await ctx.send(message)

# 봇 실행
bot.run(token)
