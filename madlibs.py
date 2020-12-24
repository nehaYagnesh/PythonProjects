# # string concatenation 
# # create a string : 'subscribe to ______'

# channel ='Neha Yagnesh' 

# # a few ways of string concatenation
# print('Subscribe to ' + channel)
# print('Subscribe to {}'.format(channel))
# print(f'Subscribe to {channel}')

adj = input('Adjective: ')
verb1 = input('Verb: ')
verb2 = input('Verb: ')
adj2 = input('Adjective: ')
famous_person = input('Famous person: ')

madlib = f'Python programming is {adj}.I love to {verb1} and {verb2}. Also help others and be {adj2} \
as you are {famous_person}'

print(madlib)