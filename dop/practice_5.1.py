class SVG:
    def __init__(self):
        self.lines = []
        self.circles = []

    def line(self, x1, y1, x2, y2, color):
        self.lines.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" />')

    def circle(self, cx, cy, r, color):
        self.circles.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" />')

    def save(self, filename, height, width):
        with open(filename, 'w') as f:
            f.write(f'<svg version="1.1" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n')
            f.write('\n'.join(self.lines))
            f.write('\n')
            f.write('\n'.join(self.circles))
            f.write('\n</svg>\n')


svg = SVG()

svg.line(10, 10, 60, 10, color='black')
svg.line(60, 10, 60, 60, color='black')
svg.line(60, 60, 10, 60, color='black')
svg.line(10, 60, 10, 10, color='black')

svg.circle(10, 10, r=5, color='red')
svg.circle(60, 10, r=5, color='red')
svg.circle(60, 60, r=5, color='red')
svg.circle(10, 60, r=5, color='red')

svg.save('test.svg', 100, 100)
