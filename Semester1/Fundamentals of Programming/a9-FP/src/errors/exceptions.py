class ValidationError(Exception):
    """
    Here we create our own Exception called ValidationError for errors that come from the validation layer
    """
    pass


class RepositoryError(Exception):
    """
    Here we create our own Exception called RepositoryError for errors that come from the Repo
    """
    pass


class UndoError(Exception):
    """
    Here we create our own Exception called RepositoryError for errors that come from the undo functionality
    """
    pass