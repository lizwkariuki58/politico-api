# politico-api
API for the Politico application

Hosted on [Heroku](https://git.heroku.com/my-politico-api.git).

**API ENDPOINTS**

| Method   | Endpoint                       | Description                           |
| -------- | -------------------------------| ------------------------------------- |
| `POST`   | `/parties/`                    | Create a new party                    |
| `GET`    | `/parties/`                    | View all parties                      |
| `GET`    | `/parties/<int:party_id>`      | Get a specific party                  |


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
    'slogan': 'Where dwell the      brave at heart'
}
```

This response shall be returned
```
'message': 'Party Created'
'party_id': 1
```
