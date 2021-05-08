import string 

#To open text file:
first_file =open("/home/ahmed/Assignment_cloud/Docker/Beyond_the_Wall_of_Sleep")
#Make a list to save the first in it:
list1=[]
book1=first_file.read()
book1=book1.lower()
#To split punctuations from the text:
op_string = book1.translate(str.maketrans('', '', string.punctuation))
book_Beyond=op_string.split()
list1=book_Beyond
print("The number of words in the first book :",len(list1))
#To remove the repeated words in the list
list1 = list( dict.fromkeys(list1) )
print("The number of unique words in the first book : ",len(list1))


#To open text file:
second_file = open("/home/ahmed/Assignment_cloud/Docker/Pride and Prejudice")
#Make a list to save the second book in it:
list2=[]
book2=second_file.read()
book2=book2.lower()
#To split punctuations from the text:
op_string2= book2.translate(str.maketrans('', '', string.punctuation))
book_Pride=op_string2.split()
list2=book_Pride
print("The number of words in the second book :",len(book_Pride))
#To remove the repeated words in the list
list2= list( dict.fromkeys(list2) )
print("The number of unique words in the first book : ",len(list2))


#Make a list to save the similar words between the two books in it:
list3=[]
#Make a list with the unuseful words that we do not need :
list4=['i', 'you', 'he', 'she', 'it', 'we', 'they',	'mine', 'yours', 'his', 'hers', 'ours', 'theirs',
'which', 'who', 'that','this', 'these', 'those','is','are','after', 'before', 'in','on','at','of','a','the',
'us','the','an']
for i in range(7827):
    for j in range(1548):
        if(list2[i]==list1[j]  not in list4):
             list3.append(list2[i])
             break             
#To remove the repeated words in the list
list3 = list( dict.fromkeys(list3) )
print("The number of the similar words between the two books :",len(list3))
print(list3)
