from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import logging

# Вставьте сюда ваш токен
TOKEN = '6599430227:AAEspy7_EKIoDB5LlArBUH4SLRtp6-GWDdY'

# URL вашего веб-приложения
WEB_APP_URL = 'https://github.com/s3kond/tap-game-meg-coin'

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Начать играть", web_app={'url': WEB_APP_URL})],
        [InlineKeyboardButton("Как заработать на игре", callback_data='how_to_earn')],
        [InlineKeyboardButton("Подписаться на канал", url='https://t.me/meg_c0in')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привет! Это Meg Coin Мы только стартуем, но уже точно знаем, что листингу — быть! И очень скоро 😏\n\n"
        "Теперь ты — директор криптобиржи!\n"
        "Тапай по экрану, развивай бизнес и зарабатывай монеты.\n"
        "А если ещё и друзей подтянешь — вместе построите крутой бизнес и заработаете больше монет 😎",
        reply_markup=reply_markup
    )

# Функция для обработки нажатий кнопок
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'how_to_earn':
        await query.message.reply_text(
            "Как играть в Hamster Kombat ⚡️\n\n"
            "💰 Tap to earn\n"
            "Тапай по экрану и собирай монеты\n\n"
            "⛏ Mine\n"
            "Прокачивай карточки, которые дадут возможность пассивного дохода.\n\n"
            "⏰ Прибыль в час\n"
            "Биржа будет работать для тебя самостоятельно, даже когда ты не в игре в течение 3х часов. \n"
            "Далее нужно будет перезайти в игру снова.\n\n"
            "📈 LVL\n"
            "Чем больше монет у тебя на балансе — тем выше уровень биржи. Чем выше уровень — тем быстрее сможешь зарабатывать ещё больше монет\n\n"
            "👥 Friends\n"
            "Приглашай своих друзей, и вы получите бонусы. Помоги другу перейти в следующие лиги, и вы получите ещё больше бонусов.\n\n"
            "🪙 Token listing\n"
            "По итогам сезона будет выпущен токен, который будет распределен между игроками. \n"
            "Даты сообщим в нашем анонс-канале. Следите за новостями!"
        )

# Основная функция для запуска бота
def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    try:
        application.run_polling()
    except Exception as e:
        logger.error(f"Error: {e}")

if __name__ == '__main__':
    main()
