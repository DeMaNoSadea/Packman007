from mongoengine import connect, Document, StringField, DateField, IntField


connect("task")


class NewMyModel(Document):
    collect = {"collection": "Collection_for_task"}
    name = StringField(required=True)
    author = StringField(required=True, default="admin")
    count = IntField(default=0)
    date = DateField(required=True)
