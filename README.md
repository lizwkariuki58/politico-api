# politico-api
API for the Politico application.

Hosted on [Heroku](https://my-politico-api.herokuapp.com/).

[![Build Status](https://travis-ci.com/lizwkariuki58/politico-api.svg?branch=develop)](https://travis-ci.com/lizwkariuki58/politico-api)

[![Coverage Status](https://coveralls.io/repos/github/lizwkariuki58/politico-api/badge.svg?branch=develop)](https://coveralls.io/github/lizwkariuki58/politico-api?branch=develop)

[![Maintainability](https://api.codeclimate.com/v1/badges/12f0f1314a467dd219a1/maintainability)](https://codeclimate.com/github/lizwkariuki58/politico-api/maintainability)

**API ENDPOINTS**

| Method   | Endpoint                              | Description                           |
| -------- | --------------------------------------| ------------------------------------- |
| `POST`   | `/api/v1/parties/`                    | Create a new party                    |
| `GET`    | `/api/v1/parties/`                    | View all parties                      |
| `GET`    | `/api/v1/parties/<int:party_id>`      | Get a specific party                  |
| `UPDATE` | `/api/v1/parties/<int:party_id>`      | Update party details                  |
| `DELETE` | `/api/v1/parties/<int:party_id>`      | Delete a political party              |
| `POST`   | `/api/v1/offices/`                    | Create a new office                   |
| `GET`    | `/api/v1/offices/`                    | View all offices                      |
| `GET`    | `/api/v1/offices/<int:office_id>`     | Get a specific office                 |



**Payloads**

*Create a Party*

The request to create a party:

```api/v1/parties/```

Payload
```
{
    'name': 'Gryffindor'
    'hqAddress': '12 Grimmauld Place'
    'slogan': 'Where dwell the brave at heart'
}
```

This response shall be returned
```
'Party': Party
'status': '200 OK'
```

*Update a Party*

The request to update a party:

```/api/v1/parties/<int:party_id>```

Payload
```
{
    'name': 'Gryffindor'
    'hqAddress': '12 Grimmauld Place'
    'slogan': 'Where dwell the brave at heart'
}
```

This response shall be returned
```
'Party': Party Updated
'status': '200 OK'
```

*Create an Office*

The request to create an office:

```/api/v1/offices/```

Payload
```
{
    'office_type': 'Executive'
    'name': 'President'
}
```

This response shall be returned
```
'Office': Office
'status': '200 OK'
```
