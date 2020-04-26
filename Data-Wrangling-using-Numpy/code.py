# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path, delimiter = ',', skip_header = 1)
print(data)

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
# Appending the two datas
census = np.array(np.concatenate((data, new_record)))
print(census)






# --------------
#Code starts here
#age 
age = np.array(census[:, [0]])
# max_age
max_age = age.max()
print(max_age)

#min_age
min_age = age.min()
print(min_age)

#age_mean
age_mean = age.mean()
print(age_mean)

#age_std
age_std = age.std()
print(age_std)


# --------------
#Code starts here
c = census[:, 2]
#race_0
race_0 = np.array(census[census[:, 2]==0])
#race_1
race_1 = np.array(census[census[:, 2]== 1])
#race_2
race_2 = np.array(census[census[:, 2] == 2])
#race_3
race_3 = np.array(census[census[:, 2] == 3])
#race_4
race_4 = np.array(census[census[:, 2] == 4])

#Length of arrays
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
print(len_0, len_1, len_2, len_3, len_4, sep='\n')

#minority race
mini = min(len_0, len_1, len_2, len_3, len_4)
if mini == len_0:
    minority_race = 0
elif mini == len_1:
    minority_race = 1
elif mini == len_2:
    minority_race = 2
elif mini == len_3:
    minority_race = 3
else: 
    minority_race = 4
print(minority_race)



# --------------
#Code starts here
#senior_citizens
senior_citizens = census[census[:,0] > 60]

#working_hour
working_hours_sum = senior_citizens.sum(axis = 0)[6]
print(working_hours_sum)

#Length of senior citizen
senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)

#average working hour of Senior citizens
avg_working_hours = working_hours_sum / senior_citizens_len
print(avg_working_hours)




# --------------
#Code starts here
#Subset arrays of census
high = census[census[:, 1] > 10]
low = census[census[:, 1] <= 10]


#average pays of both classes of educated_peoples
avg_pay_high = high.mean(axis = 0)[7]
avg_pay_low = low.mean(axis = 0)[7]
print(avg_pay_high)
print(avg_pay_low)







