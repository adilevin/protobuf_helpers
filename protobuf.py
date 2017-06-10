"""
Script for executing protoc using a docker container
"""
import os
import language_specs

class Protoc(object):

    """
    Class for compiling proto definitions into their language bindings
    """

    def __init__(self):
        pass

    def cpp(self, proto_file):
        "Compile a proto file to CPP"
        print "Compiling %s to CPP" % proto_file
        self._compile_messages(lang=language_specs.CPP, proto_file=proto_file)
        self._compile_rpc_services(lang=language_specs.CPP, proto_file=proto_file)

    def _compile_messages(self, lang, proto_file):
        "Compile messages"
        protoc_cmdline = "protoc --proto_path=proto" \
            " --%s=proto ./proto/%s" % (lang.out_arg, proto_file)
        self._run_protoc(image=lang.docker_image,
                         protoc_cmdline=protoc_cmdline)

    def _compile_rpc_services(self, lang, proto_file):
        "Compile services"
        protoc_cmdline = "protoc --proto_path=proto" \
            " --grpc_out=proto --plugin=protoc-gen-grpc=%s" \
            " ./proto/%s" % (lang.grpc_plugin, proto_file)
        self._run_protoc(image=lang.docker_image,
                         protoc_cmdline=protoc_cmdline)

    def _run_protoc(self, image, protoc_cmdline):
        "Execute the protoc command"
        src_dir = os.getcwd()
        mnt = "-v %s:/proto" % src_dir
        shellcmd = "docker run -it %s %s %s" % (mnt, image, protoc_cmdline)
        print "  > %s ... " % shellcmd,
        os.system(shellcmd)
        print "DONE"
