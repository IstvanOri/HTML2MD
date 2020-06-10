class Transformation:
    """
    Abstract Transformation class which is a marker class for Transformations used for string manipulations on a
    given text.

    Available implementations:
        LinkFixer
        LinkRelativizer
        RemoveWhiteSpace
        Replace
        Slugify
        ToLowerCase
    """

    def execute(self, content: str) -> str:
        pass