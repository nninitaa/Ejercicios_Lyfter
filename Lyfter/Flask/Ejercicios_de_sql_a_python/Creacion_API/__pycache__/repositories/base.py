def build_where(filters, allowed_columns):
    conditions = []
    values = []

    for column, value in filters.items():
        if column in allowed_columns:
            conditions.append(f"{column} = %s")
            values.append(value)

    if not conditions:
        return "", []

    return " WHERE " + " AND ".join(conditions), values
