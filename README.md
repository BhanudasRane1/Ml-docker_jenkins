# Ml-docker_jenkins
Dimensionless Tech



How To Run App
1)  Download The model_weights.h5 and Architecture json file ,and  copy paste in static folder in django webapp
Link to download architecture and weight :- 
https://baitrainingdataset.blob.core.windows.net/interviewdata/model_architecture_and_weights.zip

2) Download the Test Images For testing purpose ,
use this link :- 
https://baitrainingdataset.blob.core.windows.net/interviewdata/test_images.zip

3) Prequistics :-  Jenkins and Docker
For pipeline we can use here jenkins and Docker, 

4) Create Django Project and Integrate Ml code . Create github repo so that we can upload code here .

5) Create Dockerfile to launch docker images and container. 

6) Open Jenkins and create job and in that give github repo and command to build dockerfile.


![Screenshot (73)](https://user-images.githubusercontent.com/75332377/132812263-3294cc0d-623d-49d1-bfc0-f035ff6a2847.png)




7) Access website using following url:
ip:8000/

![Screenshot (74)](https://user-images.githubusercontent.com/75332377/132813701-ccdae89f-0c67-4768-acd7-fc88a6591937.png)

Task 1 : Things to think about

option1) We can use kubernetes to automate model also we can integrate wih jenkins . So load balancing and real time updation can do .
In Jenkins we can set hyperparameter so that human work reduced and automatic model inprovement possible.


Task 2 : Things to think about
option1) As i said above we can use kubernetes so that we load balancing happened . Using this we can scan up and scale down containers . And easily take Backup.

option2) We can use jenkins and docker so whenever we want change something we just upload in github , then jenkins automatically detect and update our code. Code is anything like webapp OR Machine Learning.
