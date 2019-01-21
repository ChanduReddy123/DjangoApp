from django.shortcuts import render
from docker import Client
from django import forms
from .Pull_Image_form import ImageForm
from .remove_image_form import RemoveImageForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .listimages import ListImages
from  .Connection import remote_Machine,IP
from django.contrib import messages
##########################################################################################################################
def containers(request):
    return render(request,"containers.html",{})
##########################################################################################################################
def images(request): 
    print('this is in images function') 
    form = ImageForm()
    Images = ListImages(remote_Machine)
    containers = ListofContainers()
    list=[]
    for data in containers:
        list.append(data[1])
    return render(request,"images.html",{"Images":Images,"form":form,"containers": list})
##########################################################################################################################  
def remove_image(request):
    if request.method == 'POST':
        image=request.POST.get('Remove')
        remote_Machine.remove_image(image)
    return HttpResponseRedirect('/get-images')
##########################################################################################################################  
def Image_Form(request):
    print('this is in Image_form')
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            image = form.cleaned_data['image']
            tag =form.cleaned_data['tag']
            PullImage(image,tag)
            result=images(request)
            return result
########################################################################################################################## 
def home(request):
    return render(request,"home.html",{})
##########################################################################################################################
def contact(request):
    name = "hello this is h1"
    return render(request,"contact.html",{"name":name})

##########################################################################################################################
def PullImage(image,tag=""):
        print('this is in pull image')
        if len(tag) == 0:
            tag = "latest"
        image+=":"+tag
        print(image)
        try:
            print('pulling the image ',image)
            remote_Machine.pull(image)
            return 1
        except:
            return 0
##########################################################################################################################
def ListContainersUI(request):
    containers=ListofContainers()
    UniqueImages = []
    for data in containers:
        UniqueImages.append(data[1])
    UniqueImages = set(UniqueImages)
    return render(request,"containers.html",{"containers":containers,"IP":IP,"Images":UniqueImages})
##########################################################################################################################
def SearchContainerUI(request):
    containers = ListofContainers()
    UniqueImages = []
    for data in containers:
        UniqueImages.append(data[1])
    UniqueImages = set(UniqueImages)
    if request.method == 'POST':
        request_container=request.POST.get('Image') 
        print('request container is ',request_container) 
        if request_container == 'ALL':
            return render(request,"containers.html",{"containers":containers,"IP":IP,"Images":UniqueImages})
        else:
            print('you selected'+request_container)
            result_list = [] 
           
            for data in containers:
                print(data)
                if request_container in data:
                    print(request_container)
                    result_list.append(data) 
            
            return render(request,"containers.html",{"containers":result_list,"IP":IP,"Images":UniqueImages})
    return render(request,"containers.html",{"containers":containers,"IP":IP,"Images":UniqueImages})
##########################################################################################################################
def ListofContainers():
    containerlist = []
    result=remote_Machine.containers(all=True)
    for container in result:
        details=[]
        details.append(container['Names'][0][1:])
        if container['Image'].find(':') > 0:
            details.append(container['Image'])
        else:
            details.append(container['Image']+":latest")
        details.append(container['State'])
    
        for data in container['Ports']:
            try:
                details.append(data['PublicPort'])
            except KeyError:
                if container['State'] == 'exited':
                    details.append('N/A')
                else:
                    details.append('N/A')
        if len(details) == 3:
            details.append('N/A')
        containerlist.append(details)
    return containerlist
##########################################################################################################################
def stop_contianer(request):
    if request.method == 'POST':
        container=request.POST.get('Stop')
        remote_Machine.stop(container)
    return HttpResponseRedirect('/get-containers')
##########################################################################################################################
def start_container(request):
    if request.method == 'POST':
        container=request.POST.get('Start')
        remote_Machine.start(container)
    return HttpResponseRedirect('/get-containers')

##########################################################################################################################

def CreateContainerUI(request):
    if request.method == 'POST':
        data = request.POST
        imagename = data.__getitem__('Image')
        if ":" in imagename:
            name=imagename.split(':')[0]
            tag=imagename.split(':')[1]
        else:
            name=imagename
            tag=''
        hostport = data.__getitem__('HostPort')
        containerport = data.__getitem__('ContainerPort')
        detachmode = data.__getitem__('Detach')
        container_name= data.__getitem__('ContainerName')
        print(imagename,containerport,hostport,detachmode,container_name)
        if containerport and hostport:
            print('this is in if')
            
            try:
                container_id =remote_Machine.create_container(image=imagename,name=container_name,ports=[hostport],
                                                    detach=detachmode,
                                                    host_config=remote_Machine.create_host_config(port_bindings={containerport:hostport}))
                remote_Machine.start(container_id)
            except Exception:
                result=PullImage(name,tag)
                if result == 0:
                    render(request,"create_container.html",{"alert":result})
                print('the return value for pullimage in createcontainer is ',result)
                container_id =remote_Machine.create_container(image=imagename,name=container_name,ports=[hostport],
                                                    detach=detachmode,
                                                    host_config=remote_Machine.create_host_config(port_bindings={containerport:hostport}))
                remote_Machine.start(container_id)
                print('this is in exception')
            return HttpResponseRedirect('/get-containers')
        else:
            result=PullImage(name,tag)
            if result == 0:
                messages.info(request, 'image is not available')
                return render(request,"create_container.html",{"alert":result})
            print('this is in else')
            print('the return value for pullimage in createcontainer is ',result)
            if result != 0:
                try:
                    container_id =remote_Machine.create_container(image=imagename,name=container_name,detach=detachmode,tty=True)
                    remote_Machine.start(container_id)
                except Exception as inst:
                    print(type(inst))
                    print(inst.args)
                    print('this is ',inst.__dict__)
                    print('explanation is ',inst.__dict__['explanation'])
            return HttpResponseRedirect('/get-containers')
                
    return render(request,"create_container.html",{})
##########################################################################################################################
def CreateContainerBE(request):
    if request.method == 'POST':
        data = request.POST
        imagename = data.__getitem__('Image')
        hostport = int(data.__getitem__('HostPort'))
        containerport = int(data.__getitem__('ContainerPort'))
        detachmode = data.__getitem__('Detach')
        container_name= data.__getitem__('ContainerName')
        print(imagename,containerport,hostport,detachmode,container_name)
##########################################################################################################################
def removecontainer(request):
    print('this is in removecontainer')
    if request.method == 'POST':
        print('--------------------------------------------')
        container=request.POST.get('Remove')
        print(container)
        remote_Machine.stop(container)
        remote_Machine.remove_container(container)
        print('--------------------------------------------')
        return HttpResponseRedirect('/get-containers')

    print('not done')    
    return HttpResponseRedirect('/get-containers')
##########################################################################################################################
def testing(request):
    print(request)
    print('this is in testing function')
    print(request.POST.__getitem__('Container'))
    print('this is in testing')
    return HttpResponseRedirect('/get-containers')