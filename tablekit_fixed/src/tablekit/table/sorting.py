def apply_sort(data, sort_by: str = None, sort_order: str = "asc"):
    if not sort_by:
        return data

    reverse = sort_order == "desc"

    return sorted(
        data,
        key=lambda x: x.get(sort_by, None),
        reverse=reverse
    )