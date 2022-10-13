# create dict
# access dict

my_dict = {"let": "test", "cat": 2}

print("let is:")
print(my_dict["let"])

print('type "1" to access "let".')
select = int(input("what num do you want: 1 or 2?"))

if select == 1:
    num = "let"

print(my_dict[num])
