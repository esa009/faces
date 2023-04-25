from deepface import DeepFace
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
import io



def img(image_1, image_2):
  image1 = Image.open(io.BytesIO(image_1.get_bytes()))
  image2 = Image.open(io.BytesIO(image_2.get_bytes()))
  image1.save("test.png")
  #image2.save("test2.png")
  #return DeepFace.analyze("/content/test.png", enforce_detection=False)
  return DeepFace.verify("/content/test.png", "/content/test2.png", enforce_detection=False)
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)


!rm /content/drive/MyDrive/anvilfaces/representations_vgg_face.pkl
def compare(image_2):
  image2 = Image.open(io.BytesIO(image_2.get_bytes()))
  image2.save("test2.png")
  result = DeepFace.find(img_path = '/content/test2.png', db_path = '/content/drive/MyDrive/anvilfaces', enforce_detection=False)
  text1 = ""
  for i in range(len(result.values)):
   text1 += str(result.identity[i])[34:-4] + "\n"
  return text1


!rm /content/drive/MyDrive/anvilfaces/representations_vgg_face.pkl
result = ""
def compare2(image_2):
  image2 = Image.open(io.BytesIO(image_2.get_bytes()))
  image2.save("test2.png")
  result = DeepFace.find(img_path = '/content/test2.png', db_path = '/content/drive/MyDrive/anvilfaces', enforce_detection=False)
  text = ""
  for i in range(len(result.values)):
    text += str(result.values[i])[-19:-1] + "\n"
  return text  

!rm /content/drive/MyDrive/anvilfaces/representations_vgg_face.pkl
result = ""
def compare3(image_2):
  image2 = Image.open(io.BytesIO(image_2.get_bytes()))
  image2.save("test2.png")
  result = DeepFace.find(img_path = '/content/test2.png', db_path = '/content/drive/MyDrive/anvilfaces', enforce_detection=False)
  text2 = ""
  text2 = result.identity[0][34:-4]
  return text2
     


!rm /content/drive/MyDrive/anvilfaces/representations_vgg_face.pkl
result = ""
def compare4(image_2):
  image2 = Image.open(io.BytesIO(image_2.get_bytes()))
  image2.save("test2.png")
  result = DeepFace.find(img_path = '/content/test2.png', db_path = '/content/drive/MyDrive/anvilfaces', enforce_detection=False)
  text2 = ""
  if(len(result.values) >= 2):
   text2 = result.identity[1][34:-4]
  return text2



!rm /content/drive/MyDrive/anvilfaces/representations_vgg_face.pkl
result = ""
def compare5(image_2):
  image2 = Image.open(io.BytesIO(image_2.get_bytes()))
  image2.save("test2.png")
  result = DeepFace.find(img_path = '/content/test2.png', db_path = '/content/drive/MyDrive/anvilfaces', enforce_detection=False)
  text2 = ""
  if(len(result.values) >= 3):
   text2 = result.identity[2][34:-4]
  return text2



!rm /content/drive/MyDrive/anvilfaces/representations_vgg_face.pkl
result = ""
def compare6(image_2):
  image2 = Image.open(io.BytesIO(image_2.get_bytes()))
  image2.save("test2.png")
  result = DeepFace.find(img_path = '/content/test2.png', db_path = '/content/drive/MyDrive/anvilfaces', enforce_detection=False)
  text2 = ""
  if(len(result.values) >= 4):
   text2 = result.identity[3][34:-4]
  return text2



!rm /content/drive/MyDrive/anvilfaces/representations_vgg_face.pkl
result = ""
def compare7(image_2):
  image2 = Image.open(io.BytesIO(image_2.get_bytes()))
  image2.save("test2.png")
  result = DeepFace.find(img_path = '/content/test2.png', db_path = '/content/drive/MyDrive/anvilfaces', enforce_detection=False)
  text2 = ""
  if(len(result.values) >= 5):
   text2 = result.identity[4][34:-4]
  return text2


!rm /content/drive/MyDrive/anvilfaces/representations_vgg_face.pkl
result = ""
def compare8(image_2):
  image2 = Image.open(io.BytesIO(image_2.get_bytes()))
  image2.save("test2.png")
  result = DeepFace.find(img_path = '/content/test2.png', db_path = '/content/drive/MyDrive/anvilfaces', enforce_detection=False)
  text2 = ""
  if(len(result.values) >= 6):
    text2 = result.identity[5][34:-4]
  return text2
     





















































