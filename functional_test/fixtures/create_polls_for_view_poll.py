from datetime import datetime
from rapidsms.models import Connection, Contact, Backend
from ureport.tests.functional.test_utils import create_group, create_user, create_connection, create_poll,\
    create_fake_response, add_contacts_to_poll
from fixtures.create_poll_utils import if_exists_delete_user, if_exists_delete_group, if_exists_delete_backend


def create_polls_with_fake_responses(number_of_polls):
    group_name = 'Pagination Group'
    username1 = 'foo'
    username = 'fred'
    backend = 'dmark'

    if_exists_delete_group(group_name)
    if_exists_delete_user(username1)
    if_exists_delete_backend(backend)

    group = create_group(group_name=group_name)
    user1 = create_user(username=username1, email=('%s@bar.com' % username1), group=group)
    if_exists_delete_user(username)
    user2 = create_user(username=username, email='shaggy@scooby.com', group=group)

    contact1 = Contact.objects.create(pk=567, name='FT1', user=user1, gender='M', birthdate=datetime.now(), language="en")
    contact2 = Contact.objects.create(pk=765, name='FT2', user=user2, gender='M', birthdate=datetime.now(), language="en")
    contacts = [contact1, contact2]

    backend = Backend.objects.create(name=backend)

    connection1 = create_connection('0794339344', contact1, backend)
    connection2 = create_connection('0794339427', contact2, backend)
    connections = [connection1, connection2]

    polls = []
    for poll in range(1, number_of_polls):
        poll = create_poll(user1)
        add_contacts_to_poll(poll, contacts)
        poll.add_yesno_categories()
        poll.save()
        polls.append(poll)

        for connection in connections:
            create_fake_response(connection, 'yes')

    return polls
