from datetime import datetime
from rapidsms.models import Connection, Contact, Backend
from ureport.tests.functional.test_utils import create_group, create_user, create_connection, create_poll,\
    create_fake_response, add_contacts_to_poll


def create_polls_with_fake_resposes(number_of_polls):
    group = create_group(group_name='Pagination Group')
    user1 = create_user(username="foo", email='foo@bar.com', group=group)
    user2 = create_user(username='fred', email='shaggy@scooby.com', group=group)

    contact1 = Contact.objects.create(pk=567, name='FT1', user=user1, gender='M', birthdate=datetime.now(), language="en")
    contact2 = Contact.objects.create(pk=765, name='FT2', user=user2, gender='M', birthdate=datetime.now(), language="en")
    contacts = [contact1, contact2]

    backend = Backend.objects.create(name='dmark')

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
