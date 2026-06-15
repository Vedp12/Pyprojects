from pyzbar import pyzbar
import cv2
from glob import glob

def decode(image):
    decoded_objects = pyzbar.decode(image)
    if not decoded_objects:
        print("No barcode detected")
    for obj in decoded_objects:
        print("Detected barcode:", obj)
        image = draw_barcode(obj, image)
        print("Type:", obj.type)
        print("Data:", obj.data.decode("utf-8"))  # decode bytes to string
        print()
    return image

def draw_barcode(decoded, image):
    pts = [(point.x, point.y) for point in decoded.polygon]
    for i in range(len(pts)):
        image = cv2.line(image, pts[i], pts[(i+1) % len(pts)], (0, 255, 0), 5)
    image = cv2.rectangle(image,
                          (decoded.rect.left, decoded.rect.top),
                          (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                          (0, 255, 0), 5)
    return image

if __name__ == "__main__":
    barcodes = glob("bar.jpg")
    for barcode_file in barcodes:
        img = cv2.imread(barcode_file)
        img = decode(img)
        cv2.imshow("img", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite("decoded_" + barcode_file, img)
