def deco(func):
     def wrap(self):
        print("*" * 20)
        func(self)
        print("*" * 20)
     return wrap


class Report:
    template = "Student Report"

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def change_template(cls, new_template):
        cls.template = new_template

    def __str__(self):
        return (
            f"Template: {self.template}\n"
            f"Title: {self.title}\n"
            f"Content: {self.content}"
        )

    @deco
    def show(self):
        print(self)


Report.change_template("Project Report")

r = Report("Python Project", "Report using OOP Concepts")

r.show()