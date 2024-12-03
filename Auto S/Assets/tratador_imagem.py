import cv2 as cv
import os

def digitalizador(path, nome_arquivo="screenshot.jpg"):
    try:
        file = str(os.path.join(str(path),str(nome_arquivo)))

        image = cv.imread(filename=file)
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        cv.imwrite(file, image)
        cv.imshow("Imagem tratada", image)
        cv.waitKey(0)
    except Exception as e:
        print(f'DIGITALIZADOR ERROR: {e}')
