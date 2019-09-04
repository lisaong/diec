# Designing Intelligent Edge Computing

## Eclipse Kapua Python Client

1. [editor.swagger.io](editor.swagger.io)
2. Drag and drop day1/swagger.json
3. Generate Client -> Python
4. Unzip the downloaded python-client-generated.zip
5. Rename the python-client folder to kapua-python-client and replace the day1/kapua-python-client
6. cd day1/kapua-python-client
7. Fix-ups

  * Update the root url in `swagger_client/configuration.py` to the host URL:
```
        # Default Base url
        self.host = "http://localhost:8081/v1"
```

  * Comment out this line near the top of `swagger_client/models/account.py`:
```
#from swagger_client.models.account import Account  # noqa: F401,E501
```

  * Comment out this line near the top of `swagger_client/models/domain.py`:
```
#from swagger_client.models.domain import Domain  # noqa: F401,E501
```

8. python setup.py install
