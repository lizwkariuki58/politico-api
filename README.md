# politico-api
API for the Politico application.

Hosted on [Heroku](https://my-politico-api.herokuapp.com/).

**API ENDPOINTS**

| Method   | Endpoint                       | Description                           |
| -------- | -------------------------------| ------------------------------------- |
| `POST`   | `/parties/`                    | Create a new party                    |
| `GET`    | `/parties/`                    | View all parties                      |
| `GET`    | `/parties/<int:party_id>`      | Get a specific party                  |
| `UPDATE` | `/parties/<int:party_id>`      | Update party details                  |
| `DELETE` | `/parties/<int:party_id>`      | Delete a political party              |
| `POST`   | `/offices/`                    | Create a new office                   |
| `GET`    | `/offices/`                    | View all offices                      |
| `GET`    | `/offices/<int:office_id>`     | Get a specific office                 |



**Payloads**

*Create a Party*

The request to create a party:

```/parties/```

Payload
```
{
    'id':1,
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
