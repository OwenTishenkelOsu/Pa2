import random as rand;
import numpy as np;
import math;
def dataPoints():
    data = [];
    for i in range(75):
        x = rand.uniform(0,1)
        h = rand.uniform(-0.1, 0.1) + 0.5 + 0.4 * math.sin(2*math.pi*x);
        data.append(np.array([x,h]))
    return data;
def whichGaussianCenter(centers,point):
    center = 0;
    distance = math.sqrt(math.pow((point[0] - centers[center,0]),2) + math.pow((point[1] - centers[center,1]),2))
    currentCenter = 0;
    for i in center:
        currentDistance = math.sqrt(math.pow((centers[currentCenter,0]-point[0]),2) + math.pow((centers[currentCenter,1] - point[1]),2))
        if(currentDistance < distance):
           center = currentCenter;
           distance =  currentDistance;
        currentCenter +=1;
    return (center,distance)
def varianceCenter(center,distances):
    sumDistSquared=np.sum(math.pow(distances,2));
    variance = sumDistSquared/len(distances);
    return variance;
def updateCenter(points):
    meanPoint = np.sum(points,0);
    meanPoint = meanPoint/len(points);
    return meanPoint;
    