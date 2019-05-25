text = 'the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car'

words = text.split()

unique_word = list()

print(words)

for word in words:
    if word not in unique_word:
        unique_word.append(word)

# diff word
print(unique_word)

# init word
counts = [0]*len(unique_word)

for word in words:
    index = unique_word.index(word)
    counts[index] = counts[index]+1

print(counts)

big_count = None
big_word = None

for i in range(len(counts)):
    if big_count is None or counts[i] > big_count:
        big_word = unique_word[i]
        big_count = counts[i]

print(big_count, big_word)

names = ['小赵', '小钱', '小孙', '小李', '小王', '小张']
friends = [45, 100, 67, 136, 77, 17]

max_name = None
max_count = None

for i in range(len(friends)):
    if max_count is None or friends[i] > max_count:
        max_name = names[i]
        max_count = friends[i]

print(max_count, max_name)

# solu 2

maxFriend = max(friends)
maxName = names[friends.index(maxFriend)]

print(maxFriend,maxName)
