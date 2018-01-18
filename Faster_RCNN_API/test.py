import cv2 as cv2
import test_frcnn as test
test, df = Test_frcnn()
print(df)
for i in range(len(test)):
  cv.imwrite("./test_results/output_{}.png".format(i+1), test[i]) 
