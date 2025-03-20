# Telegram Chatbot

This project is a Telegram chatbot that interacts with users and utilizes the Grok API for processing messages.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/telegram-chatbot.git
   ```
2. Navigate to the project directory:
   ```
   cd telegram-chatbot
   ```
3. Install the dependencies:
   ```
   npm install
   ```

## Usage

1. Create a `.env` file in the root directory and add your Telegram bot token and Grok API credentials:
   ```
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   GROK_API_ENDPOINT=your_grok_api_endpoint
   ```
2. Start the bot:
   ```
   npm start
   ```

## Environment Variables

The following environment variables are required:

- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
- `GROK_API_ENDPOINT`: The endpoint for the Grok API.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.