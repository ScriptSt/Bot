import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Токен вашего бота
BOT_TOKEN = "8522827598:AAHrYvCH3PiHWCbOaDlPW890grKqmV2aR0U"

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    user = update.effective_user
    await update.message.reply_html(
        f"Привет, {user.mention_html()}! 👋\n"
        f"Рад тебя видеть! Я бот, который готов помочь."
    )

async def main():
    """Основная функция для запуска бота"""
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start_command))
    
    # Запускаем бота
    print("Бот запущен...")
    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
