def merge(list1, list2):
    """将两个有序列表合并成一个新的有序列表"""
    clist = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            clist.append(list1[i])
            i += 1
        else:
            clist.append(list2[j])
            j += 1

    if i == len(list1):
        clist += list2[j:]
    else:
        clist += list1[i:]
    return clist
