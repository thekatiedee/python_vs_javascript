# create dict
# access dict
def another_test():

    my_dict = {"cat": 27, "dog": 3, "rabbit": 2}

    # display the items in a dict in a for loop

    # prints values
    for x in my_dict:
        print(my_dict[x])

    # prints keys
    for x in my_dict:
        print(x)

    # prints both with a space between
    for x in my_dict:
        print(x, my_dict[x])

    # dict not list

    # if select == 1:
    #     num = "let"
    # elif select == 2:
    #     num = "cat"
    # else:
    #     print("sorry! wrong num choice.")

    # print(my_dict[num])


# print specific values based on keys
# def my_test():

#     my_dict = {"let": "this is what let is", "cat": 27}

#     print("let is:")
#     print(my_dict["let"])

#     print('type "2" to see how many cats i have.')
#     select = int(input("what num do you want: 1 or 2?"))

#     if select == 1:
#         num = "let"
#     elif select == 2:
#         num = "cat"
#     else:
#         print("sorry! wrong num choice.")

#     print(my_dict[num])


if __name__ == "__main__":
    another_test()


# # make a function that returns 3 items


#     def my_func():
#         print("this is a test")
