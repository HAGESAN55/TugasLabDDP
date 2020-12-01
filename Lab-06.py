def jumlah_batas(nums, batas):
    nilai = 0
    for i in range(len(nums)):
        if nums[i] > batas:
            nilai += nums[i]
    print(nilai)
def list_nonvokal(s):
    hurufvokal='aiueoAIUEO'
    hasilarray=[]
    for a in s:
        if a not in hurufvokal:
            hasilarray += a
    print(hasilarray)
def list_modify(alist, command, position, value=None):
    if command == 'add':
        if position == 'start':
            alist.insert(0, value)
        elif position == 'end':
            alist.append(value)
        print(alist)
    elif command == 'remove':
        if position == 'start':
            alist.remove(alist[0])
        elif position == 'end':
            alist.remove(alist[-1])
        print(alist)
jumlah_batas([3,5,6,4,10,1,2], 4)
list_nonvokal('sayang kamu celalu')
list_modify(['jantan', 'betina', 'janbet', 'betjan'], 'add', 'end', 'najteb')