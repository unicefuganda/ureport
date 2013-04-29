from datetime import datetime
from rapidsms.models import Connection, Contact, Backend
from fixtures.create_poll_utils import if_exists_delete_user, if_exists_delete_group, \
    if_exists_delete_backend, if_exists_delete_contact, create_poll, create_group, create_user, create_connection, \
    add_contacts_to_poll, simulate_response


def create_and_start_polls(number_of_polls):
        polls = create_polls(number_of_polls)
        for poll in polls:
            poll.start()

            lastResponseText = 'yes'
            for contact in poll.contacts.all():
                responseText = 'yes' if (lastResponseText == 'no') else 'no'
                lastResponseText = responseText
                simulate_response(contact.default_connection, responseText)

            poll.end()


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

    create_connection('0794339344', contact1, backend)
    create_connection('0794339427', contact2, backend)

    polls = []
    for i in range(1, number_of_polls):
        poll = create_poll(user1, "FT_HP_POLL_" + str(i), "WHAT IS THE ANSWER?")
        add_contacts_to_poll(poll, contacts)
        poll.add_yesno_categories()
        poll.save()
        polls.append(poll)

    return polls
