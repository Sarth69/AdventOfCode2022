import re

class Noeud:
    def __init__(self, valeur):
        self.name = valeur
        self.children = []
        self.size = 0

    def get_child(self, childName):
        for child in self.children:
            if child.name == childName:
                return child
        node = Noeud(childName)
        self.children.append(node)
        return node
    
    def create_child_if_not_exist(self, currentPath):
        if len(currentPath)>1:
            for child in self.children:
                if child.name == currentPath[0]:
                    child.create_child_if_not_exist(currentPath[1:])
        else:
            exists = False
            for child in self.children:
                if child.name == currentPath[0]:
                    exists = True
                    break
            if not exists:
                self.children.append(Noeud(currentPath[0]))

    def add_size_to_current_path(self, size, currentPath):
        if len(currentPath)>0:
            self.size += size
            for child in self.children:
                if child.name == currentPath[0]:
                    child.add_size_to_current_path(size, currentPath[1:])
        else:
            self.size += size

    def total_sum(self, currentTot):
        if self.size <= 100000:
            currentTot+=self.size
        for child in self.children:
            currentTot = child.total_sum(currentTot)
        return currentTot

    def print(self, depth):
        print("-"*depth, self.name, self.size)
        for child in self.children:
            child.print(depth+1)

    def getMinSizeToDelete(self, minSizeToDelete, minSizeDeleted):
        #Soi même
        if self.size >= minSizeToDelete and self.size < minSizeDeleted:
            minSizeDeleted = self.size
        #Ses enfants
        for child in self.children:
            minSizeDeleted = child.getMinSizeToDelete(minSizeToDelete, minSizeDeleted)
        return minSizeDeleted

root = Noeud("/")
currentPath = []

with open("jour7Input.txt") as lines:
    for line in lines:
        line = line.strip()
        if line[0] == "$":
            if line[2] == "c":
                #CD
                dest = line[5:]
                match dest:
                    case "/":
                        currentPath = []
                    case "..":
                        currentPath.pop()
                    case _:
                        currentPath.append(dest)
                        root.create_child_if_not_exist(currentPath)
        else:
            #LS
            if line[0:3] == "dir":
                child = line[4:]
                root.create_child_if_not_exist(currentPath+[child])
            else:
                match = re.match("([0-9]*) ([a-zA-Z]*)", line)
                root.add_size_to_current_path(int(match[1]), currentPath)

root.print(0)
print(root.total_sum(0))

minSizeToDelete = 30000000-(70000000-root.size)
minSizeDeleted = root.size
print(root.size)
print(root.getMinSizeToDelete(minSizeToDelete, minSizeDeleted))