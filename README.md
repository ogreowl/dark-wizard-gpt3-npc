# Dark_Wizard_AI_NPC

<font size=”6”>**Description:**</font>

This project uses OpenAI's GPT-3 to make a "dark wizard" non-playable character. In this iteration, the player can say anything they want to the NPC, and the NPC will respond in the character of an evil wizard that uses dark magic. This project shows how cutting-edge language models can be easily implemented to make more immersive non-playable characters in video games.

*

<font size=”32”>**Example:**</font>

<img width="594" alt="demonstration" src="https://user-images.githubusercontent.com/86581611/207442135-4423f571-ebb2-47c2-b852-590187eba7b4.png">
All lowercase text is the player's input. The text with normal capitalization is the AI's output. 

*

<font size=”32”>**How:**</font>

This program takes in a string from the user, and then gives the user's input to GPT-3, along with some added context on how GPT-3 should respond. Then, it outputs GPT-3s response on-screen, presented as a line of dialogue from the NPC. This program also saves the player's input and GPT-3's output as context for GPT-3's future responses. 

*

<font size=”32”>**Limitations:**</font>

1: Calling the GPT-3 API costs a small amount of money (currently ranges from $0.02 cents to $0.0004 cents per 750 words, depending on the language model used). Though it's already pretty cheap and will get cheaper over time, this technology can become costly if implemented into a video game that's brought to a mass market.

2: Calling GPT-3 also takes a slight amount of time. This could present difficulties in a much larger project.

3: The AI can easily break character if a player decides to troll it. Ask it about the 2020 election, and the AI will tell you about Trump and Hillary. A possible solution to this is to give the player a limited number of dialogue options that they can choose to ask the AI.

4: Even when given a carefully curated input, there is always a small chance that the AI gives an undesirable response.

5: The AI has a limited memory. In this iteration, the AI can remember up to 3 back-and-forth interactions with the player. Its memory can be easily increased from, there is likely a non-trivial cap of how many past interactions the NPC can remember.

*

<font size=”32”>**Suggestions for future research:**</font>

1: People should try using GPT-3 to make other parts of video games more immersive. For example. after a player buys an item, steals something, or casts a spell, NPCs can generate original lines of dialogue.

2: People should experiment with giving GPT-3 different instructions for how to respond with the player. With this technology, it's definitely possible to create a more complex character with a backstory, motivation, passions, fears, etc.

3: OpenAI's image generation APIs (DALLE) and music APIs (Jukebox) should also be experimented with to see if they can be implemented in video games. 
