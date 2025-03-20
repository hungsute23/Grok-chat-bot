const TelegramBot = require('node-telegram-bot-api');
const { sendMessageToGrok } = require('./grokService');
const { TELEGRAM_TOKEN } = require('./config');

// Create a new Telegram bot instance
const bot = new TelegramBot(TELEGRAM_TOKEN, { polling: true });

// Listen for incoming messages
bot.on('message', (msg) => {
    const chatId = msg.chat.id;
    const userMessage = msg.text;

    // Send user message to Grok API and handle the response
    sendMessageToGrok(userMessage)
        .then(response => {
            // Send the response back to the user
            bot.sendMessage(chatId, response);
        })
        .catch(error => {
            console.error('Error sending message to Grok API:', error);
            bot.sendMessage(chatId, 'Sorry, there was an error processing your request.');
        });
});