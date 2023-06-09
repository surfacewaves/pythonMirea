class SVG:
    def __init__(self):
        self.lines = []
        self.circles = []

    def line(self, x1, y1, x2, y2, color='black'):
        self.lines.append((x1, y1, x2, y2, color))

    def circle(self, cx, cy, r, color='black'):
        self.circles.append((cx, cy, r, color))

    def save(self, filename, width, height):
        with open(filename, 'w') as f:
            f.write('<svg version="1.1" width="{}" height="{}" xmlns="http://www.w3.org/2000/svg">\n'.format(width, height))
            for line in self.lines:
                f.write('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="{}" />\n'.format(line[0], line[1], line[2], line[3], line[4]))
            for circle in self.circles:
                f.write('<circle cx="{}" cy="{}" r="{}" fill="{}" />\n'.format(circle[0], circle[1], circle[2], circle[3]))
            f.write('</svg>')


scale_x = 25 #10
scale_y = 50 #100
width = 1000


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.x = 0
        self.y = 0

    def get_width(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.get_width() + 1
        elif self.right is None:
            return self.left.get_width() + 1
        else:
            return self.left.get_width() + self.right.get_width() + 1

    def layout(self, x, y):
        if self.left is None and self.right is None:
            self.x = x
            self.y = y
        elif self.left is None:
            self.x = x
            self.y = y
            self.right.layout(x + 1, y + 1)
        elif self.right is None:
            self.x = x
            self.y = y
            self.left.layout(x - 1, y + 1)
        else:
            self.x = int((self.left.get_width() - self.right.get_width()) / 2) + x
            self.y = y
            self.left.layout(x - self.right.get_width() - 1, y + 1)
            self.right.layout(x + self.left.get_width() + 1, y + 1)

    def to_svg(self, svg):
        if self.left is not None:
            svg.line(width/2 + (self.x * scale_x), self.y * scale_y, width/2 + (self.left.x * scale_x), self.left.y * scale_y)
            self.left.to_svg(svg)
        if self.right is not None:
            svg.line(width/2 + (self.x * scale_x), self.y * scale_y, width/2 + (self.right.x * scale_x), self.right.y * scale_y)
            self.right.to_svg(svg)
        svg.circle(width/2 + (self.x * scale_x), self.y * scale_y, 10, color='black')


tree_2 = Tree(2, Tree(3, Tree(4), Tree(5)), Tree(6, Tree(7)))
tree_8 = Tree(8, Tree(9, Tree(10), Tree(11, Tree(12), Tree(13))), Tree(14))
tree = Tree(1, tree_2, tree_8)

svg = SVG()
tree.layout(tree.x, tree.y + 1)
tree.to_svg(svg)
svg.save('tree.svg', width, width/2)
