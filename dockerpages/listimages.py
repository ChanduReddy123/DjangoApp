def ListImages(remote_Machine):
    result = remote_Machine.images()
    data = []
    for list in result:
        image = []
        memory =   "{0:.2f}Mb".format(list['Size']/1024/1024)
        name = list['RepoTags'][0]
        image.append(name)
        image.append(memory)
        data.append(image)
    #ListContainers()
    return data