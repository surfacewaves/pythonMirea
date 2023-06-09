class HTML:
    def __init__(self):
        self.code = ""

    def get_code(self):
        return self.code

    def p(self, text):
        self.code += f"<p>{text}</p>\n"

    class Tag:
        def __init__(self, tag_name, html):
            self.tag_name = tag_name
            self.attributes = {}
            self.children = []
            self.html = html

        def __enter__(self):
            self.html.code += f"<{self.tag_name}"
            if self.attributes:
                self.html.code += ' ' + ' '.join([f'{k}="{v}"' for k, v in self.attributes.items()])
            self.html.code += ">\n"
            return self

        def __exit__(self, type, value, traceback):
            for child in self.children:
                self.html.code += child
            self.html.code += f"</{self.tag_name}>\n"

        def __call__(self, *args, **kwargs):
            for arg in args:
                if isinstance(arg, str):
                    self.children.append(arg)
                elif isinstance(arg, HTML.P):
                    self.children.append(str(arg))
            if kwargs:
                self.attributes = kwargs
            return self

    def __getattr__(self, tag_name):
        return HTML.Tag(tag_name, self)


def main():
    html = HTML()
    with html.body():
        with html.div():
            with html.div():
                html.p('Первая строка.')
                html.p('Вторая строка.')
            with html.div():
                html.p('Третья строка.')
    print(html.get_code())


if __name__ == '__main__':
    main()
