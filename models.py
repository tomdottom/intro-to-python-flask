class NoSuchUserError(Exception):
    pass


class Members(object):

    def __init__(self):
        self._members = []

    def get(self, mid):
        try:
            return self._members[mid]
        except IndexError:
            raise(NoSuchUserError(
                    'Could not find member with id: {}'.format(mid)))

    def list(self):
        return self._members

    def create(self, data):
        if self._member_exists(data['name']):
            api.abort(
                409,
                'Member with name \'{}\' already exists'.format(data['name'])
            )

        new_id = len(self._members)
        self._members.append({
            'id': new_id,
            'name': data['name']
        })
        return self._members[new_id]

    def _member_exists(self, name):
        return any(
            member
            for member in self._members
            if member['name'] == name
        )
