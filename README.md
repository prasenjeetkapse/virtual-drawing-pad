# virtual-drawing-pad
This is a virtual pad created in opencv python for blue circular/bottel cap.
## steps in making vdp
1) Capture frames and flip it.
2) Now make a pad on which you are going to write.
3) Find the HSV ranges of grey frames.
4) Now creat a mask in hsv range.
5) Find contours.
6) If contours and its area are in the given range then find center of blue bottelcap using moments.
7) Draw the line on pad by following the center of bottel cap.
