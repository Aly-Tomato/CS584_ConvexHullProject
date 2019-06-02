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


### Results:
You can find thorough explanations of the results in the following research paper
[Convex Hull Problem: A Comparison of Jarvis March and Graham Scan Algorithms]().
Below are clickable image links to interactive plot.ly graphs.

![Random Hull Points]("Images/Random Points Graph.JPG")  
![Min Hull Points]("Images/Min Hull Graph.JPG")  
![Max Hull Points]("Images/All Hull Points Graph.JPG")  

