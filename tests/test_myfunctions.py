from segT import myfunctions
def test_build():
    arr = [1,2,3,4,5,6,7]
    segt = myfunctions.build(arr, 'sum')
    print(myfunctions.query(arr, 2, 4, segt, 'sum'))
    myfunctions.update(arr, 2, 6, segt, 'sum')
    print(myfunctions.query(arr, 2, 4, segt, 'sum'))
