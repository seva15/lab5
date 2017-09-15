def names(arr):
    list_name = list()
    for p in emp:
        for i in p["children"]:
            if i["age"] > 18:
                list_name.append(p['name'])
                break
    return list_name



ivan = {"name" : "ivan",
        "age":34,
        "children":[{"name" : "vasja","age":16}] }

andrew = {"name" : "andrew",
          "age":25,
          "children":[{"name" : "masha" ,"age":2}] }

victor = {"name" : "victor",
          "age":55,
          "children":[{"name" : "vasja","age":25}] }

emp = [ivan,andrew,victor]
list_name = names(emp)
print(list_name)



