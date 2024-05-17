def add_items(parent, parent_name, items, dataset=None):
    import MDSplus
    for item in items:
        print(item['type'])
        if item['type'] == 'channel_group' :
            child = parent.addNode(f"{item['name'].upper()}".replace('.','_').replace(':','_'), 'STRUCTURE')
            print(f'Child is {child}')
            if len(parent_name) != 0:
                parent_name = f'{parent_name}.{item["name"]}'
            add_items(child, item["name"], item['children'])
        else:
            print(f'Type = {item["type"]}')
            print(f'Type = {item["name"]}')
            print(f'adding {item["name"]}')
            c_node = parent.addNode(item["name"].upper(), 'SIGNAL')
            if (len(parent_name) != 0) :
                qname = f'{parent_name}.{item["name"]}'
            else:
                qname = f'{item["name"]}'
            tree = c_node.tree
            c_node.record = MDSplus.compound.EXT_FUNCTION(None, 
                                                          'getquartz', 
                                                          tree._GID,
                                                          str(qname),
                                                          tree._START_TIME_STRING, 
                                                          tree._END_TIME_STRING, 
                                                          tree._ZERO_TIME_STRING,
                                                          dataset)

# dict_keys(['id', 'active', 'creation_time', 'deactivation_time', 'data_descriptors', 'expiration_time', 'description', 'name', 'tags', 'applications'])
#data_registry_client = quartz.DataRegistryClient(quartz.PRODUCTION_DATA_REGISTRY_URL)

def quartztree(run_id, treename, shotnumber, dataset=None):
    import quartz
    from MDSplus import Tree
    from nsec_from_string import nsec_from_string
    tree = Tree(treename, shotnumber, 'new')
    data_registry_client = quartz.DataRegistryClient(quartz.PRODUCTION_DATA_REGISTRY_URL)
    run_info = data_registry_client.get_run(run_id)

    descriptors_node = tree.addNode('data_descriptors', 'structure')
    datasource_node = descriptors_node.addNode('datasource', 'text')
    datasource_node.record = run_info['data_descriptors'][0]['datasource']['location']
    visualization_node = descriptors_node.addNode('visualization', 'text')
    visualization_node.record = run_info['data_descriptors'][0]['visualization']
    description_node = tree.addNode('description', 'text')
    description_node.record = run_info['description']
    end_time_string_node = tree.addNode('end_time_string', 'text')
    end_time_string_node.addTag('END_TIME_STRING')
    end_time_string_node.record = run_info['deactivation_time']
    end_time_node = tree.addNode('end_time', 'numeric')
    end_time_node.addTag('END_TIME')
    gid_node = tree.addNode('gid', 'text')
    gid_node.addTag('GID')
    gid_node.record = run_info['id']
    name_node = tree.addNode('name', 'text')
    name_node.record = run_info['name']
    start_time_string_node = tree.addNode('start_time_string', 'text')
    start_time_string_node.addTag('START_TIME_STRING')
    start_time_string_node.record = run_info['creation_time']
    start_time_node = tree.addNode('start_time', 'numeric')
    start_time_node.addTag('START_TIME')
    zero_time_string_node = tree.addNode('ZERO_TIME_STRING', 'text')
    zero_time_string_node.addTag('ZERO_TIME_STRING')
    zero_time_string_node.record = run_info['creation_time']
    zero_time_node = tree.addNode('ZERO_TIME', 'numeric')
    zero_time_node.addTag('ZERO_TIME')
    zero_time_node.record = nsec_from_string(run_info['creation_time'])
    start_time_node.record = nsec_from_string(run_info['creation_time'])
    end_time_node.record = nsec_from_string(run_info['deactivation_time'])
    tags_node = tree.addNode('tags', 'text')
#    tags_node.record = run_info['tags'] - is it a list ?

    parent = tree.addNode('quartz', 'structure')

    data_access_client = quartz.DataAccessClient(quartz.PRODUCTION_DATA_ACCESS_URL)
    items = data_access_client.get_channels(run_id, dataset=dataset)
    print(items)
    add_items(parent, '', items)
    tree.write()
