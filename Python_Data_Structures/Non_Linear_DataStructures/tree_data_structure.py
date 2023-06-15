class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def build_product_tree(self):
        root = Tree("Electronics")

        laptop = Tree("Laptop")
        laptop.add_child(Tree("Mac"))
        laptop.add_child(Tree("Surface"))
        laptop.add_child(Tree("Thinkpad"))

        cellphone = Tree("Cell Phone")
        cellphone.add_child(Tree("iPhone"))
        cellphone.add_child(Tree("Google Pixel"))
        cellphone.add_child(Tree("Vivo"))

        tv = Tree("TV")
        tv.add_child(Tree("Samsung"))
        tv.add_child(Tree("LG"))

        root.add_child(laptop)
        root.add_child(cellphone)
        root.add_child(tv)

        return root

    if __name__ == '__main__':
        root = build_product_tree()
        root.print_tree()

        # Electronics
        #    |__Laptop
        #       |__Mac
        #       |__Surface
        #       |__Thinkpad
        #    |__Cell Phone
        #       |__iPhone
        #       |__Google Pixel
        #       |__Vivo
        #    |__TV
        #       |__Samsung
        #       |__LG

