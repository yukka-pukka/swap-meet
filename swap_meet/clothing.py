from .item import Item


class Clothing(Item):
    def __init__(self, category="", condition=0, condition_description=" "):
        super().__init__("Clothing", condition)

    def __str__(self):
        return "The finest clothing you could wear."
