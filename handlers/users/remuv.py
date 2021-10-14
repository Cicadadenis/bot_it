import os

rrt = open('name.txt', 'r')
cicada = rrt.read()
rrt.close()

def dellite():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), f"Dowload/{cicada}")
    os.remove(path)