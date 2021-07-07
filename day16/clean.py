import os

def c():
    """Clean sundly the screnn """
    if os.name in ['nt', 'dos']:
        command = "cls"
    else:
        command = "clear"
    os.system(command)


def clear():
    """Give a pause before clean sundely the screen"""
    stay = input("Press enter to continue...")
    c()
