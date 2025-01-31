class Node:

    #Инициализируем вершины
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

#В нотации Голова-хвост
head = Node(1, Node(2, Node(3, Node(4))))

# выводим от головы к хвосту в цикле, пока не упремся в нон
def print_list(head, end='\n'):
    while head:
        print(head.data, end=' -> ' if head.next else '')
        head = head.next
    print(end=end)

print_list(head)

# по-сути, просто обмен значений следующий за головой, хвост, голова
def reverse_list(head, tail=None):
    while head:
        head.next, tail, head = tail, head, head.next
    return tail


print_list(reverse_list(head))
