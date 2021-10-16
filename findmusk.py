import cv2, argparse

## construindo parser
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required = True, help="C:\\repos\\find_musk\\foto-oficial.jpg")
ap.add_argument("-t","--template", required=True, help="C:\\repos\\find_musk\\foto-gabriel.jpg")
args = vars(ap.parse_args())
print('vida')

## carrega imagens de entrada 
print("[INFO] loading images..", args)
image = cv2.imread(args["image"])
template = cv2.imread(args["template"])
templateResiz = cv2.resize(template, (58,58))
cv2.imshow("Image", image)
cv2.imshow("Template", template)
cv2.waitKey()

## realiza comparação de padrão
print("[INFO] template matching..")
result = cv2.matchTemplate(image,templateResiz, cv2.TM_CCOEFF_NORMED)
(minVal,maxVal,minLoc,maxLoc) = cv2.minMaxLoc(result)

## determina local onde foi encontrado o padrão
(startX,startY) = maxLoc
endX = startX + template.shape[1]
endY = startY + template.shape[0]

## desenha quadrado ao redor do padrão encontrado
cv2.rectangle(image, (startX,startY),(endX,endY), (255,0,0),10)

## mostra imagem completa com padrão destacado
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
imgResiz = cv2.resize(image, (960,600))
cv2.imshow("Output", imgResiz)
cv2.waitKey(0) 