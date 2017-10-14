import datetime
#import matplotlib.pyplot as plt


def count_bdate(bdate_list):
    ages = []
    curr_date = datetime.date.today()
    for i in bdate_list:
        temp_d = i.split(sep='.')
       
        if int(curr_date.month) > int(temp_d[1]):
            ages.append(int(curr_date.year) - int(temp_d[2]))
      
        elif int(curr_date.month) == int(temp_d[1]):
            if int(curr_date.day) > int(temp_d[2]):
                ages.append(int(curr_date.year) - int(temp_d[2]))
          
            else:
                ages.append(int(curr_date.year) - int(temp_d[2]) - 1)
       
        elif int(curr_date.month) < int(temp_d[1]):
            ages.append(int(curr_date.year) - int(temp_d[2]) - 1)

    return ages

#def make_gist(ages):
   # plt.hist(ages)
   # plt.show()

