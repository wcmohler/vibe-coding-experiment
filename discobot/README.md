# Discord Bot with Ollama Integration

A Discord bot that integrates with Ollama's LLM API to provide AI-powered responses and server management features.

## Features

- 🤖 AI-powered responses using Ollama's LLM
- 📊 Server information and statistics
- 👋 Welcome messages for new servers
- 💬 Natural language interaction through mentions
- 📝 Command-based interaction

## Commands

- `!ask <question>` - Ask the bot any question
- `!hello` - Get a friendly greeting
- `!help_me` - Show available commands
- `!server_info` - Get information about the current server

## Prerequisites

- Docker and Docker Compose installed
- Discord Bot Token
- Ollama instance running (optional, defaults to localhost)

## Setup

1. Clone the repository
2. Create a Discord bot and get your token from the [Discord Developer Portal](https://discord.com/developers/applications)
3. Set up your environment variables:
   ```bash
   export DISCORD_TOKEN=your_discord_token_here
   export OLLAMA_HOST=your_ollama_host  # Optional, defaults to localhost
   ```

## Running with Docker

1. Navigate to the discobot directory:
   ```bash
   cd discobot
   ```

2. Build and start the container:
   ```bash
   docker-compose up
   ```

3. To run in detached mode:
   ```bash
   docker-compose up -d
   ```

4. To stop the bot:
   ```bash
   docker-compose down
   ```

## Development

The bot is built using:
- Python 3.11
- discord.py
- requests

### Project Structure

```
discobot/
├── bot.py           # Main bot code
├── Dockerfile       # Container configuration
├── docker-compose.yml # Service configuration
└── requirements.txt # Python dependencies
```

## Environment Variables

- `DISCORD_TOKEN`: Your Discord bot token (required)
- `OLLAMA_HOST`: Hostname of your Ollama instance (optional, defaults to localhost)

## License

MIT License 