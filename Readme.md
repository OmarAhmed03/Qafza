# Diamond Price Prediction API

This repository contains a FastAPI-based web application for predicting diamond prices using machine learning.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Model](#model)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```
2. Build the Docker image:
    ```sh
    docker build -t diamond-price-predictor .
    ```
3. Run the Docker container:
    ```sh
    docker run -p 8000:8000 diamond-price-predictor
    ```
4. Alternatively, you can pull the pre-built Docker image:
    ```sh
    docker pull omarahmed03/diamond-predictor:tagname
    docker run -p 8000:8000 omarahmed03/diamond-predictor:tagname
    ```

## Usage

Once the Docker container is running, you can access the API documentation at `http://localhost:8000/docs`.

## API Endpoints

### `GET /`

Returns a welcome message.

### `POST /predict/`

Predicts the price of a diamond based on its features.

**Request Body:**
```json
{
  "carat": 0.3,
  "cut": "Ideal",
  "color": "D",
  "clarity": "VS1",
  "depth": 61.9,
  "table": 57,
  "x": 4.34,
  "y": 4.35,
  "z": 2.68
}
```

**Response:**
```json
{
  "price": 807.141357421875
}
```

## Model

The model used for prediction is an XGBoost regressor trained on a dataset of diamond prices. The model is loaded from a `model.pkl` file.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.