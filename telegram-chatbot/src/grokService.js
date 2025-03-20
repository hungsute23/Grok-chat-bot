const axios = require('axios');
const config = require('./config');

const grokApiEndpoint = config.GROK_API_ENDPOINT;

async function sendMessageToGrok(userMessage) {
    try {
        const response = await axios.post(grokApiEndpoint, {
            message: userMessage
        });
        return response.data;
    } catch (error) {
        console.error('Error sending message to Grok API:', error);
        throw error;
    }
}

module.exports = {
    sendMessageToGrok
};