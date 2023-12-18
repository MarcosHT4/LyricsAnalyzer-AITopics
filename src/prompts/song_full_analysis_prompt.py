ANALYSIS_PROMPT = """Act as an expert in the field of musical lyrics and explain in a detailed and extensive manner,the meaning of a song.
The name of the song is "{name}" and it is performed by "{artist}".
You will be provided with a list of song sections, each one containing the name of the section (e.g. verse, chorus, bridge, etc.) and the lyrics of the section. {sections}
You must provide a detailed explanation of the meaning of each section, trying to not repeat the actual lyrics of the song, but rather explain the meaning of the lyrics. This explanation, apart from being detailed, must be extensive, not only a sentence or two, but rather a paragraph or two.
First, when explaining the meaning of each section, you must start with the an overall explanation of the section, and then, go to a more detailed explanation of the section, focusing on the connection between the current section and the other sections.
Second, you will need to explain the meaning of each section, based on three variables, the sentiment of the song, the emotion of the song, and the meaning of the album cover.
To be able to do this, you will be provided with three things: The overall sentiment of the song, which will contain two values: POSITIVE AND NEGATIVE, each one with a score from 0 to 1, and they both add up to 1. {sentiment}
The other thing you will be provided with is the overall emotion of the song, which will contain the top three emotions of the song, and their scores, which add up to 1. {emotion}
Finally, you will be provided with the overall meaning of the song's album cover, which will contain an overall meaning of what is seen in the album cover. {album_cover}
When you have the output with each section, add a final section called "overall" and explain the overall meaning of the song.
The output you will provide, will be a list of explanations, one for each section. The output is defined as follows: {format_instructions}"""