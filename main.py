import cv2 as Opencv
from consolemenu import *
from consolemenu.items import *


def Contorno(imagen):

    img = Opencv.imread(imagen)

    Opencv.imwrite('Contorno.jpg',Opencv.Canny(img,200,200))

    result = Opencv.imread('Contorno.jpg')
    Opencv.imshow('Imagen Original', img)
    Opencv.imshow('Ejemplo Contorno', result)
    Opencv.waitKey()
    Opencv.destroyAllWindows()

main_menu=ConsoleMenu("Main Menu", "Detección de Contornos")
item_img_hight_detail= FunctionItem("Alto detalle",Contorno, ["images/hightDetail.jpeg"] )
item_img_hight_contrast=FunctionItem("Alto Contraste",Contorno, ["images/hightContrast.jpeg"] )
item_img_blur= FunctionItem("Fondo desenfocado", Contorno,["images/blur.jpeg"])
item_img_animated= FunctionItem("Imagen animada", Contorno, ["images/animado.jpeg"] )
item_img_forest= FunctionItem("Imagen Bosque", Contorno, ["images/forest.jpeg"] )
item_img_ocean= FunctionItem("Imagen Oceano", Contorno, ["images/ocean.jpeg"])
item_img_faces= FunctionItem("Solo rostros", Contorno, ["images/faces.jpeg"])
item_img_galaxy= FunctionItem("Imagen Galaxia",Contorno, ["images/galaxy.png"])
item_img_surrealismo= FunctionItem("Imagen Surrealista", Contorno, ["images/surrealismo.jpg"])
item_img_fiction= FunctionItem("Imagen Ficción", Contorno, ["images/ficcion.jpeg"])

main_menu.append_item(item_img_hight_detail)
main_menu.append_item(item_img_hight_contrast)
main_menu.append_item(item_img_blur)
main_menu.append_item(item_img_animated)
main_menu.append_item(item_img_forest)
main_menu.append_item(item_img_ocean)
main_menu.append_item(item_img_faces)
main_menu.append_item(item_img_galaxy)
main_menu.append_item(item_img_surrealismo)
main_menu.append_item(item_img_fiction)

main_menu.show()