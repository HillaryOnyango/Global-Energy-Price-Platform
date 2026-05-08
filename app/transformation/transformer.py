from datetime import datetime


def transform_record(record, batch_id):

    return {
        "country": record.get("country"),
        "product_type": record.get("product_type"),
        "price": float(record.get("price", 0)),
        "currency": record.get("currency"),
        "unit": record.get("unit", "unknown"),
        "source": "global_petrol_prices",
        "reporting_date": record.get("reporting_date"),
        "ingestion_timestamp": datetime.utcnow(),
        "batch_id": batch_id
    }


def transform_dataset(records, batch_id):

    return [
        transform_record(record, batch_id)
        for record in records
    ]