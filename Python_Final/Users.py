import abc

class User(metaclass=abc.ABCMeta):

    def __init__(self, username, password, firstName, lastName):
        self.username = username
        self.password = password
        self.firstName = firstName
        self.lastName = lastName

    def getPassword(self):
        return self.password

    def setPassword(self,password):
        self.password = password

    @abc.abstractmethod
    def get_info(self):
        pass


class student(User):

    def __init__(self,username, password, firstName, lastName,major):
        super().__init__(username, password, firstName, lastName)
        self.major = major

    def get_info(self):
        return "Student: "+self.firstName+" "+self.lastName+" "+self.major

    def set_major(self,major):
        self.major = major

class professor(User):

    def __init__(self,username, password, firstName, lastName):
        super().__init__(username, password, firstName, lastName)
        self.subjects = []

    def get_info(self):
        return "Professor: "+self.firstName+" "+self.lastName

    def add_subject(self,subject):
        self.subjects.append(subject)

    def get_subjects(self):
        return self.subjects


class admin(User):
    def __init__(self, username, password, firstName, lastName):
        super().__init__(username, password, firstName, lastName)

    def get_info(self):
        return "ADMIN: "+self.firstName+" "+self.lastName











