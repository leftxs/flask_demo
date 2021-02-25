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

    def user_list(self):
        # Get all the users from the users variable and exclude the bio since the list requires
        # less information to be sent to the client. If all the information from a user is needed,
        # rely on GET /users/<user_id>
        users = list(map(lambda user: {key: user[key]
                                       for key in user if key != 'bio'}, self.users))

        return users

    def add_user(self, payload):
        user = self.__create_user_element(payload)
        self.users.append(user)
        return user

    def get_user(self, user_id):
        filtered_users_list = list(
            filter(lambda user: user['id'] == user_id, self.users))
        return filtered_users_list[0]

    def update_user(self, user_id, payload):
        new_user = self.__create_user_element(payload, user_id)

        self.users = list(
            map(lambda user: user if user['id'] != user_id else new_user, self.users))
        return new_user

    def delete_user(self, user_id):
        self.users = list(
            filter(lambda user: user['id'] != user_id, self.users))

    def __create_user_element(self, payload, user_id=None):
        '''Private method for the user object creation base on the received payload'''
        user = {
            'id': self.users[-1]['id'] + 1 if user_id is None else user_id,
            'first_name': payload['first_name'],
            'last_name': payload['last_name'],
            'bio': payload['bio']
        }
        return user
