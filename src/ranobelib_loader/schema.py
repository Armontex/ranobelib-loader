from prosemirror.model import Schema
from prosemirror.model.schema import MarkSpec, NodeSpec

marks: dict[str, MarkSpec] = {
    "bold": {
        "parseDOM": [{
            "tag": "strong"
        }, {
            "tag": "bold"
        }, {
            "tag": "b"
        }],
        "toDOM": lambda node, _: ["strong", 0],
    },
    "italic": {
        "parseDOM": [{
            "tag": "i",
            "tag": "em"
        }],
        "toDOM": lambda node, _: ["em", 0],
    },
    "underline": {
        "parseDOM": [{
            "tag": "u"
        }],
        "toDOM": lambda node, _: ["u", 0],
    },
    "strike": {
        "parseDOM": [{
            "tag": "s",
            "tag": "strike",
            "tag": "del"
        }],
        "toDOM": lambda node, _: ["s", 0],
    }
}

nodes: dict[str, NodeSpec] = {
    "doc": {
        "content": "block+"
    },
    "paragraph": {
        "content": "text*",
        "group": "block",
        "parseDOM": [{
            "tag": "p"
        }],
        "toDOM": lambda _: ["p", 0]
    },
    "text": {
        "group": "inline"
    },
    "heading": {
        "attrs": {
            "level": {
                "default": 1
            }
        },  # TODO: Добавить textAlign
        "content":
        "text*",
        "group":
        "block",
        "parseDOM": [
            {
                "tag": "h1",
                "attrs": {
                    "level": 1
                }
            },
            {
                "tag": "h2",
                "attrs": {
                    "level": 2
                }
            },
            {
                "tag": "h3",
                "attrs": {
                    "level": 2
                }
            },
            {
                "tag": "h4",
                "attrs": {
                    "level": 2
                }
            },
            {
                "tag": "h5",
                "attrs": {
                    "level": 2
                }
            },
            {
                "tag": "h6",
                "attrs": {
                    "level": 2
                }
            },
        ],
        "toDOM":
        lambda node: [f"h{node.attrs['level']}", 0],
    },
    "orderedList": {
        "attrs": {
            "start": {
                "default": 1
            }
        },
        "content": "listItem+",
        "group": "block",
        "parseDOM": [{
            "tag": "ol"
        }],
        "toDOM": lambda _: ["ol", 0]
    },
    "bulletList": {
        "content": "listItem+",
        "group": "block",
        "parseDOM": [{
            "tag": "ul"
        }],
        "toDOM": lambda _: ["ul", 0]
    },
    "listItem": {
        "group": "block",
        "content": "paragraph",
        "parseDOM": [{
            "tag": "li"
        }],
        "toDOM": lambda _: ["li", 0]
    },
    "blockquote": {
        "group": "block",
        "content": "paragraph* orderedList* bulletList*",
        "parseDOM": [{
            "tag": "blockquote"
        }],
        "toDOM": lambda _: ["blockquote", 0]
    },
    "horizontalRule": {
        "group": "block",
        "parseDOM": [{
            "tag": "hr"
        }],
        "toDOM": lambda _: ["hr"]
    }
}

schema = Schema({"nodes": nodes, "marks": marks})


__all__ = ["schema"]