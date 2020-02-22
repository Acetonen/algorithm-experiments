from lettuce import *

from project.linked_lists.linked_list import LinkedList, Node


def get_linked_list(list_of_numbers):
    linked_list = LinkedList()

    for node in [Node(number) for number in list_of_numbers]:
        linked_list.add_in_tail(node)

    return linked_list


@step('У нас есть лист (.*)')
def have_the_linked_list(step, list_of_numbers):  # noqa
    world.linked_list = get_linked_list(
        list_of_numbers.split(' ') if list_of_numbers else list()
    )


@step('мы вызываем метод .len')
def call_th_length_method(step):  # noqa
    world.length = world.linked_list.len()


@step('получаем количество элементов как переменную (\d+)')
def check_number(step, length):  # noqa
    assert world.length == int(length), "Получили %d" % world.length
