from datetime import datetime
from rapidsms.models import Connection, Contact, Backend
from ureport.tests.functional.test_utils import create_group, create_user, create_connection, create_poll,\
    create_fake_response, add_contacts_to_poll
from fixtures.create_poll_utils import if_exists_delete_user, if_exists_delete_group, if_exists_delete_backend, if_exists_delete_contact, simulate_response
from ureport_project.rapidsms_ureport.ureport.models import UreportContact


def create_polls(number_of_polls):
    group_name = 'Pagination Group'
    username_1 = 'FT_HP_USER_1'
    username_2 = 'FT_HP_USER_2'
    backend = 'dmark'
    contact_name_1 = 'FUNCT_HP_CONTACT_1'
    contact_name_2 = 'FUNCT_HP_CONTACT_2'

    if_exists_delete_contact(contact_name_1)
    if_exists_delete_contact(contact_name_2)
    if_exists_delete_user(username_1)
    if_exists_delete_user(username_2)
    if_exists_delete_group(group_name)
    if_exists_delete_backend(backend)

    group = create_group(group_name=group_name)

    user1 = create_user(username=username_1, email=('%s@bar.com' % username_1), group=group)
    user2 = create_user(username=username_2, email='shaggy@scooby.com', group=group)

    contact1 = Contact.objects.create(name=contact_name_1, user=user1, gender='M', birthdate=datetime.now(), language="en")
    contact2 = Contact.objects.create(name=contact_name_2, user=user2, gender='F', birthdate=datetime.now(), language="en")

    contact1.groups.add(group)
    contact2.groups.add(group)

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

    return polls
