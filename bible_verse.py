# This saves the feeling so we can respond to it.
emotion = input('\nHow are you feeling? ')

# A list of words that refer to being scared.
scared_words = [
'frightened', 
'afraid', 
'fearful', 
'nervous', 
'panicky', 
'agitated', 
'alarmed', 
'worried', 
'intimidated', 
'terrified', 
'petrified', 
'horrified',
'scared'
]

# Loops through all of the scared emotions, 
# & gives a bible verse.
for word in scared_words:
	if emotion.lower() == word:
		print('\n1 Peter 5:7 NLT\n"Give all your worries and cares to God, for he cares about you."')

