import logging
from priority_queue import PrimaryQueue

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def test_insert():
    """
    Tests the insert function of the PrimaryQueue class.
    """
    queue = PrimaryQueue()
    node = {'command': 'command1', 'priority': 5}
    queue.insert(node)
    assert queue.peek() == node

def test_insert_error():
    """
    Attempts to insert a node with no command or priority specified.
    """
    queue = PrimaryQueue()
    node = {'priority': 5}
    try:
        queue.insert(node)
    except ValueError as e:
        assert str(e) == 'Command and priority must be specified'

def test_missing_priority():
    """
    Tests if the insert function raises a ValueError when the priority is not specified.
    """
    queue = PrimaryQueue()
    node = {'command': 'command1'}
    try:
        queue.insert(node)
    except ValueError as e:
        assert str(e) == 'Command and priority must be specified'

def test_invalid_priority_1():
    """
    Tests that an error is raised when an invalid priority is passed to the insert method when greater than the max.
    """
    queue = PrimaryQueue()
    node = {'command': 'command1', 'priority': 11}
    try:
        queue.insert(node)
    except ValueError as e:
        assert str(e) == 'Priority must be between 0 and 10'

def test_invalid_priority_2():
    """
    Tests that an error is raised when an invalid priority is passed to the insert method when less than the min.
    """
    queue = PrimaryQueue()
    node = {'command': 'command1', 'priority': -1}
    try:
        queue.insert(node)
    except ValueError as e:
        assert str(e) == 'Priority must be between 0 and 10'

def test_remove_empty():
    """
    Tests that the remove method will return nothing when given an empty queue.
    """
    queue = PrimaryQueue()
    assert queue.remove() == None

def test_remove():
    """
    Tests that commans added to the queue are removed from the queue in the correct order.
    """
    queue = PrimaryQueue()
    node1 = {'command': 'command1', 'priority': 5}
    node2 = {'command': 'command2', 'priority': 8}
    queue.insert(node1)
    queue.insert(node2)
    print(queue.heap)
    print(queue.peek())
    assert queue.remove() == node2
    assert queue.peek() == node1

def test_peek_empty():
    """
    Tests that the peek method will return nothing when given an empty queue.
    """
    queue = PrimaryQueue()
    assert queue.peek() == None

def test_peek():
    """
    Tests that the peek method will return the head of the priority queue.
    """
    queue = PrimaryQueue()
    node1 = {'command': 'command1', 'priority': 5}
    node2 = {'command': 'command1', 'priority': 3}
    node3 = {'command': 'command2', 'priority': 2}
    queue.insert(node1)
    assert queue.peek() == node1

def main():
    test_insert()
    test_insert_error()
    test_missing_priority()
    test_invalid_priority_1()
    test_invalid_priority_2()
    test_remove_empty()
    test_remove()
    test_peek_empty()
    test_peek()

if __name__ == '__main__':
    main()
    