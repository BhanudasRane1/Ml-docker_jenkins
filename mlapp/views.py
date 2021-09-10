from django.shortcuts import render, redirect
from django.views.generic import View 
from .models import Image as imgs
from .forms import ImageForm
from django.contrib import messages
import requests
import tensorflow as tf
from PIL import Image
import numpy as np
from numpy import asarray
import os

# def impropper_access(request):
#      return render(request, 'admin/impropper_access.html')


class Index_Data(View):
    def get(self,request):
        template = 'index.html'
        index_form = ImageForm()

        context = { 
                    'form' : index_form , 
                    
                    } 
                            
        return render(request, template, context)
    def post(self,request):
        image_form = ImageForm(request.POST, request.FILES or None )
        if image_form.is_valid():
            image_form.save()
            messages.success(request, "Your Image Successfully!")
            return redirect('confirmation_url' )
        else:
            messages.warning(request, "Something went Wrong!")
            return redirect('index_url') 
            

class Confirmation(View):
    def get(self,request):
        
        template = 'confirmation.html'
        img = imgs.objects.last()
        print("msdsd")
        with open('static/model_architecture.json', 'r') as json_file:
    	    json_savedModel= json_file.read()
        model_j = tf.keras.models.model_from_json(json_savedModel)
        print("hello")
        model_j.load_weights('static/model_weights.h5')
        model_j.compile(loss='sparse_categorical_crossentropy',optimizer='SGD',metrics=['accuracy'])
         
        a = img.image
        a= str(a)
        c =a.split('/')
        print(c[1])
        path = "I:/dimensionless/mlops/media/img/" + c[1] 
        print(path)
        img = Image.open(path)
        print('img loaded')
        img = asarray(img)
        print(type(img))
        x = np.resize(img, (456,456,3))
        x.reshape(1,456,456,3)
        img_exp = np.expand_dims(x, axis=0)
        result = model_j.predict(img_exp)
        print(result)
        max_val = np.amax(result)
        result = np.where(result == np.amax(result))
        res   = max(result)
        imgforprint= imgs.objects.last()
        context = {
            'img': imgforprint,
            'res' : res
        }
        return render(request, template,context)

    
            


