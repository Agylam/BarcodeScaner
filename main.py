from time import sleep

import cv2
from pyzbar.pyzbar import decode


def WebCamBarcodeReader():
    cap = cv2.VideoCapture(int(input("Введите номер камеры: ")))

    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)

        detectedBarcodes = decode(frame)

        if not detectedBarcodes:
            pass
        else:
            for barcode in detectedBarcodes:

                (x, y, w, h) = barcode.rect

                cv2.rectangle(frame, (x - 10, y - 10),
                              (x + w + 10, y + h + 10),
                              (255, 0, 0), 2)

                if barcode.data != "":
                    # Print the barcode data
                    print(barcode.data)
                    print(barcode.type)

        cv2.imshow('Input', frame)

        c = cv2.waitKey(1)
        if c == 27:
            break
        sleep(0.1)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    WebCamBarcodeReader()