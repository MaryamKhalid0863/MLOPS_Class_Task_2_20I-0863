class StudentsInMLOps:
    def __init__(self):
        self.students = 0
        self.class_name = "StudentsInMLOps"
    
    def enrollStudents(self, count):
        self.students += count

    def dropStudents(self, count):
        self.students = max(0, self.students - count)

    def getTotalStrength(self):
        return self.students

    def getClassName(self):
        return self.class_name

