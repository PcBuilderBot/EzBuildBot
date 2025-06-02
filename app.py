from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os
import asyncio

app = Flask(__name__)
TOKEN = os.environ.get("TOKEN")

# Créer le bot Telegram
bot_app = ApplicationBuilder().token(TOKEN).build()

# Commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Yo poto ! Envoie-moi ton budget pour une config PC 💻🔥")

# Gestion des messages texte
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.lower()
    if "800" in message:
        await update.message.reply_text("Config à 800€ : Ryzen 5, RTX 4060 Ti, 16Go RAM 🔥")
    elif "1000" in message:
        await update.message.reply_text("Config à 1000€ : i5 13400F, RTX 4070, 32Go RAM 🚀")
    else:
        await update.message.reply_text("Dis-moi ton budget pour que je te sorte la meilleure config 👇")

# Ajouter les handlers
bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Webhook pour Telegram
@app.route(f"/{TOKEN}", methods=["POST"])
async def telegram_webhook():
    update = Update.de_json(request.get_json(force=True), bot_app.bot)
    await bot_app.process_update(update)
    return "ok"
