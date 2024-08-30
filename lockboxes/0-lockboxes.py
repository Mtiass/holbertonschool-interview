#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked given the initial unlocked state of the first box.

    Args:
        boxes (list of lists): A list where each element is a list containing keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    opened = set()
    blist = [0]  # Start with the first box

    while blist:
        box = blist.pop()  # Get the last element added to the blist
        if box in opened:
            continue
        opened.add(box)

        for key in boxes[box]:
            if key < n and key not in opened:
                blist.append(key)  # Add the box index to the blist

    return len(opened) == n
