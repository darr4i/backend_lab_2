import datetime

class User:
    user_id_counter = 1
    users = {}

    def __init__(self, name):
        self.id = User.user_id_counter
        self.name = name
        User.users[self.id] = self
        User.user_id_counter += 1

    @classmethod
    def get_user(cls, user_id):
        return cls.users.get(user_id)

    @classmethod
    def get_all_users(cls):
        return list(cls.users.values())


class Category:
    category_id_counter = 1
    categories = {}

    def __init__(self, name):
        self.id = Category.category_id_counter
        self.name = name
        Category.categories[self.id] = self
        Category.category_id_counter += 1

    @classmethod
    def get_category(cls, category_id):
        return cls.categories.get(category_id)

    @classmethod
    def get_all_categories(cls):
        return list(cls.categories.values())


class Record:
    record_id_counter = 1
    records = {}

    def __init__(self, user_id, category_id, amount):
        self.id = Record.record_id_counter
        self.user_id = user_id
        self.category_id = category_id
        self.date = datetime.datetime.now()
        self.amount = amount
        Record.records[self.id] = self
        Record.record_id_counter += 1

    @classmethod
    def get_record(cls, record_id):
        return cls.records.get(record_id)

    @classmethod
    def get_records_by_user(cls, user_id):
        return [record for record in cls.records.values() if record.user_id == user_id]

    @classmethod
    def get_records_by_category(cls, category_id):
        return [record for record in cls.records.values() if record.category_id == category_id]

    @classmethod
    def get_all_records(cls):
        return list(cls.records.values())
