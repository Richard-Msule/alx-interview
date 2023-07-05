#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Function that determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing locked boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    # Check if input is a list
    if type(boxes) is not list:
        return False

    # Check if the list is empty
    elif len(boxes) == 0:
        return False

    # Iterate through indices from 1 to len(boxes) - 1
    for k in range(1, len(boxes) - 1):
        # Flag to track if key is found for current index (k)
        boxes_checked = False

        # Iterate through all boxes
        for idx in range(len(boxes)):
            # Check if current index (k) is a key in any other box and not the same box
            boxes_checked = k in boxes[idx] and k != idx

            # If key is found, break the loop
            if boxes_checked:
                break

        # If no key is found for the current index (k), return False
        if not boxes_checked:
            return boxes_checked

    # If all keys are found for all indices, return True
    return True


# Sample test cases
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False

