# --------------
##File path for the file 
file_path 
#Function for reading
def read_file(path):
    file = open(path,'r')
    sentence = file.readline()
    return (sentence)
    file.close()
#Function call
sample_message = read_file(file_path)
#print the contents of text file
print(sample_message)
#Code starts here


# --------------
#Code starts here
#calling function for message 1&2
message_1 = read_file(file_path_1)

message_2 = read_file(file_path_2)

#printing the message 1
print(message_1)
#Printing message 2
print(message_2)
#defining a function Fuse_mg
def fuse_msg(message_a,message_b):
    quotient =  int(message_b) // int(message_a)
    return str(quotient)

#Calling the function
secret_msg_1 = fuse_msg(message_1,message_2)

print(secret_msg_1)




# --------------
#Code starts here
#Read the contents of msg 3
message_3 = read_file(file_path_3)
print(message_3)

#function definition
def substitute_msg(message_c):
    if message_c == 'Red':
        sub = 'Army General'
    elif message_c == 'Green':
        sub = 'Data Scientist'
    elif message_c == 'Blue':
        sub = 'Marine Biologist'
    return sub
#Print secret Value
secret_msg_2 = substitute_msg(message_3)
print(secret_msg_2)


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here

#Calling function read_file
message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)

#Print the contents of message
print(message_4, message_5,sep = '\n')

#Function definition
def compare_msg(message_d, message_e):
    a_list = message_d.split()
    b_list = message_e.split()
    c_list = []
    for i in a_list:
        for j in b_list:
            if j != i:
                a = True
            else:
                a = False
                break
        if a == True:
            c_list.append(i)
    final_msg = ' '.join(c_list)
    return final_msg

#Function calling
secret_msg_3 = compare_msg(message_4, message_5)

print(secret_msg_3)







# --------------
#Code starts here

#message6
message_6 = read_file(file_path_6)

print(message_6)

#function definition
def extract_msg(message_f):
    a_list = message_f.split()
    even_word = lambda x: len(x)%2 == 0
    b_list = list(filter(even_word, a_list))
    final_msg = ' '.join(b_list)
    return final_msg

#Function Call
secret_msg_4 = extract_msg(message_6)
print(secret_msg_4)


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here

#secret message develpopjia
secret_msg = ' '.join(message_parts)

#new function defnt
def write_file(secret_msg, path):
    file = open(path, 'a+')
    file.write(secret_msg)
    file.close()

#Function call
write_file(secret_msg, final_path)

print(secret_msg)










