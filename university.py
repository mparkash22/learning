class University:
    # Hello anoop, ,this is just a test
    def __init__(self, name, role, holidays):
        print('Constructor called')
        self.name = name
        self.role = role
        self.holiday_var = 0

    def print_details(self):
        print("{} : {}".format(self.name, self.role))
        print('Holidays: {}'.format(self.holiday_var))
        print('---------------------------------------')

    def holiday(self, number):
        self.holiday_var = number

class NTU(University):
    def print_details(self):
        print("{} : {}".format(self.name, self.role))


uni_obj = University('Alice', 'teacher', 100)

uni_obj.print_details()
uni_obj.holiday(100)
uni_obj.print_details()

ntu_obj = NTU('Alex', 'Student', 10)
ntu_obj.print_details()