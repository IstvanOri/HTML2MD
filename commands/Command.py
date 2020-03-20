class Command:
    """
    Abstract command class to hold the command logic, the tag properties and the children and parent commands

    Available implementations:
        Ignore
        Strip
        Wrap
        WrapIn
        WrapOut
        WrapWithAttribute
        Config
        Table
    """

    _bullet = " * "

    def __init__(self):
        self._children: [Command] = []
        self._ancestor: Command = None
        self._data: str = ""
        self._attrs = None
        self._tag: str = None
        self._pop_more: bool = False

    def __copy__(self):
        return None

    def execute(self) -> str:
        """
        Executes this command on the assigned tag
        :return: the result of the command
        """
        result = ""
        for child in self._children:
            result += child.execute()
        return result

    def pop_more(self):
        """
        Sets if this command is part of a composite rule so that the command stack needs another pop after this command
        was popped.
        """
        self._pop_more = True

    def needs_more_pop(self) -> bool:
        """
        Indicates if this command is part of a composite rule so that the command stack needs another pop after this one
        was popped.
        :return: True if another pop is required, False otherwise
        """
        return self._pop_more

    @property
    def data(self):
        """
        data property that holds basicall the content between the start and end tag
        """
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def ancestor(self):
        """
        The Command this Command is child of
        """
        return self._ancestor

    @ancestor.setter
    def ancestor(self, ancestor):
        self._ancestor = ancestor

    def add_child(self, command):
        """
        Adds a Command to this one as a child. Child commands are performed before ancestors.
        :param command: The child command
        """
        self._children.append(command)

    @property
    def tag(self):
        """
        The name of the tag this Command is assigned to
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        self._tag = tag

    @property
    def attrs(self):
        """
        The attributes of the tag this Command is assigned to
        """
        return self._attrs

    @attrs.setter
    def attrs(self, attrs):
        self._attrs = attrs
