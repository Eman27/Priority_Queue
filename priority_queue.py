# -*- coding: utf-8 -*-
import argparse
import json
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def heapify(heap, i):
    """
    Takes an node and creates/updates a binary heap 
    
    Args:
        heap(list): Store the heap
        i(int): Specify the index of the node to be heapified 
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    #checks if the left/right heapNode is larger than the current largest, updates the largest
    if left < len(heap) and heap[left]['priority'] > heap[largest]['priority']:
        largest = left
    if right < len(heap) and heap[right]['priority'] > heap[largest]['priority']:
        largest = right

    #checks if largest node has changed, swaps the current and largest nodes and reheapifies
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        heapify(heap, largest)
 
class PrimaryQueue(object):

    def __init__(self):
        self.heap = []

    def insert(self, d):
        """
        Takes creates a new node, adds it to the heap and reheapifies it.
        
        Args:
            d(dict): Pass in a dictionary containing the command and priority
        """
        #check for missing dictionary keys
        if 'command' not in d.keys() or 'priority' not in d.keys():
            raise ValueError('Command and priority must be specified')
        
        #check for a valid priority value
        if d['priority'] > 10 or d['priority'] < 0:
            raise ValueError('Priority must be between 0 and 10')
        
        #creates a new heapNode that is added to the heap
        self.heap.append(d)
        for i in range((len(self.heap)//2) - 1, -1, -1):
            heapify(self.heap, i)
 
    def peek(self):
        """
        Returns the value of the first element in the heap.
        
        Returns:
            head(dict): Returns the dictionary with the highest priority
        """

        #checks if heap is not empty and returns the heap's head if true
        if len(self.heap) <= 0:
            log.info('Heap is empty, nothing to peek')
            return None
        else:
            return self.heap[0]

    def remove(self):
        """
        Removes the root node from the heap then calls heapify to re-establish the max-heap property.

        
        Returns:
            head(dict): Returns the dictionary with the highest priority
        """

        size = len(self.heap)
        if size <= 0:
            log.info('Heap is empty, nothing to extract')
            return None
        else:
            #Swaps root node with the last element in the heap, removes it and reheapifies
            self.heap[0],self.heap[size - 1] = self.heap[size - 1],self.heap[0]
            head = self.heap.pop(size - 1)
            for i in range((len(self.heap)//2) - 1, -1, -1):
                heapify(self.heap, i)
            # heapify(self.heap, 0)
            return head

def launch_priority_queue(command_list):
    """
    Takes a list of dictionaries containing command and priority, and executes them in order of priority.
    
    Args:
        data([dict]): Pass in the list of commands to be executed
    """

    if len(command_list) <= 0:
        log.info('No commands to execute')
        return
    
    log.info('Creating priority queue.')
    pq = PrimaryQueue()
    
    log.info('Reading commands into priority queue.')
    for command in command_list:
        pq.insert(command)

    log.info('Heapifying commands.{}'.format(pq.heap))
    log.info('Begin executing commands in order of priority.')
    while len(pq.heap) > 0:
        commandNode = pq.remove()
        log.info('Executing command {} priority {} '.format(commandNode['command'], commandNode['priority']))
    log.info('Finished executing commands in order of priority.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-j', '--json',
        type=str,
        required=True,
        help='json file containing list of dictionaries containing command and priority',
    )
    args = parser.parse_args()

    with open(args.json,'r') as j:
        try:
            data = json.load(j)
            launch_priority_queue(data)
        except json.decoder.JSONDecodeError:
            log.error('Unable to parse json file')
        