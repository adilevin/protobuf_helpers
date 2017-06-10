"""
Compile .proto files in this folder
"""

from protobuf import Protoc

PROTOBUF = Protoc()
PROTOBUF.cpp('bank.proto')
