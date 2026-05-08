from app.ingestion.api_client import (
    fetch_petroleum_prices,
    fetch_natural_gas_prices
)

from app.loaders.mongodb_loader import (
    load_raw_data
)


def run_ingestion():

    petroleum_data = fetch_petroleum_prices()

    natural_gas_data = fetch_natural_gas_prices()

    load_raw_data(petroleum_data)

    load_raw_data(natural_gas_data)