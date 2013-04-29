from splinter import Browser
from django.contrib.auth.models import Group, User
from rapidsms.models import Connection, Backend, Contact
from poll.models import Poll
from rapidsms_httprouter.models import Message
from rapidsms_httprouter.router import get_router
from ureport.models import PollAttribute, PollAttributeValue
from ureport_project.rapidsms_ureport.ureport.models import UPoll


def create_group(group_name):
    group = Group.objects.create(name=group_name)
    return group


def create_user(username, email, group):
    user1 = User.objects.create(username=username, email=email)
    user1.groups.add(group)
    user1.save()
    return user1


def create_connection(identity, contact, backend):
    connection = Connection.objects.create(identity=identity, backend=backend)
    connection.contact = contact
    connection.save()
    return connection


def create_poll(user, name, question):
    poll_name = name
    question = question
    poll = Poll.objects.create(name=poll_name, question=question, user=user, type=Poll.TYPE_TEXT)

    if not PollAttribute.objects.filter(key='viewable').exists():
        PollAttribute.objects.create(key='viewable', key_type='bool', default=True)

    upoll = UPoll.objects.get(pk=poll.pk)
    upoll.set_attr('viewable', True)
    upoll.save()

    return poll


def add_contacts_to_poll(poll, contacts):
    for contact in contacts:
        poll.contacts.add(contact)
    poll.save()


def simulate_response(connection, incoming_message):
    router = get_router()
    incoming = router.handle_incoming(connection.backend.name, connection.identity, incoming_message)
    return incoming


def get_browser():
    return Browser('firefox')


def if_exists_delete_group(groupname):
    try:
        group = Group.objects.get(name=groupname)
        Group.delete(group)
    except Group.DoesNotExist:
        pass


def if_exists_delete_user(username):
    try:
        user = User.objects.get(username=username)
        User.delete(user)
    except User.DoesNotExist:
        pass

def if_exists_delete_contact(name):
    try:
        contact = Contact.objects.get(name=name)
        Contact.delete(contact)
    except Contact.DoesNotExist:
        pass


def if_it_exists_delete_poll_called(poll_name):
    try:
        poll = Poll.objects.get(name=poll_name)
        Poll.delete(poll)
    except Poll.DoesNotExist:
        pass

    if_exists_delete_group()
    if_exists_delete_user()


def if_exists_delete_backend(name):
    try:
        backend = Backend.objects.get(name=name)
        Backend.delete(backend)
    except Backend.DoesNotExist:
        pass

def create_poll_called(poll_name):
    group = create_group(group_name='Pagination Group')
    user = create_user(username="foo", email='foo@bar.com', group=group)
    poll = Poll.objects.create(name=poll_name, question="question", user=user, type=Poll.TYPE_TEXT)
    return poll
