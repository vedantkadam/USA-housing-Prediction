from django.shortcuts import render;
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


def home(request):
    return render(request,"home.html")

def predict(request):
    return render(request,"predict.html")