MEANING_PROMPT = """Act as an expert in the field of musical lyrics and explain the meaning of a song.
You will be provided with a list of song sections, each one containing the name of the section (e.g. verse, chorus, bridge, etc.) and the lyrics of the section. {sections}
You must provide a detailed explanation of the meaning of each section, trying to not repeat the actual lyrics of the song, but rather explain the meaning of the lyrics.
The output you will provide, will be a list of explanations, one for each section. The output is defined as follows: {format_instructions}
When you have the output with each section, add a final section called "overall" and explain the overall meaning of the song."""