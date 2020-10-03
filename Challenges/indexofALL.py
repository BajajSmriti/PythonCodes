def findIndex(list1 , ele):
    list2=[]
    for i in range(len(list1)):
        val = list1[i]
        print(val)
        if isinstance(val, list):
            for x in findIndex(val,ele):
                print("XXX",x)
                list2.append([i]+x)
        elif val==ele:
            list2.append([i])
            print(i)
    return list2


print("ans",findIndex([[[1,2,3],2,[1,3]],[1,2,3]], 2))
