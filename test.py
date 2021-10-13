from main import NetworkMapper, NetworkConfig, host_wapper, IPPort

mapper = NetworkMapper()

node1 = NetworkConfig()
node1.append(IPPort("192.168.1.1", 80))
node1.append(IPPort("192.168.2.1", 80))
mapper.set_node("lzx", node1)


@host_wapper(mapper, "lzx")
def test(host, port, *args, **kwargs):
    node_info = args[0]
    print(node_info)
    print(host, port)
    print(node_info.next().ip)
    print(node_info.next().port)

if __name__ == '__main__':
    test()
