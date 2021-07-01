import os
from utils import *
from GradientDescending import *

crtDir = os.getcwd()
filePath = os.path.join(crtDir,'data', 'world-happiness-report-2017.csv')

def univariateRegression():
    inputs, outputs = loadData(filePath, 'Economy..GDP.per.Capita.', 'Happiness.Score')
    inputs = [[el] for el in inputs]
    trainInputs, trainOutputs, testInputs, testOutputs = splitData(inputs, outputs)
    params = {}
    params["trainInputs"] = trainInputs
    params["trainOutputs"] = trainOutputs
    params["testInputs"] = testInputs
    params["testOutputs"] = testOutputs
    params["noIter"] = 10000
    params["learningRate"] = 0.0001
    gd = GradientDescending(params)
    print(gd.errorPrediction())

def bivariateRegression():
    inputs1, outputs = loadData(filePath, 'Economy..GDP.per.Capita.', 'Happiness.Score')
    inputs2, outputs = loadData(filePath, 'Health..Life.Expectancy.', 'Happiness.Score')
    inputs = [[inp1]+[inp2] for inp1,inp2 in zip(inputs1,inputs2)]
    trainInputs, trainOutputs, testInputs, testOutputs = splitData(inputs, outputs)
    params = {}
    params["trainInputs"] = trainInputs
    params["trainOutputs"] = trainOutputs
    params["testInputs"] = testInputs
    params["testOutputs"] = testOutputs
    params["noIter"] = 10000
    params["learningRate"] = 0.0001
    gd = GradientDescending(params)
    print(gd.errorPrediction())

def main():
    print("Univariate regression:")
    univariateRegression()
    print("Bivariate regression:")
    bivariateRegression()

main()