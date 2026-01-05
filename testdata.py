from main import Cousin, Parents, UserPrefs

def create_test_data() -> tuple[dict[str, Cousin], dict[str, Parents]]:
    """
    Creates a complete set of test data for development/testing.
    
    Returns:
        tuple: (cousins_dict, families_dict)
    """
    # Create families
    families = {
        "Charlie Baker": Parents("Charlie Baker", "chuck@email.com"),
        "Angela Johnson": Parents("Angela Johnson", "ajohnsons@email.com"),
        "Frankie Baker": Parents("Frankie Baker", "frankb@email.com")
    }
    
    # Create cousins
    cousins = {
        "Alice": Cousin("Alice", "Charlie Baker", "alice@email.com", 8),
        "Bob": Cousin("Bob", "Angela Johnson", "bob@email.com", 12),
        "Charlie": Cousin("Charlie", "Angela Johnson", "charlie@email.com", 10),
        "Diana": Cousin("Diana", "Frankie Baker", None, 6),
        "Eve": Cousin("Eve", "Frankie Baker", "eve@email.com", 14)
    }
    
    # Link children to parents
    families["Charlie Baker"].add_child("Alice")
    families["Angela Johnson"].add_child("Bob")
    families["Angela Johnson"].add_child("Charlie")
    families["Frankie Baker"].add_child("Diana")
    families["Frankie Baker"].add_child("Eve")
    
    return cousins, families