
def list_Containers(conn):
    containerlist = []
    result=conn.containers(all=True)
    #print(result)
    for container in result:
        details=[]
        if str(container['State']).lower() == 'running':
            #print(container['Names'][0])
            details.append(container['Names'][0])
            details.append(container['State'])
            containerlist.append(details)
        else:
            details.append(container['Names'][0])
            details.append(container['State'])
            containerlist.append(details)
           # print(container['Ports'])
            for data in container['Ports']:
                print("PublicPort:",data['PublicPort'])
           
    return containerlist
