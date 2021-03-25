class AllPasswords:
    def __init__(self, json_data):
        self.all = json_data

    def add_to_list(self, app_name, username, password):
        entry = {
            "name": app_name,
            "username": username,
            "pass": password
        }
        self.all.append(entry)
        print(self.all)
