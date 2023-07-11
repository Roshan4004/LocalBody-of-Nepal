
# LocalBody of Nepal

This is an api for list of all local bodies of Nepal, aligned with their respective districts and province.

The data I got in this api is by web scraping so the data mayn't be 100% correct.
Basically, you can send a POST request of your preferred type of data(You'll understand more in documentation later.) and then get the required data.


## API Reference

#### Get all items

```
You don't have access to get all items at once since it's a large data and server might have issues. 
```

#### Get item

```https
  https://roshan4004.pythonanywhere.com/localbody/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `data`      | `string` | **Required**. type and which specific data you want to get |

  Examples of payload and response for each type of data is shown below:
- To get all districts of Nepal  
  ```
    {
    "data":"Districts"
    }
  ```
- To get all provinces of Nepal
  ```
    {
    "data":"Provinces"
    }
  ```
- To get all local bodies of Nepal
  ```
    {
    "data":"Local_bodies"
    }
  ```
- To get list of local bodies in a specific district.
  ```
    {
    "data":{"District":"Name of district"(eg:Kaski)}
    }
  ```
- To get list of district in a specific province.
  ```
    {
    "data":{"Province":"Name of province"(eg:Gandaki Pradesh, you can look into the all provinces response for correct name to avoid error),
    "alldata":"True/False"(True to get local bodies in each districts as well, False to get only list of district inside that pradesh)}
    }
  ```

