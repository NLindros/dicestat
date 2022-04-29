import cv2
import numpy as np

class Rect:
    def __init__(self, cv_rect) -> None:
        (x, y), (width, height), angle = cv_rect
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle

    def square_like(self):
        if self.width and self.height:
            return (self.width / self.height) > 0.5
        return False

    def valid_area(self):
        area = self.width * self.height
        return area > 1000 and area < 5000

    def center(self):
        return self.x + self.width, self.y + self.height
        

def center_exist(c1, centers):
    for c2 in centers:
        dist = np.linalg.norm(np.array(c1) - np.array(c2))
        if dist < 10:
            return True
    return False


dice_original = cv2.imread('example.jpg')
dice_grey = cv2.cvtColor(dice_original, cv2.COLOR_BGR2GRAY)
blured = cv2.blur(dice_grey, (3,3))
threshold, black_and_white = cv2.threshold(blured, 170, 255, cv2.THRESH_BINARY)

edges = cv2.Canny(black_and_white, 80, 230)

#cv2.imshow('Edges', edges)
#cv2.waitKey(0)

contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# -1 signifies drawing all contours
#result = cv2.drawContours(dice_original, contours, -1, (0, 255, 0), 3)
#cv2.imshow('Contours', result)
#cv2.waitKey(0)

centers = []

for rect in [Rect(cv2.minAreaRect(contour)) for contour in contours]:

    if not (rect.valid_area() and rect.square_like()):
        continue

    if rect.center




rectangles = [rect for rect in rectangles if rect.squareish() and rect.valid_area()]

all_centers = [np.array(rect.center) for rect in rectangles]

centers = []
for c1 in all_centers:
    centers.append

    



return


for rect in rectangles:
    if valid_area(*size) and squareish(*size):




        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(dice_original, [box], 0, (0, 0, 255), 2)

    

n_dice = len(rectangles)
cv2.putText(dice_original, f"Num dice: {n_dice}", (10,80), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0,255,0))

cv2.imshow('Result', dice_original)
cv2.waitKey(0)

cv2.destroyAllWindows()