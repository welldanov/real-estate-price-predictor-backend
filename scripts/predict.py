from real_estate_price_predictor.ml.predictor import (
    RealEstatePredictor,
)


def main() -> None:
    predictor = RealEstatePredictor()

    price = predictor.predict_apartment(
        city_name="Альметьевск",
        lat=54.890438,
        lon=52.268565,
        distance_to_center_km=2.3,
        area_m2=42,
        rooms=1,
        is_studio=0,
        floor=8,
        floors_total=18,
    )

    print()
    print("=" * 50)
    print("APARTMENT PRICE PREDICTION")
    print("=" * 50)
    print(f"Predicted price: {price:,.0f} RUB")
    print("=" * 50)


if __name__ == "__main__":
    main()
