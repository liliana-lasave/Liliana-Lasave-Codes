class DatabaseError(Exception):
    """Base class for all custom data-related exceptions."""
    pass

class ConnectionError(DatabaseError):
    """Raised when a connection to the data cannot be established."""
    pass

class SaveError(DatabaseError):
    """Raised when saving to the data fails."""
    pass

class NotFoundError(DatabaseError):
    """Raised when a requested item is not found in the data."""
    pass