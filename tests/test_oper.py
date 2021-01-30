from segT import oper
def test_build():
    arr = [1,2,3,4,5,6,7]
    segt = oper.build(arr, 'sum')
    print(oper.query(arr, 2, 4, segt, 'sum'))
    oper.update(arr, 2, 6, segt, 'sum')
    print(oper.query(arr, 2, 4, segt, 'sum'))
