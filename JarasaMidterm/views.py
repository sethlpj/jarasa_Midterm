from django.http import HttpResponse

def docker(request):
    return HttpResponse("What is Docker? Docker makes development efficient and predictable Docker takes away repetitive, mundane configuration tasks and is used throughout the development lifecycle for fast, easy and portaple application development desktop and cloud. Docker's comprehensive end to end platform includes UIs, CLIs, APIs and security that are engineered to work together across the entire application delivery lifecycle. ")

def build(request):
    return HttpResponse("BUILD Get a head start on your coding by leveraging Docker images to efficiently develop your own unique applications on Windows and Mac. Create your multi-container application using Docker Compose. Integrate with your favorite tools throughout your development pipeline -Docker works with all development tools you use including VS Code, CircleCI and GitHub. Package applications as portable container images to run in any environment consistently from on premises Kubernetes to AWS ECS, Azure ACI, Google GKE and more. ")

def share(request):
    return HttpResponse("SHARELeverage Docker Trusted Content, including Docker Official Images and images from Docker Verified Publishers from the Docker Hub repository. Innovate by collaborating with team members and other developers and by easily publishing images to Docker Hub.Personalize developer access to images with roles based access and get insights into activity history with Docker Hub Audit Logs. ")

def run(request):
    return HttpResponse("RUN Deliver multiple applications hassle free and have them run the same way on all your environments including design, testing, staging and production --desktop or cloud-native. Deploy your applications in separate containers independently and in different languages. Reduce the risk of conflict between languages, libraries or frameworks. Speed development with the simplicity of Docker Compose CLI and with one command, launch your applications locally and on the cloud with AWS ECS and Azure ACI. ")