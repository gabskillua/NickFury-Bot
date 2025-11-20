import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(TOKEN)


TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

marvel_personagens = [
    "Iron Man", "Thor", "Hulk", "Captain America", "Spider-Man",
    "Black Widow", "Wolverine", "Doctor Strange", "Scarlet Witch",
    "Deadpool", "Black Panther", "Captain Marvel"
]

ranks = ["C", "B", "A", "S", "SS", "SSS"]

missoes_base = [
    "investigar uma atividade suspeita em {lugar}.",
    "neutralizar uma célula da Hydra em {lugar}.",
    "salvar civis durante um ataque em {lugar}.",
    "conter uma anomalia energética detectada em {lugar}.",
    "impedir que uma arma de destruição massiva seja ativada em {lugar}."
]

lugares = [
    "Nova York", "Wakanda", "Sokovia", "o Edifício Baxter",
    "a Torre dos Vingadores", "o Aeroporta-Aviões da S.H.I.E.L.D"
]

def gerar_missao(personagens):
    rank = random.choice(ranks)
    missao = random.choice(missoes_base)
    lugar = random.choice(lugares)
    return rank, missao.format(lugar=lugar)

@bot.command()
async def missao(ctx, *, personagem):
    personagem = personagem.strip()

    if personagem not in marvel_personagens:
        await ctx.send(f"Nick Fury: *{personagem}? Nunca ouvi falar. Tenta outro herói.*")
        return

    rank, missao = gerar_missao(personagem)
    await ctx.send(
        f"Nick Fury: **Missão para {personagem}**\n"
        f"Rank: **{rank}**\n"
        f"Objetivo: {missao}"
    )

@bot.command()
async def equipe(ctx, *, membros):
    membros_lista = [m.strip() for m in membros.split()]
    desconhecidos = [m for m in membros_lista if m not in marvel_personagens]

    if desconhecidos:
        await ctx.send(f"Nick Fury: Esses aqui eu não conheço: {', '.join(desconhecidos)}")
        return

    rank, missao = gerar_missao(membros_lista)
    await ctx.send(
        f"Nick Fury: **Missão de equipe: {', '.join(membros_lista)}**\n"
        f"Rank: **{rank}**\n"
        f"Objetivo: {missao}"
    )

bot.run(TOKEN)


