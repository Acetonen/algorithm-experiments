from lettuce import *

from linked_lists.linked_list import LinkedList, Node


def get_linked_list(list_of_numbers):
    linked_list = LinkedList()

    for node in [Node(number) for number in list_of_numbers]:
        linked_list.add_in_tail(node)

    return linked_list


@step('I have list as (.*)')
def have_the_linked_list(step, list):  # noqa
    world.linked_list = get_linked_list(list.split(' '))


@step('I call .len method')
def call_th_length_method(step):  # noqa
    world.length = world.linked_list.len()


@step('I see the number of nodes in list as (\d+)')
def check_number(step, length):
    assert world.length == length, \
        "Got %d" % world.length
