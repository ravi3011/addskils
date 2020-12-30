class GenericTree:

    class Node:
        def __init__(self,data):
            self.data = data
            self.children = list()

    size = -1
    root = None
    # def __init__(self):
    #     root = self.takeInput(None,0)

    def takeInput(self,parent,ithChild):
        if(not parent):
            print("Enter the data for the root")
        else:
            print("Enter the data "+str(ithChild)+ " th child of "+str(parent.data) )

        data = int(input())
        node = self.Node(data)
        self.size +=1
        print("Enter the children for "+str(node.data) )

        children = int(input())
        for i in range(children):
            child = self.takeInput(node,i)
            node.children.append(child)
        return node

    def display(self,node):
        st = str(node.data) + "=>"

        for i in range(len(node.children)):
            st += str(node.children[i].data)+" "
        st = st + "END"
        print(st)
        for i in range(len(node.children)):
            self.display(node.children[i])

temp = GenericTree()
node = temp.takeInput(None,0)
temp.display(node)                                        
