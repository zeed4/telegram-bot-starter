#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! 🎲 Я бот для DnD. Используй команду /roll, чтобы бросить кубик.\nПример: /roll 1d20"
    )

# Команда /roll
async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Используй формат: /roll 1d20 или /roll 2d6")
        return
    try:
        count, die = context.args[0].lower().split('d')
        count = int(count)
        die = int(die)
        rolls = [random.randint(1, die) for _ in range(count)]
        await update.message.reply_text(f'🎲 Результат: {rolls} (сумма: {sum(rolls)})')
    except Exception as e:
        await update.message.reply_text("Ошибка. Пример: /roll 2d6")

# Основной запуск бота
if __name__ == '__main__':
    token = os.environ["BOT_TOKEN"]
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("roll", roll))

    print("🤖 Бот запущен!")
    app.run_polling()
