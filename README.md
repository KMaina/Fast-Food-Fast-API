[![Build Status](https://travis-ci.org/KMaina/Fast-Food-Fast-API.svg?branch=develop)](https://travis-ci.org/KMaina/Fast-Food-Fast-API) 
[![Test Coverage](https://api.codeclimate.com/v1/badges/9d8493d316483f7c9d58/test_coverage)](https://codeclimate.com/github/KMaina/Fast-Food-Fast-API/test_coverage) <a href="https://codeclimate.com/github/KMaina/Fast-Food-Fast-API/maintainability"><img src="https://api.codeclimate.com/v1/badges/9d8493d316483f7c9d58/maintainability" /></a> 
[![Coverage Status](https://coveralls.io/repos/github/KMaina/Fast-Food-Fast-API/badge.svg?branch=develop)](https://coveralls.io/github/KMaina/Fast-Food-Fast-API?branch=develop)
# Fast-Food-Fast-API

This contains all work undertaken for challenge 2

## Getting Started

Clone the repo locally using the command `git clone https://github.com/KMaina/Fast-Food-Fast-API.git`

### Prerequisites

```
Software to test out the api functionality eg Postman or Curl
Python version 3.6.x
```

### Installing

Once cloned locally, cd into the `Fast-Food-Fast-API` folder

Run the command `pip install -r requirements.txt` to install all dependencies and packages

Create a new file called `.env` that will house all your environment variables

Inside it add the following configurations

```
export FLASK_APP = run.py
export FLASK_ENV = development
```

Create a virtual environmnent by running the command `virtualenv <virtualenvironnment-name>` then activate it

To run the app type the command `flask run`

### Testing

With the virtual environment active, run the command `pytest`

# API Functionality

## Add Order

Adds a new order to the list of orders

  * URL
  /api/v1/orders
  * Method
  `POST`
  * Success Response
    * Code: 201
    * Content: `{'name': Pizza, 'quantity' : 2,'description' : 'Perfect as a snack.','id' : 1,'status' : 1}`
  * Sample Call:
      ```
      {
        'name': "Pizza",
        'quantity' : 2,
        'description' : "Perfect as a snack",
        'id' : len(orders) + 1,
        'status' : 1
      }
      ```
 
 ## Get All Orders

Returns all orders placed

  * URL
  /api/v1/orders
  * Method
    `GET`
  * Success Response
    * Code: 200
    * Content: 
    ```
    [
      {
        'name': 'Pizza',
        'quantity' : 2,
        'description' : 'Perfect as a snack.',
        'id' : 1,
        'status' : 1
        }
    ]
    ```
  * Error Response
    * Code: 404
    * Content : `{'messsage': 'Nothing found'}`
  * Sample Call:
      ```
      url: "api/v1/users",
      dataType: "json",
      type:"GET"
      ```
 ## Get A Specific Order

Returns one order placed

  * URL
  /api/v1/order/:id
  * URL Params
    ##### Required:
    `id=[Integer]`
    
  * Method
    `GET`
  * Success Response
    * Code: 200
    * Content: 
    ```
    [
      {
        'name': 'Pizza',
        'quantity' : 2,
        'description' : 'Perfect as a snack.',
        'id' : 1,
        'status' : 1
        }
    ]
    ```
  * Error Response
    * Code: 404
    * Content : `{'messsage': 'Error, order not found'}`
  * Sample Call:
      ```
      url: "api/v1/user/1",
      dataType: "json",
      type:"GET"
      ```
## Change the Status of A Particular Order

Returns one order with a different status code

  * URL
  /api/v1/order/:id
  * URL Params
    ##### Required:
    `id=[Integer]`
    
  * Method
    `PUT`
  * Success Response
    * Code: 200
    * Content: 
    ```
    [
      {
        'name': 'Pizza',
        'quantity' : 2,
        'description' : 'Perfect as a snack.',
        'id' : 1,
        'status' : 2
        }
    ]
    ```
  * Error Response
    * Code: 404
    * Content : `{'messsage': 'Error, order not found'}`
  * Sample Call:
      ```
      {'status' : 1}
      ```
      
## Deletes a Specific Order

Returns all orders less the one deleted

  * URL
  /api/v1/order/:id
  * URL Params
    ##### Required:
    `id=[Integer]`
    
  * Method
    `DELETE`
  * Success Response
    * Code: 204
    * Content: 
    ```
    [
      {
        'name': 'Pizza',
        'quantity' : 2,
        'description' : 'Perfect as a snack.',
        'id' : 1,
        'status' : 1
        }
    ]
    ```
  * Error Response
    * Code: 404
    * Content : `{'messsage': 'Error, order not found'}`
  * Sample Call:
      ```
      url: "api/v1/user/1",
      dataType: "json",
      type:"DELETE"
      ```