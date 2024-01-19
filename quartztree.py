def add_items(parent, items):
    for item in items:
        print(item['type'])
        if item['type'] == 'channel_group' :
            child = parent.addNode(f".{item['name'].upper()}", 'STRUCTURE')
            add_items(child, item['children'])
        else:
            c_node = parent.addNode(item["name"].upper(), 'SIGNAL')

def quartztree(run_id, treename, shotnumber):
    import quartz
    from MDSplus import Tree
    tree = Tree(treename, shotnumber, 'new')
    description_node = tree.addNode('description', 'text')
    end_time_node = tree.addNode('end_time', 'text')
    end_time_node.addTag('END_TIME')
    gid_node = tree.addNode('gid', 'text')
    name_node = tree.addNode('name', 'text')
    start_time_node = tree.addNode('start_time', 'text')
    start_time_node.addTag('START_TIME')
    zero_time_node = tree.addNode('ZERO_TIME', 'text')
    zero_time_node.addTag('ZERO_TIME')
    tags_node = tree.addNode('tags', 'text')
    parent = tree.addNode('quartz', 'structure')

    data_access_client = quartz.DataAccessClient(quartz.PRODUCTION_DATA_ACCESS_URL)
    items = data_access_client.get_channels(run_id)
    add_items(parent, items)
    tree.write()
