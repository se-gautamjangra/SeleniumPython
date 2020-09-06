from utilities.mysql_utils import MysqlUtils
import unittest

class DatabaseTest(unittest.TestCase):

    def test_mysql_operations(self):
        connection = MysqlUtils(host='localhost', port=3306, user='root', password='root', database='test')
        #Assuming that our table have the fields id and name in this order.
        #we can use this way but the parameter should have the same order that table
        #connection.insert('table_name',parameters to insert)
        connection.insert('person',1, 'Peter Malan')
        #in this case the order isn't matter
        #connection.insert('table_name', field=Value to insert)
        connection.insert('person',name='Peter Malan', id=1)
        #connection.select('Table', where="conditional(optional)", field to returned)
        connection.select('person', where="name = 'Peter Malan' ")
        connection.select('person', None,'id','name')
        #connection.update('Table', id, field=Value to update)
        connection.update('person', 1, name='Harry')
        #connection.delete('Table', id)
        connection.delete('person', 1)
        #connection.call_store_procedure(prodecure name, Values)
        connection.call_store_procedure('search_users_by_name', 'Harry')