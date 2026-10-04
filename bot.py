import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get bot token from environment variable
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# Create bot instance
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print('=' * 30)
    print(f'Bot: {bot.user}')
    print(f'ID: {bot.user.id}')
    print(f'Connected to {len(bot.guilds)} guilds')
    print('=' * 30)

@bot.command(name='kanallarıverolleri')
@commands.has_permissions(administrator=True)
async def delete_channels_and_roles(ctx, action: str = None):
    """
    Tüm kanalları ve rolleri siler (Üyeler ve botlar etkilenmez).
    Kullanım: !kanallarıverolleri sil
    """
    if action != 'sil':
        await ctx.send('⚠️ Kullanım: `!kanallarıverolleri sil` - Tüm kanalları ve rolleri siler.')
        return

    # Confirm the action
    embed = discord.Embed(
        title="⚠️ DİKKAT: Yıkıcı İşlem",
        description="Tüm kanalları ve rolleri silmek üzeresiniz.\nBu işlem **GERİ ALINAMAZ**.\n\nOnaylamak için ✅ emojisine tıklayın.",
        color=discord.Color.red()
    )
    confirmation_message = await ctx.send(embed=embed)
    await confirmation_message.add_reaction('✅')

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) == '✅' and reaction.message.id == confirmation_message.id

    try:
        # Wait for confirmation
        await bot.wait_for('reaction_add', timeout=30.0, check=check)
        
        await ctx.send('🔄 Kanal ve rol silme işlemi başlatılıyor...')
        
        # Delete all channels except the one the command was sent in
        for channel in ctx.guild.channels:
            if channel.id == ctx.channel.id:
                continue
            try:
                await channel.delete(reason='Toplu silim işlemi başlatıldı.')
            except discord.Forbidden:
                pass
            except discord.HTTPException:
                pass
                
        # Delete all roles (except @everyone and bot's highest role)
        for role in ctx.guild.roles:
            if role.name != '@everyone' and role < ctx.guild.me.top_role and not role.managed:
                try:
                    await role.delete(reason='Toplu silim işlemi başlatıldı.')
                except discord.Forbidden:
                    pass
                except discord.HTTPException:
                    pass
        
        # Send success message
        await ctx.send('✅ Tüm kanallar ve roller başarıyla silindi! (Bu kanal hariç)')
        
    except asyncio.TimeoutError:
        await ctx.send('⏰ Zaman aşımı! İşlem iptal edildi.')
        await confirmation_message.delete()
    except Exception as e:
        await ctx.send(f'❌ Beklenmeyen bir hata oluştu: {e}')

@delete_channels_and_roles.error
async def delete_channels_and_roles_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ Bu komutu kullanmak için `Yönetici` yetkisine sahip olmalısınız.")

# Run the bot
if __name__ == "__main__":
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("HATA: .env dosyasında DISCORD_TOKEN bulunamadı.")