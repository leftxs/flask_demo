class DataExample():
    def __init__(self):
        self.users = [
            {
                'id': 1,
                'first_name': 'Pedro',
                'last_name': 'Martinho',
                'bio': 'Information you can only read in the show used detail endpoint'
            }
        ]

    def add_user(self, user):
        user = {
            'id': self.users[-1]['id'] + 1,
            'first_name': user['first_name'],
            'last_name': user['last_name'],
            'bio': user['bio']
        }
        self.users.append(user)

    def get_user(self, user_id):
        self.users = list(
            filter(lambda user: user['id'] == user_id, self.users))

    def delete_user(self, user_id):
        self.users = list(
            filter(lambda user: user['id'] != user_id, self.users))

    def user_list(self):
        # Get all the users from the users variable and exclude the bio since the list requires
        # less information to be sent to the client. If all the information from a user is needed,
        # rely on GET /users/<user_id>
        return list(map(lambda user: {key: user[key]
                                      for key in user if key != 'bio'}, self.users))
