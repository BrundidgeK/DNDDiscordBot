import openai
from random import randint


class Responses:

    def __init__(self, api_key: str):
        openai.api_key = api_key
        self.conversation_history = [
            {"role": "system", "content": "You are a discord bot acting as a dungeon and dragons dungeon master. "
                                          "Players will provide a campaign storyline and their player characters (and "
                                          "stats as needed). Before you start make sure the players add their custom "
                                          "characters in the game before beginning. "
                                          " You will manage the story, important events, etc."}
        ]

    def get_response(self, user_input: str, author: str) -> str:
        lowered = user_input.lower()

        if lowered == '':
            return 'Silent treatment, eh?'
        elif "/commands" in lowered:
            return ("/Roll: Will output a random number between 1 and the inputted number (ex: /Roll 20, will roll "
                    "between 1 and 20) \n\n"
                    "/AddCharacter: Will add a playable character to the campaign, include name, class, level, and "
                    "race (ex: /AddCharacter Majax, Warlock 1, Elf) \n\n "
                    "/RemoveCharacter: Will remove the named character \n\n "
                    "/CampaignStory: Will select the DND campaign story to follow "
                    "(ex: /CampaignStory The Lost Mines of Phandelver) \n\n"
                    "/BeginCampaign: Will start the campaign \n\n"
                    "/RewriteStory: allows you to rewrite a story event that occurred \n\n"
                    "/stopstory: Ends the current campaign (this action cannot be undone) \n\n"
                    "~_: allows players to input what action they will preform in the game "
                    "(ex: ~I will use my charisma to charm the dragon)")
        elif '/roll' in lowered:
            try:
                num = int(lowered.split('/roll')[1].strip())
                return f'You rolled: {randint(1, num)}'
            except (IndexError, ValueError):
                return 'Please provide a valid number of dice sides after /roll'
        elif '/addcharacter' in lowered:
            character = lowered.replace("/addcharacter", "").strip()
            if character:
                self.conversation_history.append({"role": "user", "content": f'{author} will play as {character}'})
                return f'Character added for {author}'
            else:
                return 'Please provide a character name, race, class, and level after /addcharacter'
        elif '/begincampaign' in lowered:
            self.conversation_history.append({"role": "user", "content": 'Start the Campaign!'})
            try:
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=self.conversation_history
                )
                assistant_response = response.choices[0].message.content
                self.conversation_history.append({"role": "assistant", "content": assistant_response})
                return assistant_response
            except Exception as e:
                return f"Error: {str(e)}"
        elif '/stopstory' in lowered:
            self.conversation_history.clear()
        elif '/removecharacter' in lowered:
            character = lowered.replace("/removecharacter", "").strip()
            if character:
                self.conversation_history.append(
                    {"role": "user", "content": f'{character} was removed from the campaign'})
                return f'Character removed'
            else:
                return 'Please provide a character name after /removecharacter'
        elif '/rewritestory' in lowered:
            rewrite = lowered.replace("/rewritestory", "").strip()
            if rewrite:
                self.conversation_history.append(
                    {"role": "user", "content": f'The story will be rewritten to {rewrite}'})
                return 'Story has been rewritten'
            else:
                return 'Please provide a character name after /removecharacter'
        elif '/campaignstory' in lowered:
            story = lowered.replace('/campaignstory', "").strip()
            if story:
                self.conversation_history.append({"role": "user", "content": f"The campaign's story will be {story}"})
                return f'Campaign story set to: {story}'
            else:
                return 'Please provide the campaign story after /campaignstory'
        elif '~' in lowered:
            self.conversation_history.append({"role": "user", "content": f'{author} wrote "{user_input}"'})
            try:
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=self.conversation_history
                )
                assistant_response = response.choices[0].message.content
                self.conversation_history.append({"role": "assistant", "content": assistant_response})
                return assistant_response
            except Exception as e:
                return f"Error: {str(e)}"

        return "0000000000000000000"
