import cv2
import time
import imutils
import os
from biometric_app import f_Face_info
from cachetools import TTLCache
import datetime, time
from biometric_app.f_Face_info import det
from biometric_app.f_Face_info import name
from .models import Employee, Detected
from .forms import EmployeeForm
from .models import unreg

import numpy as np
from biometric_app.data import main
from biometric_app.data import lst,check_listing,check_main
from biometric_app import views
import face_recognition
from django.conf import settings
cache = TTLCache(maxsize=20, ttl=60)


from biometric_app.models import Employee, Detected
from cachetools import TTLCache
import datetime, time
from biometric_app.my_face_recognition import f_main
rec_face = f_main.rec()



def identify1(frame, name):

    # timestamp = datetime.datetime.now(tz=timezone.utc)
    timestamp = datetime.datetime.today()
    # timestamp = datetime.datetime.second

    print(name, timestamp)
    # cache[name] = 'detected'
    path = 'detected/{}_{}.jpg'.format(name, timestamp)
    # write_path = 'media/' + path
    cv2.imwrite(path, frame)
    try:
        emp = Employee.objects.get(name=name)
        emp.detected_set.create(time_stamp=timestamp, photo=path)
    except:
        pass


def unknown(out):
    if name(out) == 'unknown':
        release=cv2.VideoCapture(0).release()
        return release


# def identify1(frame, name, buf, buf_length, known_conf):
#     # if name in cache:
#     #     return
#     count = 0
#     for ele in buf:
#         count += ele.count(name)
#
#
#
#     if count >= known_conf:
#         # timestamp = datetime.datetime.now(tz=timezone.utc)
#         timestamp = datetime.datetime.today()
#         print(name, timestamp)
#         cache[name] = 'detected'
#         path = 'detected/{}_{}.jpg'.format(name, timestamp)
#         write_path = 'media/' + path
#         cv2.imwrite(path, frame)
#         try:
#             emp = Employee.objects.get(name=name)
#             emp.detected_set.create(time_stamp=timestamp, photo=path)
#         except:
#             pass



global buf_length, known_conf ,i
buf_length = 10
known_conf = 6
i = 0

#
# def name(names,img):
#     buf = [[]] * buf_length
#     face_names=[]
#     for data_face in names:
#         box = data_face["bbx_frontal_face"]
#         if len(box) == 0:
#             continue
#         else:
#             x0,y0,x1,y1 = box
#             img = cv2.rectangle(img,
#                             (x0,y0),
#                             (x1,y1),
#                             (0,255,0),2);
#             thickness = 2
#             fontSize = 1.0
#             step = 13
#
#             try:
#                 cv2.putText(img, "name: " + data_face["name"], (x0, y0 - step - 10 * 2), cv2.FONT_HERSHEY_SIMPLEX,
#                             fontSize, (0, 0, 255), thickness)
#
#             except:
#                 pass
#     return data_face









# def get_face_info(im):
#     # face detection
#     boxes_face = face_recognition.face_locations(im)
#     out = []
#     if len(boxes_face)!=0:
#         for box_face in boxes_face:
#             # segmento rostro
#             box_face_fc = box_face
#             x0,y1,x1,y0 = box_face
#             box_face = np.array([y0,x0,y1,x1])
#             face_features = {
#                 "name":[],
#                 # "age":[],
#                 # "gender":[],
#                 # "race":[],
#                 # "emotion":[],
#                 "bbx_frontal_face":box_face
#             }
#
#             face_image = im[x0:x1,y0:y1]
#
#             # -------------------------------------- face_recognition ---------------------------------------
#             face_features["name"] = rec_face.recognize_face2(im,[box_face_fc])[0]
#
#             # -------------------------------------- age_detection ---------------------------------------
#             # age = age_detector.predict_age(face_image)
#             # face_features["age"] = str(round(age,2))
#
#             # -------------------------------------- gender_detection ---------------------------------------
#             # face_features["gender"] = gender_detector.predict_gender(face_image)
#
#             # -------------------------------------- race_detection ---------------------------------------
#             # face_features["race"] = race_detector.predict_race(face_image)
#
#             # -------------------------------------- emotion_detection ---------------------------------------
#             # _,emotion = emotion_detector.get_emotion(im,[box_face])
#             # face_features["emotion"] = emotion[0]
#
#             # -------------------------------------- out ---------------------------------------
#             out.append(face_features)
#     else:
#         face_features = {
#             "name":[],
#             # "age":[],
#             # "gender":[],
#             # "race":[],
#             # "emotion":[],
#             "bbx_frontal_face":[]
#         }
#         out.append(face_features)
#     return out
#
#
# face_names=[]
#
# def bounding_box(out,img):
#     buf = [[]] * buf_length
#     i = 0
#     face_names=[]
#     for data_face in out:
#         box = data_face["bbx_frontal_face"]
#         if len(box) == 0:
#             continue
#         else:
#             x0,y0,x1,y1 = box
#             img = cv2.rectangle(img,
#                             (x0,y0),
#                             (x1,y1),
#                             (0,255,0),2);
#             thickness = 2
#             fontSize = 1.0
#             step = 13
#
#             # try:
#             #     cv2.putText(img, "age: " +data_face["age"], (x0, y0-7), cv2.FONT_HERSHEY_SIMPLEX, fontSize, (0,255,0), thickness)
#             # except:
#             #     pass
#             # try:
#             #     cv2.putText(img, "gender: " +data_face["gender"], (x0, y0-step-10*1), cv2.FONT_HERSHEY_SIMPLEX, fontSize, (0,255,0), thickness)
#             # except:
#             #     pass
#             # try:
#             #     cv2.putText(img, "race: " +data_face["race"], (x0, y0-step-10*3), cv2.FONT_HERSHEY_SIMPLEX, fontSize, (0,255,0), thickness)
#             # except:
#             #     pass
#             try:
#                 cv2.putText(img, "emotion: " +data_face["emotion"], (x0, y0-step-10*5), cv2.FONT_HERSHEY_SIMPLEX, fontSize, (0,255,0), thickness)
#             except:
#                 pass
#             try:
#                 cv2.putText(img, "name: " +data_face["name"], (x0, y0-step-10*2), cv2.FONT_HERSHEY_SIMPLEX, fontSize, (0,0,255), thickness)
#                 identify1(img,data_face["name"],buf,buf_length,known_conf)
#             except:
#                 pass
#             # identify1(img, data_face['name'], buf, buf_length, known_conf)
#             # face_names.append(data_face['name'])
#             # buf[i] = face_names
#             # i = (i + 1) % buf_length















class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.buf = [[]] * buf_length
        # self.buf = [] * buf_length
        self.i = 0
        self.buf_length = 10
        self.known_conf = 6

    def __del__(self):
        self.video.release()





    def get_frame(self):
        star_time = time.time()
        ret, frame = self.video.read()
        face_names = []

        frame = imutils.resize(frame, width=720)

        # obtenego info del frame
        out = f_Face_info.get_face_info(frame)


        # pintar imagen
        frame  = f_Face_info.bounding_box(out, frame)

        end_time = time.time() - star_time
        FPS = 1 / end_time
        cv2.putText(frame , f"FPS: {round(FPS, 3)}", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        print(name(out))

        # identify1(frame,name(out),self.buf,self.buf_length,self.known_conf)
        identify1(frame,name(out))
        if name(out) == "unknow":
            # self.video.release()
            now = datetime.datetime.today()
            pht="detected{}.jpg".format(str(now).replace(":", ''))
            # p=os.path.sep.join(['biometric_app/image', "detected{}.jpg".format(str(now).replace(":", ''))])
            # p=os.path.sep.join(['biometric_app/image', pht])
            p1= os.path.sep.join(['biometric_app/image',pht])
            p2= os.path.sep.join(['media/biometric_app/image',pht])
            # p=os.path.sep.join(['biometric_app/image', "detected.png".replace(":", '')])

            # cv2.imwrite(saving(), frame)
            cv2.imwrite(p1, frame)
            cv2.imwrite(p2, frame)
            lst()
            main()

            # unreg()


        # face_names.append(name(out))
        elif name(out) == views.check_list():
            now = datetime.datetime.today()
            pht = "detected{}.jpg".format(str(now).replace(":", ''))
            # p=os.path.sep.join(['biometric_app/image', "detected{}.jpg".format(str(now).replace(":", ''))])
            # p=os.path.sep.join(['biometric_app/image', pht])
            s1 = os.path.sep.join(['biometric_app/check', pht])
            s2 = os.path.sep.join(['media/biometric_app/check', pht])
            cv2.imwrite(s1, frame)
            cv2.imwrite(s2, frame)
            check_listing()
            check_main()





        self.buf[self.i] = name(out)
        self.i = (self.i + 1) % self.buf_length



        # print(det(out,frame))



        # for item in f_Face_info.get_face_info(frame):
        #
        #     face_names.append(item)
        #     self.buf[self.i] = face_names
        #     self.i = (self.i + 1) % self.buf_length
        ret, frame = cv2.imencode('.jpg', frame)

        return frame.tobytes()

        # ret, buffer = cv2.imencode('.jpg', frame)
        # frame = buffer.tobytes()
        # yield (b'--frame\r\n'
        #        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')




class unknowncam(object):

    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret, frame = self.video.read()
        # rgb_small_frame = frame[:, :, ::-1]

        # face_locations = face_recognition.face_locations(rgb_small_frame)
        # print(len(face_locations))
        #
        # cv2.imshow("Video", frame)
        # if not ret:
        #     break
        #
        # now = datetime.datetime.today()
        # p=os.path.sep.join(['biometric_app/image', "detected{}.jpg".format(str(now).replace(":", ''))])
        # cv2.imwrite(p, frame)



        # k = cv2.waitKey(1)
        #
        # if k % 256 == 27:
        #     # ESC pressed
        #     print("Escape hit, closing...")
        # #
        # #
        # elif k % 256 == 32:
        #     # SPACE pressed
        #     img_name = "biometric_app/images_db/detect.jpg"
        #     # img_name = os.path.join(
        #     #     settings.BASE_DIR, "biometric_app/images_db/detect.jpg")
        # #
        #     cv2.imwrite(img_name, frame)
        #     print("{} written!".format(img_name))

        ret, frame = cv2.imencode('.jpg', frame)

        return frame.tobytes()




