# Karolinska Lunch Bot

This is a Discord bot that fetches the daily lunch menu from the [61an Gastrogate Website](https://61an.gastrogate.com/dagens-lunch/) and provides it in a Discord server through various commands.

## Features

- **Fetch lunch menus for each weekday**:
  - `!monday` - Get the lunch menu for Monday.
  - `!tuesday` - Get the lunch menu for Tuesday.
  - `!wednesday` - Get the lunch menu for Wednesday.
  - `!thursday` - Get the lunch menu for Thursday.
  - `!friday` - Get the lunch menu for Friday.
- **Easy setup**: Uses environment variables to keep your bot token secure.
- **Web scraping**: Uses BeautifulSoup to scrape lunch menu data from [61an Gastrogate](https://61an.gastrogate.com/dagens-lunch/).

## Installation

### Prerequisites

Make sure you have the following installed:

- Python 3.7+
- [Discord Developer Portal](https://discord.com/developers/applications) account to create a bot and obtain your bot token.

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/karolinska-lunch-bot.git
   cd karolinska-lunch-bot
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the root of the project and add your Discord bot token:

   ```bash
   DISCORD_TOKEN=your_discord_bot_token
   ```

5. **Run the bot:**
   ```bash
   python main.py
   ```

## Commands

The bot responds to the following commands:

| Command      | Description                            |
| ------------ | -------------------------------------- |
| `!monday`    | Fetches Monday's lunch menu.           |
| `!tuesday`   | Fetches Tuesday's lunch menu.          |
| `!wednesday` | Fetches Wednesday's lunch menu.        |
| `!thursday`  | Fetches Thursday's lunch menu.         |
| `!friday`    | Fetches Friday's lunch menu.           |
| `!today`     | Placeholder for fetching today's menu. |

## How it works

The bot scrapes the lunch menu from [61an Gastrogate](https://61an.gastrogate.com/dagens-lunch/) using the BeautifulSoup library. It fetches the menu data for each day and responds in Discord when the respective command is used.

### Example

## Files

- `main.py`: Contains the bot logic and command handling.
- `response.py`: Responsible for fetching and processing the lunch menu via web scraping.

## Dependencies

- [discord.py](https://github.com/Rapptz/discord.py) - A Python wrapper for the Discord API.
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/) - A library to extract data from HTML and XML files.
- [requests](https://pypi.org/project/requests/) - A simple HTTP library for Python.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
