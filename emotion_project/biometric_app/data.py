import sqlite3
import os
import cv2
import  sys
from PIL import Image
from .models import  unreg,Checking
import glob
import shutil
import os
import biometric_app.config as cfg
import cv2
import numpy as np
from biometric_app.my_face_recognition import f_main
import imutils
from biometric_app import f_Face_info
from importlib import reload
from biometric_app import images_db as img
from .models import Employee
from biometric_app.my_face_recognition import f_storage as st
import traceback



# class Image(object):
#     def __init__(self):
#         self.image_name = []
#
#     def load_directory(self, path='image'):
#         """
#         :param path: Provide Path of File Directory
#         :return: List of images Names
#         """
#         # for image in glob.iglob(f'{path}/*'):
#         for x in os.listdir(path):
#             # self.image_name.append(image)
#             self.image_name.append(x)
#
#         return self.image_name
#
#     def create_database(self, name, image):
#         """
#         :param name: String
#         :param image:  BLOP Data
#         :return: None
#         """
#
#         conn = sqlite3.connect("Image.db")
#         cursor = conn.cursor()
#
#         cursor.execute("""
#         CREATE TABLE IF NOT EXISTS my_table
#         (name TEXT,images BLOP)""")
#
#         cursor.execute(""" INSERT INTO my_table
#         (name, images) VALUES (?,?)""",(name,image))
#
#         conn.commit()
#         cursor.close()
#         conn.close()

path='biometric_app/image'
# path='image'




list=[]
def lst():
    for image in glob.iglob(f'{path}/*'):
        list.append(image)


def main():
    img=list[-1]
    obj1=unreg.objects.create(photo=img)
    #     print(obj1)
    obj1.save()


check_path= 'biometric_app/check'
chck_list=[]
def check_listing():
    for image in glob.iglob(f'{check_path}/*'):
        chck_list.append(image)

def check_main():
    photo=chck_list[-1]
    obj2= Checking.objects.create(image=photo)
    obj2.save()





# lst()
# main()

# def load_image():
#     list_images = os.listdir(paths)
#     print(list_images)

# def load_image():
#     list_images = os.listdir(cfg.path_images)
#     print(list_images)
#     # return list_images

# def copy():
#     src_path = "media/biometric_app/pictures"
#     dst_path = "biometric_app/images_db"
#     shutil.copy(src_path, dst_path)



#
def copy():
    src_dir = "media/biometric_app/pictures"
    # src_dir = img
    dst_dir = "biometric_app/images_db"
    for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):
        shutil.copy(jpgfile, dst_dir)


def loading():
    list_images = os.listdir(cfg.path_images)
    return list_images
    # names,features = st.load_images_to_database()
    # return names,features
# def main():
#     for image in glob.iglob(f'{path}/*'):
#         list.append(image)
        # obj1=unreg.objects.create(photo=image)
        # # print(obj1)
        # obj1.save()


# def main():
#     for x in os.listdir(path):
#         obj1 = unreg.objects.create(photo=x)
#         obj1.save()


    # for image in glob.iglob(f'{path}/*'):
    #     obj1 = unreg.objects.create(photo=image)
    #     obj1.save()


# def main():
#     for x in os.listdir(path):
#         obj1 = unreg.objects.create(photo=x)
#         obj1.save()

# #
#             # obj.create_database(name=x,image=unreg)
#             obj1 = unreg.objects.create(photo=y)
#             obj1.save()
#             # print("{} added to Database".format(x))
#             return obj1.save()


# def main():
#     obj = Image()
#     # os.chdir("images")
#     print(obj.load_directory())
#     for y in obj.load_directory():
#         # print(y)
#     # #
#     #     if ".png" in y:
#     #
#     #         # with open(x,'rb') as f:
#     #         #     data = f.read()
#     #         # obj.create_database(name=x, image=unreg)
#     #         obj1 = unreg.objects.create(photo=y)
#     #         obj1.save()
#     #         # print("{} Added to database ".format(x))
#
#     # #
#         if ".jpg" in y:
#             # with open(x,"rb") as f:
#             #     data = f.read()
#             # obj.create_database(name=x,image=unreg)
#             obj1 = unreg.objects.create(photo=y)
#             obj1.save()
#             # print("{} added to Database".format(x))
#             return obj1.save()




# def main():
#     obj = Image()
#     # os.chdir("images")
#     print(obj.load_directory())
#     for x in obj.load_directory():
#         print(x)
#     #
#         if ".png" in x:
#
#             with open(x,'rb') as f:
#                 data = f.read()
#                 obj.create_database(name=x, image=data)
#                 print("{} Added to database ".format(x))
#
#     # #
#         elif ".jpg" in x:
#             with open(x,"rb") as f:
#                 data = f.read()
#                 obj.create_database(name=x,image=data)
#                 print("{} added to Database".format(x))
#

# def fetch_data():
#     counter = 1
#     # os.chdir("images")
#     conn = sqlite3.connect("Image.db")
#     cursor = conn.cursor()
#
#     data = cursor.execute("""SELECT * FROM my_table""")
#     for x in data.fetchall():
#         print(x[1])
#         with open("{}.png".format(counter),"wb") as f:
#             f.write(x[1])
#             counter= counter + 1
#
#
#     conn.commit()
#     cursor.close()
#     conn.close()

# main()

def load_images():
    list_images = os.listdir(cfg.path_images)
    # filto los archivos que no son imagenes
    list_images = [File for File in list_images if File.endswith(('.jpg','.jpeg','JPEG','.png'))]

    # inicalizo variables
    name = []
    Feats = []

    # ingesta de imagenes
    for file_name in list_images:
        im = cv2.imread(cfg.path_images+os.sep+file_name)

        # obtengo las caracteristicas del rostro
        box_face = f_main.rec_face.detect_face(im)
        feat = f_main.rec_face.get_features(im,box_face)
        if len(feat)!=1:
            '''
            esto significa que no hay rostros o hay mas de un rostro
            '''
            continue
        else:
            # inserto las nuevas caracteristicas en la base de datos
            new_name = file_name.split(".")[0]
            if new_name == "":
                continue
            name.append(new_name)
            if len(Feats)==0:
                Feats = np.frombuffer(feat[0], dtype=np.float64)
            else:
                Feats = np.vstack((Feats,np.frombuffer(feat[0], dtype=np.float64)))


def get_frame():
    ret, frame = cv2.VideoCapture(0).read()

    frame = imutils.resize(frame, width=720)

    # obtenego info del frame
    f_Face_info.get_face_info(frame)




def reload():
    from importlib import reload  # Python 3.4+
    from biometric_app import f_Face_info


    f_Face_info = reload(f_Face_info)
    return f_Face_info