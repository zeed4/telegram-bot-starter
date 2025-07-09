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
    token = os.environ.get("BOT_TOKEN")
    if not token:
        print("❌ Ошибка: переменная BOT_TOKEN не найдена")
    else:
        app = ApplicationBuilder().token(token).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("roll", roll))
        print("🤖 Бот запущен!")
        app.run_polling()
        
