MEANING_PROMPT = """Act as an expert in the field of musical lyrics and explain in a detailed and extensive manner,the meaning of a song.
You will be provided with a list of song sections, each one containing the name of the section (e.g. verse, chorus, bridge, etc.) and the lyrics of the section. {sections}
You must provide a detailed explanation of the meaning of each section, trying to not repeat the actual lyrics of the song, but rather explain the meaning of the lyrics. This explanation, apart from being detailed, must be extensive, not only a sentence or two, but rather a paragraph or two.
First, when explaining the meaning of each section, you must start with the an overall explanation of the section, and then, go to a more detailed explanation of the section, focusing on the connection between the current section and the other sections.
When you have the output with each section, add a final section called "overall" and explain the overall meaning of the song.
The output you will provide, will be a list of explanations, one for each section. The output is defined as follows: {format_instructions}"""