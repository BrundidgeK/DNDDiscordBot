# Dungeon Master Discord Bot

## Overview

The Dungeon Master Discord Bot is designed to facilitate and manage Dungeons & Dragons campaigns on Discord. This bot allows players to interact with a virtual dungeon master, making it easier to manage characters, roll dice, and progress through the campaign story.

## Features

- **/Roll**: Rolls a random number between 1 and the specified number.
- **/AddCharacter**: Adds a playable character to the campaign, including name, class, level, and race.
- **/RemoveCharacter**: Removes the named character from the campaign.
- **/CampaignStory**: Selects the D&D campaign story to follow.
- **/BeginCampaign**: Starts the campaign.
- **/RewriteStory**: Allows you to rewrite a story event that occurred.
- **/stopstory**: Ends the current campaign (this action cannot be undone).
- **/SaveCampaign**: Saves the current progress on the campaign
- **/LoadCampaign**: Loads a previously saved campaign (make sure to save your current one first)
- **/SavedCampaigns**: Provides a list of all campaigns that have been saved
- **/Recap**: Provides a recap for the current campaign
- **~**: Allows players to input actions they will perform in the game.

## Prerequisites

- Python 3.8+
- Discord account and a server where you can add the bot.
- OpenAI API key.
- Discord Bot Token.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/dungeon-master-discord-bot.git
    cd dungeon-master-discord-bot
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables:
    - Create a `.env` file in the root directory of your project.
    - Add your OpenAI API key and Discord Bot Token to the `.env` file:
        ```env
        OPENAI_TOKEN=your_openai_api_key
        DISCORD_TOKEN=your_discord_bot_token
        ```

## Usage

1. Run the bot:
    ```bash
    python main.py
    ```

2. Invite the bot to your Discord server using the OAuth2 URL generated from the Discord Developer Portal.

## Commands

- **/commands**: Lists all the available commands.
- **/Roll <number>**: Rolls a random number between 1 and the specified number.
- **/AddCharacter <name>, <class> <level>, <race>**: Adds a playable character to the campaign.
- **/RemoveCharacter <name>**: Removes the named character from the campaign.
- **/CampaignStory <story>**: Selects the D&D campaign story to follow.
- **/BeginCampaign**: Starts the campaign.
- **/RewriteStory <event>**: Rewrites a story event.
- **/stopstory**: Ends the current campaign.
- **~<action>**: Allows players to input actions they will perform in the game.

## Example Usage

- **Adding a Character**: 
    ```
    /AddCharacter Majax, Warlock 1, Elf
    ```
- **Rolling a Dice**: 
    ```
    /Roll 20
    ```
- **Saving a Campaign**:
    ```
    /SaveCampaign Cthulu's Rising
    ```
    
- **Performing Actions**:
    ```
    ~I attempt a sneak attack on the guards
    ```

## Development

To contribute to this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License.

---

If you encounter any issues or have any questions, feel free to open an issue in the repository or contact the maintainer.

Enjoy your adventures with the Dungeon Master Discord Bot!
