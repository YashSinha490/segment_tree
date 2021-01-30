# ABOUT
This is a generic implementation of segment trees for python3.
 * segment trees helps us to do range queries and updates in O(logN) time.
 * it has built in support for operations such as min, max, xor, sum etc.
 * it is currently limited to point updates.
 * python2 is not currently supported.
 
# INSTALLATION
* pip install segT

# USAGE
   from segT import oper <br/>
   arr = [1,2,3,4,5,6,7]
   
   * build segment tree <br/>
   tree = oper.build(arr, 'xor')
   
   * range query in O(logN) <br/>
   print(oper.query(arr, left_index, right_index, tree, 'xor'))
   
   * point update in O(logN) <br/>
   oper.update(arr, left_index, right_index, tree, 'xor')
   
# TESTS
* execute python setup.py test to run tests
