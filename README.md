
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
  ```
  {
    "msg": "success",
    "info": "Districs list is sent..",
    "data": [
        "Taplejung",
        "Sankhuwasabha",
        .....]
  }
  ```  
- To get all provinces of Nepal
  ```
    {
    "data":"Provinces"
    }
  ```
  ```
  {
    "msg": "success",
    "info": "Districs list is sent..",
    "data": [
        "Province 1",
        "Madesh Pradesh",
        "Bagmati Pradesh",
        "Gandaki Pradesh",
        "Lumbini Pradesh",
        "Karnali Pradesh",
        "Sudurpaschim Pradesh"
    ]
  }
  ```
- To get all local bodies of Nepal
  ```
    {
    "data":"Local_bodies"
    }
  ```
  ```
  {
    "msg": "success",
    "info": "Local Bodies list is sent..",
    "data": [
        "Sidingba Rural Municipality",
        "Meringden Rural Municipality",
        "Maiwakhola Rural Municipality"
        ......]
  }
  ```
- To get list of local bodies in a specific district.
  ```
    {
    "data":{"District":"Name of district"(eg:Kaski)}
    }
  ```
  ```
  {
    "msg": "success",
    "info": "Local_bodies in Kaski district is sent.",
    "data": [
        "Rupa Rural Municipality",
        "Madi Rural Municipality",
        "Annapurna Rural Municipality",
        "Machhapuchchhre Rural Municipality",
        "Pokhara Metropolitian City"
    ]
  }
  ```
- To get list of district in a specific province.
  ```
    {
    "data":{"Province":"Name of province"(eg:Gandaki Pradesh, you can look into the all provinces response for correct name to avoid error),
    "alldata":"True/False"(True to get local bodies in each districts as well, False to get only list of district inside that pradesh)}
    }
  ```
  ```
  {
    "msg": "success",
    "info": "Districts in Gandaki Pradesh is sent.",
    "data": [
        "Gorkha",
        "Manang",
        "Mustang",
        "Myagdi",
        "Kaski",
        "Lamjung",
        "Tanahu",
        "Nawalparasi east",
        "Syangja",
        "Parbat",
        "Baglung"
    ]
  }
  ```
  ```
  {
    "msg": "success",
    "info": "Disricts with local_bodies in Gandaki Pradesh is sent.",
    "data": [
        {
            "Gorkha": [
                "Gandaki Rural Municipality",
                "Dharche Rural Municipality",
                "Aarughat Rural Municipality",
                "Ajirkot Rural Municipality",
                ....]
        ......
        }        
    ]
  ```

