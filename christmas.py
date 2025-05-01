trees = [1, 3, 4, 7, 3, 6, 8, 9, 3, 10, 9, 4, 8, 13, 17]
ascend = 0
descend = 0
high_ascend = 0
high_descend = 0
   
for index, i in enumerate(trees):

    print(f"i is {i}")
    print(f"index is {index}")
    print(f"Compared number is {trees[index - 1]}")



    if index != 0:
        if i > trees[index - 1]:
            ascend += 1
        else:
            ascend = 1
        
        if i < trees[index - 1]:
            descend += 1
        else:
            descend = 1


    if ascend > high_ascend:
        high_ascend = ascend

    if descend > high_descend:
        high_descend = descend


    print(f"Current ascend: {ascend}")
    print(f"Current high_ascend: {high_ascend}")
    print(f"Current descend: {descend}")
    print(f"Current high_descend: {high_descend}")


print(high_ascend)
print(high_descend)
        