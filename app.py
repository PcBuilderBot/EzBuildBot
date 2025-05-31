from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, filters

TOKEN = 'TON_TOKEN_BOT'

app = Flask(__name__)
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)

def start(update, context):
    update.message.reply_text("👋 Salut ! Envoie-moi ton budget ou ce que tu veux faire avec ton futur PC.")

def handle_message(update, context):
    msg = update.message.text.lower()
    
    if "gaming" in msg:
        config = "🎮 Config gaming :\n- Ryzen 5 5600\n- RTX 3060\n- 16Go RAM\n- SSD 1To"
    elif "montage" in msg:
        config = "🎬 Config montage vidéo :\n- i7 12700K\n- 32Go RAM\n- RTX 4060\n- SSD 2To NVMe"
    elif "500" in msg or "600" in msg:
        config = "💰 Budget serré :\n- Ryzen 5 4600G (chipset intégré)\n- 16Go RAM\n- SSD 500Go\nPas de GPU dédié, mais bon en bureautique/jeux légers."
    else:
        config = "🤔 Je comprends pas bien. Envoie un budget (ex: 700€) ou un usage (gaming, bureautique...)."

    update.message.reply_text(config)

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

@app.route("/")
def index():
    return "Bot de config PC prêt 🔧"
