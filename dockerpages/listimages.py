def ListImages(remote_Machine):
    result = remote_Machine.images()
    print(result)
    data = []
    for list in result:
        image = []
        memory =   "{0:.2f}Mb".format(list['Size']/1000/1000)
        if(list['RepoTags']):        
            for tags in list['RepoTags']:
                name = tags
                image.append(name)
                image.append(memory)
                data.append(image)
        elif(list['RepoDigests']):
            name = list['RepoDigests'][0].split('@')[0]
            image.append(name)
            image.append(memory)
            data.append(image)
        else:
            name='none'
            image.append(name)
            image.append(memory)
            data.append(image)
         
    #ListContainers()
    return data