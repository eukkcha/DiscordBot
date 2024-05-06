import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import random

# 봇 토큰
token = open("llama_token.txt", "r").readline()

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
    embed=discord.Embed(title="본국 제1 본정보부 첩보부서", 
                        url="https://github.com/eukkcha/LlamaBot", 
                        description="조선인민국 호위총국 제14과 첨단양자전산화공수특전대 산하 주식회사 에버랜드 소속 전자동화어트랙션지원병력.:llama:\n\n해당 전동화병기는 시범 운영 중에 있음.\n\n본국 제1 본정보부 첩보부서에서 그동안 작전해온 기밀들을 낱낱히 공개하도록 하겠음.", 
                        color=0xf43d8f)
    embed.set_author(name="라마봇", 
                     url="https://github.com/eukkcha/LlamaBot")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/1233535085635043390/3a12cd88c71c6c8c6fabb0ef26fb07ca.png?size=2048")
    
    embed.add_field(name="`라마 도움말`", value="도움말 출력", inline=True)
    embed.add_field(name="`라마 핑`", value="봇 핑 출력", inline=True)
    embed.add_field(name="`라마 안녕`", value="라마봇과 인사하기", inline=True)
    embed.add_field(name="`라마 날씨`", value="현재 날씨 정보 출력", inline=True)
    embed.add_field(name="`라마 개소리`", value="랜덤 개소리 출력", inline=True)
    embed.add_field(name="`라마 채팅 [메세지]`", value="[메세지]를 라마봇이 출력", inline=True)
    
    embed.set_footer(text="(라마봇0.1.3)   개발자 : @eukkcha")
    
    await ctx.send(embed=embed)
    
# 네이버 날씨 정보 크롤링
def get_weather_info():
    html = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EB%85%B8%EC%9B%90%EA%B5%AC+%EB%82%A0%EC%94%A8&oquery=%EA%B0%95%EB%82%A8%EA%B5%AC+%EB%82%A0%EC%94%A8&tqi=iBAoTwqptbNssuT1VHwssssssT8-001324')
    soup = BeautifulSoup(html.text, "html.parser")
    
    current_temp = soup.find('div', {'class':'temperature_text'}) # 현재 날씨
    weather_desc = soup.find('span', {'class':'weather before_slash'}) # 현재 기상
    dust = soup.find('span', {'class':'txt'}) # 미세 먼지
    
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
    message = f"남조선괴뢰통신정보국포착감시프로세스를 가동중\n:llama:`{temp}C ({description}), 미세먼지 {dust}`:llama:"
    
    await ctx.send(message)
    
# 핑 명령어
@bot.command()
async def 핑(ctx):
    latancy = bot.latency
    await ctx.send(f'라마국의 긴급공멸프로토콜 속도 `{round(latancy * 1000)} ms`')

# 채팅 명령어
@bot.command()
async def 채팅(ctx, *, message: str):
    await ctx.message.delete() # 사용자의 메시지 삭제 
    await ctx.send(message)
    
# 개소리 문장 리스트
sentences = [
    "본국의 전략비축자산인 까까를 침탈해가는것은 심각한 군사도발행위임.",
    "라마국은 식량조차 없어 본국의 뇌-컴퓨터 인터페이스를 기반으로 한 오토파일럿 라마년 감시체계(ALSS)는 커녕 과거의 유산인 유인보초시스템 또한 구성하지 못해 그 어느 시간에도 공격을 효과적으로 방어할 방어 체계가 단 하나도 없음이 본국의 그 어떤 정보화 체계들보다 최소 25년 이상 앞선 정보화 기술력에 기반한 자동 수집 봇에 의해 밝혀져 만천하에 공개되었음.",
    "제국주의국가들은 모두 본국의 최후통첩을 똑똑히 보고 명심하길 바람. 그 어떤 추가적인 도발행위라도 이루어질 시 국제사회에는 치명적인 피바람이 불게될것.",
    "본국의 특수목적 분립정보부산하 지하금고에 철저하게 최상의 보안상태로 보관되어있음.",
    "$1 라마국 달러(LMD)의 가치는 미국 달러로 약 $0.000000000000273의 가치를 지님.",
    "본국 비대칭전략운용사령부 직속 제2과 강행타격공수기계화돌격대의 120톤급 차륜형 이동식발사대의  반축스핀적색전자탄두 이온화7행정반양자중력장상반전추진 미사일이 불을 뿜는 모습을 보고싶지 않다면 현시간부로부터 35시간동안  침묵을 유지할것.",
    "본국 전략사령본부에서는 본 지역의 상대친화도를 중립구역에서 비중립 준적대지역으로 격상조치하였음을 선언함.",
    "그 어떤것을 선택하더라도 본국 비대칭전략핵무기에 의한 국제사회의 광범위한 파괴와 충격은 막을 수 없을것.",
    "본국은 이미 그동안의 누적데이터를 통해 디폴트가 거의 신적으로 해당 문제를 해결해주는 최고의 방안이라는 것을 학습하였음.",
    "본국은 국제사회의 세력균형을 되찾기 위해 군사행동을 기꺼이 시행할 준비가 되어있음을 선언하는 바임.",
    "상대국은 본국이 주도중인 평화주의적 국제정세의 경로에서 이탈하지 말고 균형있는 세계정세를 유지해야할것.",
    "본국 육군소속 비대칭전략사령부 제4자기화대대 역축스핀반양자과이온화대기스피어운용중대 직속 비처리반양자 비축허브의 주동력원인 축중첩비이온화삼중수소변환레일코어에서  반자기성 쇼트가 발생, 허브 전체에 막대한 반자기성 플라즈마파를 발생시켜 비축중이던 반양자필러에서 축결합양자융합연쇄반응이 일어나 이중축비통과성가공양자인 크릴톤이 대량으로 지각을 통해 맨틀로 침투, 맨틀 내의 일반물질과 크릴톤간의 축전이비활성교환핵반응이 발생하여 이에 따른 B형중력장왜곡이 발생, 지구의 궤도가 0.8% 변화하였음을 귀국에 알리는 바임. 이에 따른 영향으로는 약 5세기 내의 초빙하기 발생이 예상됨.",
    "나 잘거니깐 이제 조용히 할것.",
    "긴급공멸 우리늄폭풍 프로토콜 가동준비 카운트다운 돌입.",
    "현재 본국자본회수를 위해 대전차로켓포로 무장한 지상대정규군과 부유식 능동소나 및 리모트가이드무착수음할로포인트초공동어뢰를 탑재한 극초음속 고무동력초계기를 발진시킬 예정임을 알림."
    ]

# 개소리 명령어
@bot.command()
async def 개소리(ctx):
    message = random.choice(sentences)
    await ctx.send(message)
    
@bot.command()
async def 안녕(ctx):
    user_name = ctx.author.display_name
    await ctx.send(f'오 {user_name}형 ㅎㅇ')

# 봇 실행
bot.run(token)
