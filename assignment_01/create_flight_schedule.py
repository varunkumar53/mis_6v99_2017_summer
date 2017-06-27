
# coding: utf-8

# In[1]:

TailNumber=['T1','T2','T3','T4','T5','T6']


# In[143]:

Source_Destination = {'DAL HOU':65,'HOU AUS':45,'AUS DAL':50,'DAL AUS':50,'AUS HOU':45,'HOU DAL':65}

#Keys, Values = list(Source_Destination.keys())  , list(Source_Destination.values())

Ground_Time = {'DAL':30,'HOU':35,'AUS':25}


# In[151]:

route='AUS DAL'
military_time=1735
zeropad_time=('{:04}'.format(military_time))
min_midnight=(int(str(zeropad_time)[:2])*60)+(int(str(zeropad_time)[2:]))
destination_time=min_midnight+Source_Destination[route]
destination_time


# In[152]:

reach_time=str('{:02}'.format(destination_time//60))+('{:02}'.format(destination_time%60))
print(reach_time)


# In[153]:

min_midnight_afr_grnd=destination_time+Ground_Time[(str(route)[4:])]
nextdep_time=str('{:02}'.format(min_midnight_afr_grnd//60))+('{:02}'.format(min_midnight_afr_grnd%60))
print(nextdep_time)

