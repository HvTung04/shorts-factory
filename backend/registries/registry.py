class Registry[Key, Value]:
    """Generic implementation of the Registry pattern using a hash map.
    """

    def __init__(self):
        """Initialize the registry with an empty internal store."""
        self._store: dict[Key, Value] = {}

    def register(self, key: Key, value: Value) -> None:
        """Register a key-value pair to the registry.

        This method checks for key collisions to ensure uniqueness.

        Args:
            key (Key): The unique identifier for the stored value.
            value (Value): The item (object, class, or callable) to store.

        Raises:
            ValueError: If the key is already registered.
        """
        if key in self._store:
            raise ValueError(f"Key '{key}' is already registered.")
        self._store[key] = value

    def get(self, key: Key) -> Value:
        """Retrieve a value by its key.

        Args:
            key (Key): The unique identifier to look up.

        Returns:
            Value: The stored value associated with the key.

        Raises: 
            KeyError: If the key is not found in the registry.
        """
        if value := self._store.get(key):
            return value
        else:
            raise KeyError(f"Key '{key}' not found in registry.")

    def unregister(self, key: Key) -> None:
        """Remove a key-value pair from the registry.

        Args:
            key (Key): The unique identifier of the item to remove.

        Raises:
            KeyError: If the key is not found in the registry.
        """
        if key not in self._store:
            raise KeyError(f"Key '{key}' not found in registry.")
        del self._store[key]

    def __contains__(self, key: Key) -> bool:
        """Checks if a key exists in the registry.

        This method enables the use of the 'in' operator (e.g., `if key in registry:`).

        Args:
            key (Key): The unique identifier to check.

        Returns:
            bool: True if the key is registered, False otherwise.
        """
        return key in self._store

    def list_keys(self) -> list[Key]:
        """Return a list of all keys currently registered.

        Returns:
            list[Key]: A list containing all registered keys.
        """
        return list(self._store.keys())