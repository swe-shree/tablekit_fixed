def apply_filter(data, search: str = None):
    if not search:
        return data

    search = search.lower()

    return [
        item for item in data
        if any(search in str(value).lower() for value in item.values())
    ]