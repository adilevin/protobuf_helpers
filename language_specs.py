"""
Protobuf specifications for various languages
"""

from collections import namedtuple
Language = namedtuple('Language', ['docker_image', 'out_arg', 'grpc_plugin'])

CPP = Language(
    docker_image='grpc/cxx',
    out_arg='cpp_out',
    grpc_plugin='/usr/local/bin/grpc_cpp_plugin'
)
