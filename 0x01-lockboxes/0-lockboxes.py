#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    num_boxes = len(boxes)
    visited = [False] * num_boxes   # Track visited boxes
    visited[0] = True   # Mark first box as visited
    stack = [0]   # Use a stack to perform depth-first search

    while stack:
        current_box = stack.pop()

        # Iterate throgh the keys in current box
        for key in boxes[current_box]:
            if key < num_boxes and not visited[key]:
                visited[key] = True
                stack.append(key)

    # Check if all boxes have been visited
    return all(visited)
