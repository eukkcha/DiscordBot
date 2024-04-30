import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

# 봇 토큰
token = '토큰'

# 기본 인텐트 설정
intents = discord.Intents.default() 
intents.message_content = True

bot = commands.Bot(
    command_prefix='라마 ', # 명령어 접두사
    intents=discord.Intents.all()) # 모든 인텐트 활성화

# Bot is ready
@bot.event
async def on_ready(): 
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game("라마 도움말")) # 활동 메세지
    print(f'{bot.user} is ready and online.') # 봇 준비되면 출력
    print('--------------------------------')

# 도움말 명령어
@bot.command()
async def 도움말(ctx):
    embed=discord.Embed(title="본국 제1 본정보부 첩보부서", url="https://github.com/eukkcha/LlamaBot", description="조선인민국 호위총국 제14과 첨단양자전산화공수특전대 산하 주식회사 에버랜드 소속 전자동화어트랙션지원병력.:llama:\n\n해당 전동화병기는 시범 운영 중에 있음.\n\n본국 제1 본정보부 첩보부서에서 그동안 작전해온 기밀들을 낱낱히 공개하도록 하겠음.", color=0xf43d8f)
    embed.set_author(name="라마봇", url="https://github.com/eukkcha/LlamaBot")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1233535085635043390/3a12cd88c71c6c8c6fabb0ef26fb07ca.png?size=2048")
    
    embed.add_field(name="`라마 도움말`", value="도움말 표시", inline=True)
    embed.add_field(name="`라마 날씨`", value="현재 날씨 정보 표시", inline=True)
    embed.add_field(name="`라마 채팅 [메세지]`", value="[메세지]를 라마봇이 채팅", inline=True)
    embed.add_field(name="`라마 핑`", value="봇 핑 표시", inline=True)
    embed.add_field(name="`라마 뻘소리`", value="개발 중", inline=True)
    embed.add_field(name="`라마 환율`", value="개발 중", inline=True)
    
    embed.set_footer(text="개발자 : @eukkcha")
    
    await ctx.send(embed=embed)
    
# 네이버 날씨 정보 크롤링
def get_weather_info():
    html = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%82%A0%EC%94%A8')
    soup = BeautifulSoup(html.text, "html.parser")
    
    current_temp = soup.find('div', {'class':'temperature_text'}) # 현재 날씨
    weather_desc = soup.find('span', {'class':'weather before_slash'}) # 현재 기상
    dust = soup.find('li', {'class':'item_today level2'}) # 미세 먼지
    
    # 크롤링에 실패 했을 시
    if current_temp and weather_desc and dust:
        return current_temp.text.strip(), weather_desc.text.strip(), dust.text.strip()
    else:
        return '날씨 정보를 가져오는데 실패했음을 알림', '상세 정보 없음', '오류 발생'
    
    return current_temp, weather_desc, dust

# 날씨 명령어
@bot.command()
async def 날씨(ctx):
    temp, description, dust = get_weather_info()
    message = f"남조선괴뢰통신정보국포착감시프로세스를 가동중\n:llama:`{temp}C ({description}), {dust}`:llama:"
    
    await ctx.send(message)
    
# 핑 명령어
@bot.command()
async def 핑(ctx):
    latancy = bot.latency
    await ctx.send(f'라마국의 긴급공멸프로토콜 속도 : {round(latancy * 1000)}ms')

# 채팅 명령어
@bot.command()
async def 채팅(ctx, *, message: str):
    await ctx.message.delete() # 사용자의 메시지 삭제 
    await ctx.send(message)

# 봇 실행
bot.run(token)
