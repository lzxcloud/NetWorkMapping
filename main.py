from functools import wraps


class IPPort(object):
    def __init__(self, ip, port):
        self.ip = ip if ip else None
        self.port = port if port else None


class NetworkConfig(object):
    def __init__(self):
        self.socket_list = []
        self.index = 0

    def append(self, IPPort):
        self.socket_list.append(IPPort)

    def iter(self):
        pass

    def next(self):
        pass

    def top(self):
        return self.socket_list[self.index]

    def next(self):
        self.index += 1
        print(self.index)
        return self.socket_list[self.index]


class NetworkMapper(object):
    def __init__(self):
        self.mapper = {}

    def set_node(self, node_name, config):
        self.mapper[node_name] = config

    def get_node(self, node_name):
        return self.mapper[node_name]

    def next(self, node_name):
        return self.mapper[node_name].next()


def host_wapper(NetworkMapper, node_name):
    def _host_wapper(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            host = NetworkMapper.get_node(node_name).top().ip
            port = NetworkMapper.get_node(node_name).top().port
            network_config = NetworkMapper.get_node(node_name)
            return func(host, port, network_config, *args, **kwargs)
        return decorated
    return _host_wapper
