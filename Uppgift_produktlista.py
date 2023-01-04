class Node:
    def __init__(self, x):
        self.value = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, n):
        if self.first == None:
            self.first = n
            self.last = n
        else:
            self.last.next = n
            self.last = n

    def printList(self):
        currentNode = self.first
        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next

    def sortList(self):
        current = self.first
        index = None

        if self.first == None:
            return
        else:
            while current != None:
                index = current.next

                while index != None:
                    if current.value > index.value:
                        temp = current.value
                        current.value = index.value
                        index.value = temp
                    index = index.next
                current = current.next


class Menu:

    def MenuProducts1(self):
        print("Skriv in produkter i form av av bokstäver - bindestreck - siffror, exemeplvis CE-400. Avsluta med att skriva 'exit'.")
        while True:
            product = input("Ange produkt: \n")
            x = product.split("-")
            if product.strip().lower() == "exit":
                print("Du angav följade produkter i sorterad ordning:")
                linkedList.sortList()
                linkedList.printList()
                break
            elif "-" not in product:
                print("Felaktig input\nSkriv in produkter i form av av bokstäver - bindestreck - siffror, exemeplvis CE-400. Avsluta med att skriva 'exit'")
            elif x[0].isalpha() == False and x[1].isdigit() == False:
                print("Felaktigt format på båda sidorna av produktnamnet")
            elif x[0].isalpha() == False:
                print("Felaktigt format på vänstra sidan av produktnamnet")
            elif x[1].isdigit() == False:
                print("Felaktigt format på högra sidan av produktnamnet")
            elif int(x[1]) < 200 or int(x[1]) > 500:
                print("Den numeriska delen måste vara mellan 200 och 500")
            else:
                node1 = Node(product)
                linkedList.add(node1)


linkedList = LinkedList()
menu1 = Menu()
menu1.MenuProducts1()
