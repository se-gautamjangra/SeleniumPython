from utilities.database_connector import DatabaseConnector
import unittest


class MysqlTests(unittest.TestCase):
    mysql_connector = DatabaseConnector()

    def test_fetch_departments(self):
        departments = self.mysql_connector.run_select('select * from departments')
        for department in departments:
            if department[0] == 110:
                self.assertEqual(department[0], 110, 'Department with 110 not found')
                self.assertEqual(department[1], 'Security and transport',
                                 'Department - Security and transport not found')

    def test_add_employee(self):
        insert_query = "insert into employees (first_name,last_name,date_of_birth,gender,hire_date) values ('Shelly','White','1987-09-11','F','2010-10-10')"
        new_emp_id = self.mysql_connector.run_non_select(insert_query)
        print('Employee Id -> ' + str(new_emp_id))
        self.assertIsNot(new_emp_id, None, 'Employee not added')

    def test_fetch_employee(self):
        employee_details = self.mysql_connector.run_select('select * from employees e where e.emp_no = 1106')
        for employee in employee_details:
            self.assertEqual(employee[0], 1106, 'employee id not matched')
            self.assertEqual(employee[1], 'Shelly', 'first name not matched')
            self.assertEqual(employee[2], 'White', 'first name not matched')
            self.assertEqual(str(employee[3]), '1987-09-11', 'last name not matched')
            self.assertEqual(employee[4], 'F', 'gender not matched')
            self.assertEqual(str(employee[5]), '2010-10-10', 'hiring date not matched')
