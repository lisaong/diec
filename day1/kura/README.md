## Setup

```
sudo apt-get install python3-pip virtualenv
cd somefoldername
virtualenv –p python3 kura
source kura/bin/activate

pip install -r requirements.txt
```

## Protobuf Setup
```
sudo apt-get install protobuf-compiler
wget https://raw.githubusercontent.com/eclipse/kura/release-4.0.0/kura/org.eclipse.kura.cloudconnection.eclipseiot.mqtt.provider/src/main/protobuf/kurapayload.proto
protoc kurapayload.proto --python_out=.
```

References:
- https://github.com/protocolbuffers/protobuf/issues/2993
- https://github.com/protocolbuffers/protobuf/blob/master/python/google/protobuf/json_format.py
