def num_days(month):
    months = ('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec')
    idx = months.index(month)

    if idx == 1:
        print('number of days in', month, 'is', 28)
    elif idx in [0,2,4,6,7,9,11]:
        print('number of days in', month, 'is', 31)
    else:
        print('number of days in', month, 'is', 30)

num_days('feb')
