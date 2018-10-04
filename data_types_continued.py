#string

s = "i am a string."
print(type(s)) 			# say str

#boolean

yes = True
print(type(yes))

no = False
print(type(no))

#list -- ordered and changeable

alpha_list = ["a", "b", "c"]	#list initialization
print(type(alpha_list))
print(type(alpha_list[0]))
alpha_list.append("d")
print(alpha_list)

#tuple -- ordered and unchangebale

alpha_tuple = ("a", "b", "c")
print(type(alpha_tuple))

try:
	alpha_tuple[2] = "d"
except TypeError:
	print("we cant add the elements to tuples!")
print(alpha_tuple)
