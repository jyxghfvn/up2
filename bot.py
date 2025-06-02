from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackContext

LANGUAGE, MODE, STEP, MESSAGE = range(4)

async def start(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['RU', 'ENG']]
    await update.message.reply_text(
        "Привет. Я шифратор. Давайте начнем.\n"
        "Пожалуйста, выберите язык:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return LANGUAGE

async def language(update: Update, context: CallbackContext) -> int:
    lang = update.message.text.upper()
    if lang not in ['RU', 'ENG']:
        await update.message.reply_text("Пожалуйста, выберите язык из предложенных вариантов.")
        return LANGUAGE
    context.user_data['lang'] = lang
    reply_keyboard = [['зашифровать', 'расшифровать']]
    await update.message.reply_text(
        "Выберите режим:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return MODE

async def mode(update: Update, context: CallbackContext) -> int:
    mode_input = update.message.text.lower()
    if mode_input not in ['зашифровать', 'расшифровать']:
        await update.message.reply_text("Пожалуйста, выберите режим из предложенных вариантов.")
        return MODE
    context.user_data['mode'] = mode_input
    await update.message.reply_text(
        "Введите шаг сдвига (число):",
        reply_markup=ReplyKeyboardRemove()
    )
    return STEP

async def step(update: Update, context: CallbackContext) -> int:
    try:
        smeshenie = int(update.message.text)
        context.user_data['smeshenie'] = smeshenie
        await update.message.reply_text(
            "Теперь введите сообщение для обработки:",
            reply_markup=ReplyKeyboardRemove()
        )
        return MESSAGE
    except ValueError:
        await update.message.reply_text("Пожалуйста, введите число для шага сдвига.")
        return STEP

async def message_handler(update: Update, context: CallbackContext) -> int:
    message = update.message.text.upper()
    lang = context.user_data['lang']
    mode = context.user_data['mode']
    smeshenie = context.user_data['smeshenie']

    alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    if lang == 'RU':
        alphabet = alfavit_RU
    else:
        alphabet = alfavit_ENG

    result = ''
    for i in message:
        if i in alphabet:
            mesto = alphabet.find(i)
            if mode == 'зашифровать':
                new_mesto = mesto + smeshenie
            else:
                new_mesto = mesto - smeshenie
            new_mesto %= len(alphabet)
            result += alphabet[new_mesto]
        else:
            result += i

    await update.message.reply_text(f"Результат:\n{result}", reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

async def cancel(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Диалог завершен.', reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

def main():
    TOKEN = '7922164398:AAGPtGqaUsvwRIPb-_llPuog91tLUPCymOE'

    application = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            LANGUAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, language)],
            MODE: [MessageHandler(filters.TEXT & ~filters.COMMAND, mode)],
            STEP: [MessageHandler(filters.TEXT & ~filters.COMMAND, step)],
            MESSAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    application.add_handler(conv_handler)

    application.run_polling()

if __name__ == '__main__':
    main()