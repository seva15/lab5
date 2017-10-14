# coding: utf8
from getID import *
from getFriends import *
from Make_gist import *

nick = raw_input("Введите пользователя\n")
user = GetUserID(nick)
us_id = user.get_data()

fr = Friends(us_id)
fr_list = fr.make_list()
print(fr_list)

 #make_gist(count_bdate(fr_list))

