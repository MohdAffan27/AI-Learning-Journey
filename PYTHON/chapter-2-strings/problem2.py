#use replace function
letter = '''Dear <|Name|>,
you are selected!
on <|Date|>'''
print(letter.replace("<|Name|>","Affan").replace("<|Date|>","24 July 2026")) 
#generates the new strings because strings can't be changed hence immutable