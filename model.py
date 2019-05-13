from document_model.model_bd import NewMyModel
import datetime


class TaskClass:
    def __init__(self, author, name):
        try:
            document = NewMyModel.objects.get(author=author, name=name)
            print("try")
        except Exception as e:
            print(f"{e}")
            document = NewMyModel()
            document.author = author
            document.name = name
            document.date = datetime.date.today()
            document.save()
        self.document = document

    def counter(self):
        if getattr(self.document, "private", False) is False:
            self.document.count += 1
            self.document.save()
        print(getattr(self.document, "private", None))

    def private_tru(self):
        setattr(self.document, "private", True)
        self.document.save()

    def private_false(self):
        try:
            setattr(self.document, "private", False)
            self.document.save()
        except:
            raise Exception("No private document")


NewTask = TaskClass(author="Semen", name="New_Docs")
print(NewTask)
