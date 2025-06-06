class DatabaseError(Exception):
    """Base class for all custom database-related exceptions."""
    pass

class ConnectionError(DatabaseError):
    """Raised when a connection to the database cannot be established."""
    pass

class SaveError(DatabaseError):
    """Raised when saving to the database fails."""
    pass

class NotFoundError(DatabaseError):
    """Raised when a requested item is not found in the database."""
    pass