# # Question = input("Enter any number, wanna confirm it mate \n")
# # Question = int(Question)
# #
# # print(Question)
#
# Review_Exercise1 = ('This has a "double quoted" statement')
#
# Review_Exercise2 = ("'This has a single quoted statement'")
#
# Review_Exercise3 = ("""It is a mistake to think time is going. Time is not going.
# Time is here until the world ends. It is you that is going. You don’t waste time. Time is infinite. You waste yourself.
# You are finite. It is you that grows old and die, time doesn’t. So make better use of yourself before you expire.
# And one of the worst things to do with time is comparing yourself to others.
# A cow eats grass and gets fat but if dog eats grass, it will die. Never compare yourself with others.
# Run your race. What works for one person may be that which will kill you. Focus on the gifts and talents God gave you
# and don’t be envious of the blessings He gave others .
#
# Both Lion and Shark are professional hunters, BUT:
# A Lion cannot hunt in the Ocean and a Shark cannot hunt in the jungle
# That a Lion cannot hunt in the ocean doesn't make him useless and that a Shark cannot hunt in the jungle doesn't also
# make him useless both have their own territory where they can do well
#
# If a rose smells better than tomatoes, It doesn't mean the rose can make a better stew. Don't try to compare yourself to
# others. You also have your own strength, look for it and build on it. All animals that exist, were in Noah's ark.
# A snail is one of those animals. If God could wait long enough for snails to enter Noah's ark; His door of grace
# won't close till you reach your expected position in life. Never look down on yourself, keep looking up. Remember that
# Broken crayons still colour.
# _Keep on pushing, you never can tell how close you are to your goal...!""")
#
# Review_Exercise4 = ("This is \
# a multiline code \
# that is printed on one line.")
#
#
#
# print(Review_Exercise1)
# print(Review_Exercise2)
# print(Review_Exercise3)
# print(Review_Exercise4)
#
#
#
# word = 'indices of this statememt'
# print(word[5])
#
#
#
# word = 'goal'
# print(word[0])
#
# slicing = word[1:]
# print(slicing)
#
# slicing = word[0 : -1]
# print(slicing)
#
# slicing = word[0 : 51]
# print(slicing)
#
# new = 'f' + 'o' + 'o' + 'd'
# print(new.upper())
#
# new_Word = 'new ' + word
# print(new_Word)
# print(len(new_Word))
#
# strings = 'bazinga'
# print(strings[2 : -1])
#
#
# grade = 90
# print(grade * 2.212)
#
#
# addition = 2
#
# while addition < 100:
#     addition = addition + 1
#     print(addition)

scores = [98, 71, 76, 87, 83, 90, 57, 79, 82, 94]
total = 0
count = 0
for grade in scores:
    total += grade
    count += 1
print(total)
print(count)

avg = total / count
print(avg)
print(f'average is {avg}')