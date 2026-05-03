from app.utils.logger import logger

REQUIRED_FIELDS = [
    "country",
    "product_type",
    "price",
    "currency",
    "reporting_date"
]


def validate_record(record):

    errors = []

    for field in REQUIRED_FIELDS:
        if field not in record or record[field] is None:
            errors.append(f"Missing field: {field}")

    if "price" in record:
        try:
            price = float(record["price"])
            if price < 0:
                errors.append("Negative price value")
        except Exception:
            errors.append("Invalid price type")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }


def validate_dataset(records):

    logger.info("Starting validation process")

    valid_records = []
    invalid_records = []

    for record in records:
        result = validate_record(record)

        if result["valid"]:
            valid_records.append(record)
        else:
            invalid_records.append({
                "record": record,
                "errors": result["errors"]
            })

    return {
        "total_records": len(records),
        "valid_records": len(valid_records),
        "invalid_records": len(invalid_records),
        "valid_data": valid_records,
        "invalid_data": invalid_records
    }