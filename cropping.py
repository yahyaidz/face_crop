from src.detector import detect_faces
from src.utils import show_bboxes
from PIL import Image
import matplotlib.pyplot  as plt
def crop_face(img):
  bounding_boxes, landmarks = detect_faces(img)
  image = show_bboxes(img, bounding_boxes)
  (x, y, h, w)=bounding_boxes[0][:4]
  img = img.crop((x, y, h, w))
  img=img.resize((224,224))
  return img