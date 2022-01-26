# -*- coding:utf-8 -*- 
# 위에 구문은 # 빼버리시면 문제 생깁니다.
# 가끔가다 애가 인코딩을 잘못 읽어서 오류를 냅니다. 그것을 대비하기 위해 'utf-8'으로 읽으라고 선언합니다.

from ast import Constant
from distutils import command
import discord, asyncio

from setuptools import Command # 디스코드 모듈과, 보조 모듈인 asyncio를 불러옵니다.

token = "OTM1MTE5ODQ0MzI2NjQ1ODMw.Ye6AOA.57rHBUJJX5iSF_3jzPKJi24wYvk"; # 아까 메모해 둔 토큰을 입력합니다
client = discord.Client(commands_delif = "#"); # discord.Client() 같은 긴 단어 대신 client를 사용하겠다는 선언입니다.

@client.event
async def on_ready(): # 봇이 준비가 되면 1회 실행되는 부분입니다.
  # 봇이 "반갑습니다"를 플레이 하게 됩니다.
  # 눈치 채셨을지 모르곘지만, discord.Status.online에서 online을 dnd로 바꾸면 "다른 용무 중", idle로 바꾸면 "자리 비움"으로 바뀝니다.
  await client.change_presence(status=discord.Status.online, activity=discord.Game("정성스레 손편지 적는 중"))
  print("오늘은 무엇을 적을까!") # I'm Ready! 문구를 출력합니다.
  print(client.user.name) # 봇의 이름을 출력합니다.
  print(client.user.id) # 봇의 Discord 고유 ID를 출력합니다.
  
@client.event
async def on_message(message): # 메시지가 들어 올 때마다 가동되는 구문입니다.
  if message.author.bot: # 채팅을 친 사람이 봇일 경우
    return None # 반응하지 않고 구문을 종료합니다.
  
  if message.content.startswith("#도와줘"): # !명령어   라는 채팅을 친다면
    # 메시지 전송이 두가지 방법이 있습니다. 상황에 맞는 구문을 사용하시면 됩니다.
    # 이 구문은 메시지가 보내진 채널에 메시지를 보내는 구문입니다.
    embed = discord.Embed(title = "🌸 봄편지 사용법", color = 0xff9eb1)
    embed.add_field(name = "💌 익명 편지", value = "``#전해줘``")
    embed.add_field(name = "✏ 지우개", value = "``#지워줘``")
    embed.add_field(name = "📄 도움말", value = "``#도와줘``")
    embed.set_footer(text = "추후 기능이 추가될 수 있어! ｜ ⓒ 2022 made by 봄")
    await message.channel.send("응, 알았어!", embed = embed)
    # 이 아래 구문은 메시지를 보낸 사람의 DM으로 메시지를 보냅니다.
    #await message.author.send("응답")

  # 이번 강좌를 위해서 추가적인 모듈은 불러 올 필요가 없습니다. 단순히 메시지 전송 구문을 아래과 같이 바꾸면 됩니다.
  # 익명 편지(임베드)
  if message.content.startswith("#전해줘"):
        if message.author.guild_permissions.manage_messages:
           try:
                amount = message.content[5:]
                await message.channel.send("띵동, 편지가 도착했어★") # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.
                await message.channel.send(embed = discord.Embed(title="💌 익명 편지", description="누군가가 " + amount + " 이/가 하고 싶대!", color=0xff9eb1)) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
                await message.delete()
                #embed.set_footer(text="같이 할래?") # 하단에 들어가는 조그마한 설명을 잡아줍니다
           except ValueError:
                await message.channel.send("전하고픈 말을 적어줘!")

  # 지우개(채팅청소 기능)
  if message.content.startswith("#지워줘"):
        if message.author.guild_permissions.manage_messages:
            try:
                amount = message.content[5:]
                await message.channel.purge(limit=int(amount))
                await message.channel.send(f"✏ **{amount}**개의 메시지를 지웠어!")
            except ValueError:
                await message.channel.send("✏ 지울 메시지의 **수**를 입력해 줘!")
        else:
            await message.channel.send("✏ 너에겐 그럴 자격이 없어!")

# 여기 token에는 토큰을 넣지 않고 그대로 옮겨 쓰시면 됩니다.
TOKEN = os.environ.get('BOT_TOKEN') # 아까 넣어놓은 토큰 가져다가 봇을 실행하라는 부분입니다. 이 코드 없으면 구문이 아무리 완벽해도 실행되지 않습니다.
