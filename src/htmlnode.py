class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        return (
            "".join([f' {key}="{self.props[key]}"' for key in self.props.keys()])
            if self.props is not None
            else ""
        )

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):

    def __init__(self, value, tag=None, props=None) -> None:
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        return (
            self.value
            if self.tag is None
            else f'<{self.tag}{self.props_to_html()}>{self.value}<\\{self.tag}>'
        )

    def __repr__(self) -> str:
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"


if __name__ == '__main__':
    node = HTMLNode("test", "test", "test", {"test": "test", "test2": "test2"})
    print(node)
    print(node.props_to_html())
    node2 = HTMLNode()
    print(node2.props_to_html())

    node = LeafNode("test text 123", "p", {"test": "test", "test2": "test2"})
    print(node)
    print(node.to_html())
    node2 = LeafNode("test text 123")
    print(node2.to_html())