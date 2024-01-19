def quartztree(run_id, treename, shotnumber):
    import quartz
    from MDSplus import Tree
    tree = Tree(treename, -1)
    tree.createPulse(shotnumber)
    tree = Tree(treename, shotnumber, 'edit')
    q_node = tree.QUARTZ
    data_access_client = quartz.DataAccessClient(quartz.PRODUCTION_DATA_ACCESS_URL)
    chans = data_access_client.get_channels(run_id)
    for channel_group in chans:
        g_node = q_node.addNode(f".{channel_group['name'].upper()}", 'STRUCTURE')
        print(g_node)
        for channel in channel_group['children']:
            print(f'  Adding {channel["name"].upper()} to {g_node}')
            c_node = g_node.addNode(channel["name"].upper(), 'NUMERIC')
            print(c_node)
    tree.write()
