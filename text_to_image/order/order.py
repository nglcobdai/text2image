class Order:
    def __init__(self, **kwargs):
        """Prompt class

        Args:
            category (str): Category name
            tags (List[str]): Tags
            title (str): Title
        """
        self.category = kwargs.get("category", "general")
        self.tags = kwargs.get("tags", [])
        self.title = kwargs.get("title", "A beautiful landscape painting")

    def prompt(self):
        return self.title
