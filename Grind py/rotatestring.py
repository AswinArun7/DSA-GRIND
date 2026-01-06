def rotate_string(s, goal):
    if len(s) != len(goal):
        return False
    return goal in s + s


s=input("Enter the str:")
goal=input("Enter the goal str:")
print(rotate_string(s, goal))