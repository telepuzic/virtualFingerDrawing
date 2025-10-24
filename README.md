This project is called "Drawing on the screen". Its main aim, as the name suggests, is to give users the opportunity to draw on the screen using various gestures and techniques described below.

What do I need to launch?
Install python libraries: mediapipe, numpy, math, cv2.

The main knowledge that can be useful for using the code:
1. You can only draw with your index finger (all fingers are bent, index finger is straight, thumb is not important)
2. To erase everything from the screen, you need to clench your palm into a fist (again, the condition of the thumb is not important)
3. In order to change the color (there are 4 of them), you can apply one of the 2 strategies:
3.1 Show the little finger (then the colors will switch with great frequency, it is difficult to "catch" the desired color)
3.2 On the top panel you can see 4 chickens standing in a row. By pointing your index finger at the circle with the desired color, you will begin to draw with this color. (see img.png)
4. In the upper panel on the left, you can see a circle that shows what color you are currently drawing. (see img_1.png)
5. The original color when you log in to the program is purple

However, this program has several disadvantages.:
1. The main thing is its slowness due to the large amount of information being processed, the smoothness of the line is not preserved. To draw a solid line, you need to move your finger slowly
2. Sometimes inaccurate recognition of hands and gestures. This problem arises due to the imperfection of the mediapipe and cv2 libraries. This problem can be avoided by using the program in good light and clearly showing the previously described gestures.
