### Convex Hull Problem: A Comparison of Jarvis March and Graham Scan Algorithms

This project serves as a final project submission for Dan Leblanc's CS 584 
Algorithm Design and Analysis class at Portland State University.


This project implements Jarvis March and Graham Scan and tests
the performance of these algorithms on the following sets of data points: 
* A randomly distributed set of points where the number of point on the hull
is unknown
* A set of a points where exactly 3 points lie on the hull
* A set of points where every point in on the hull in a circle

### Usage:

##### Running the Test Suite
The test suite with run a total of 3,300 tests with various point sets 
as default. Results will be stored in a csv file labeled ```test_results.csv``` upon completion.
You can edit the total number of tests to run in ```TestSuite.py``` at the top of the file.
Assuming a linux based terminal you may follow the instructions below to clone the project.
```
Test Suite
$ git clone https://github.com/Aly-Tomato/CS584_ConvexHullProject.git
$ cd CS584_ConvexHullProject 
$ python3 TestSuite.py
```

##### Running the Point Generator:

Once cloned you will have access to the Processing Applications folder
which contains various executables. Find the executable for your specific
machine environment. Note that you'll need at least JAVA 7 to run these applications.
For example, if running on linux 64
```
$cd Processing_Applications/application.linux64
$ chmod +x PointGenerator.exe 
$ ./PointGenerator.exe
```
[![Point Genertor Example Run](https://github.com/Aly-Tomato/CS584_ConvexHullProject/blob/master/Images/VideoThumbnail.JPG)](http://youtu.be/lrnvb3jol0Q?hd=1 "Point Genertor Example Run")



### Results:
You can find thorough explanations of the results in the following research paper  
[Convex Hull Problem: A Comparison of Jarvis March and Graham Scan Algorithms](https://docs.google.com/document/d/1VC5qr3sTwCX5O1JSbs-Pjc_GJwBJu5wLoYspDSl8EPg/edit?usp=sharing).  
Below are links to interactive plot.ly graphs. To my knowledge, these links should work
on all browsers except FireFox.

<a href="https://htmlpreview.github.io/?https://github.com/Aly-Tomato/CS584_ConvexHullProject/blob/master/HTML%20Plot.ly%20Graphs/Convex%20Hull%20Random%20Hull.html" target="_blank">Link to Random Hull Plot.ly Graph</a>  
<a href="https://htmlpreview.github.io/?https://github.com/Aly-Tomato/CS584_ConvexHullProject/blob/master/HTML%20Plot.ly%20Graphs/Convex%20Hull%20Min%20Hull.html" target="_blank">Link to Min Hull Plot.ly Graph</a>  
<a href="https://htmlpreview.github.io/?https://github.com/Aly-Tomato/CS584_ConvexHullProject/blob/master/HTML%20Plot.ly%20Graphs/Convex%20Hull%20Max%20Hull.html" target="_blank">Link to Max Hull Plot.ly Graph</a>  

