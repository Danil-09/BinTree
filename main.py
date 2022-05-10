import random


class BinTree:
    class Node:
        def __init__(self, elem):
            self.elem = elem
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        self.root = None

    def _delete(self, elem, root):
        if self.root == None:
            return self.root
        if root.elem > elem:
            if root.left:
                root.left = self._delete(elem, root.left)
            return root
        if root.elem < elem:
            if root.right:
                root.right = self._delete(elem, root.right)
            return root
        if root.right == None:
            return root.left
        if root.left == None:
            return root.right
        min_larger_node = root.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        root.elem = min_larger_node.elem
        root.right = self._delete(min_larger_node.elem, root.right)
        return root

    def delete(self, elem):
        deli = self._delete(elem, self.root)

    def insert_iter(self, elem):
        y = self.root
        while y:
            if elem >= y.elem:
                if y.right:
                    y = y.right
                    continue
                else:
                    y.right = self.Node(elem)
                    return
            else:
                if y.left:
                    y = y.left
                    continue
                else:
                    y.left = self.Node(elem)
                    return

    def _insert(self, elem, root):
        if root.elem > elem:
            if root.left is None:
                root.left = self.Node(elem)
            else:
                self._insert(elem, root.left)
        else:
            if root.right is None:
                root.right = self.Node(elem)
            else:
                self._insert(elem, root.right)

    def insert(self, elem):
        if self.root is None:
            self.root = self.Node(elem)
        else:
            self._insert(elem, self.root)

    def _height(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self._height(root.left), self._height(root.right))

    def height(self):
        return self._height(self.root)

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, root):
        if root is not None:
            self._printTree(root.left)
            print(str(root.elem) + ' ')
            self._printTree(root.right)

    def max(self):
        if self.root is None:
            self.root = self.Node(self.elem)
        else:
            maxi = self._max(self.root)

    def _max(self, root):
        if root.right != None:
            self._max(root.right)
        else:
            print(root.elem)

    def min(self):
        if self.root is None:
            self.root = self.Node(self.elem)
        else:
            mini = self._min(self.root)

    def _min(self, root):
        if root.left != None:
            self._min(root.left)
        else:
            print(root.elem)

    def _DFS(self, root):
        if root is None:
            return
        self._DFS(root.left)
        print(root.elem, end=' ')
        self._DFS(root.right)

    def DFS(self):
        self._DFS(self.root)

    def _current_level(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root.elem, end=' ')
        elif level > 1:
            self._current_level(root.left, level - 1)
            self._current_level(root.right, level - 1)

    def _level_order(self, root):
        h = self.height()
        for i in range(1, h + 1):
            self._current_level(root, i)
            print('\n')

    def print_level_order(self):
        self._level_order(self.root)
        # print('\n')

    def getWidth(self, root, level):
        if root == None:
            return 0
        if level == 1:
            return 1
        elif level > 1:
            return self.getWidth(root.left, level-1) + self.getWidth(root.right, level-1)
        self.getWidth(root.right, level-1)

    def getMaxWidth(self, root):
        maxWdth = 0
        i = 1
        width = 0
        h = self.height()
        while i < h:
            width = self.getWidth(root, i)
            if width > maxWdth:
                maxWdth = width
            i += 1
        return maxWdth

    def __str__(self):
        if self.root is None:
            return ''

        def recurse(root):
            if root is None:
                return [], 0, 0
            label = str(root.elem)
            left_lines, left_pos, left_width = recurse(root.left)
            right_lines, right_pos, right_width = recurse(root.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and root.right is not None and \
                    root is root.right.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.':
                label = ' ' + label[1:]
            if label[-1] == '.':
                label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle - 2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
                    [left_line + ' ' * (width - left_width - right_width) +
                     right_line
                     for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width

        return '\n'.join(recurse(self.root)[0])

if __name__ == '__main__':
    btr = BinTree()
    i = 0
    lst = []
    while i < 20:
        number = random.randint(0, 51)
        lst = lst + [number]
        i = i + 1
    print("lst = ", lst)

    f = open('file.txt', 'wt')
    for i in lst:
        s = str(i)
        f.write(s + ' ')
    f.close()
    f = open('file.txt', 'r')
    s = f.readline()
    f.close()
    for ll in lst:
        btr.insert(ll)

    print("Height", btr.height())
    print("Width:", btr.getMaxWidth(btr.root))
    print("DFS")
    btr.DFS()
    print('\n'+'BFS')
    btr.print_level_order()
    print("Max:")
    btr.max()
    print("Min:")
    btr.min()
    print('\n')
    print(btr)

    f = open('bst.txt', 'w')
    f.write(str(btr))
    f.close()
