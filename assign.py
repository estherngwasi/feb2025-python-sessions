#CREATING AN EMPTY LIST
my_list = []
#APPENDING 10,20,30,40 TO THE LIST
my_list.append( 10)
my_list.append( 20)
my_list.append( 30)
my_list.append( 40)
#INSERTING 15 ON THE SECOND POSITION IN THE LIST
my_list.insert(1,15)
#EXTENDING WITH ANOTHER LIST
my_list.extend([50,60,70])
#REMOVING THE LAST ELEMENT IN THE LIST
my_list.pop(-1)
#SORTING THE LIST IN ASCENDING ORDER
my_list.sort()
#FINDING AND PRINTING INDEX OF 30
index_30 = my_list.index(30)
print("Index of 30:", index_30)

