import csv
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
import seaborn as sns
import statsmodels.api as sm
# The iris data set consists  of 150 rows with basically 4 features which includes petal length,petal width ,sepal length and sepal width of different species of flower
# The iris data set is loaded in the form of csv file and it is imported using the existing csv module and the file is read in reading mode using the existing defined functions
filename = open('Iris project.csv', 'r')
file = csv.DictReader(filename)
# Empty list to store the parameters of the features column wise.
Petal_width=[]
Petal_length=[]
Sepal_width=[]
Sepal_length=[]
# Assigning variable names to the naming convention as in the csv files so that it is easier to use in the rest part of the program.
petal_wid = 'Petal_width'
petal_len = 'Petal_length'
sepal_wid = 'Sepal_width'
sepal_len = 'Sepal_length'

# Looping column wise to include the parameters of features in the defined list.
for col in file:
    Petal_width.append(col[petal_wid])
    Petal_length.append(col[petal_len])
    Sepal_width.append(col[sepal_wid])
    Sepal_length.append(col[sepal_len])

#The function to convert all the list of the features which are collection of strings in the list into the list of integers in order to work,manipulate and analyze the data through various statistical features.
def convert_integer(num):
    if num == 1:
        data_petal_string = Petal_width[:]
        data_petal_integer = [eval(i) for i in data_petal_string]
        return data_petal_integer
    elif num == 2:
        data1_petal_string = Petal_length[:]
        data1_petal_integer = [eval(i) for i in data1_petal_string]
        return data1_petal_integer
    elif num == 3:
        data2_sepal_string = Sepal_width[:]
        data2_sepal_integer = [eval(i) for i in data2_sepal_string]
        return data2_sepal_integer
    elif num == 4 :
        data3_sepal_string = Sepal_length[:]
        data3_sepal_integer = [eval(i) for i in data3_sepal_string]
        return data3_sepal_integer

# The function to plot histogram, box plot and density curve using the features of iris data set which enables the user to visualize the distribution of data.
def plot_graph(data, feature):

    # Histogram Representation
    plt.hist(data)
    plt.title(f"Histogram of {feature}")
    plt.xlabel(feature)
    plt.ylabel("Frequency")
    plt.show()

    # Boxplot Representation
    plt.boxplot(data)
    plt.title(f"Boxplot of {feature}")
    plt.xlabel(feature)
    plt.ylabel("Distribution of the data")
    plt.show()

    # Density Curve Representation
    sns.kdeplot(data)
    plt.title(f"Density Curve of {feature}")
    plt.xlabel(feature)
    plt.ylabel("Frequency")
    plt.show()

#The function to calculate the measures of central tendency and measure of dispersion through the single feature of the data set.
def cal_stat(data,feature):
    print("\nMeasures of Central Tendency:")
    print(f"Minimum and maximum values of {feature}:")
    print(np.min(data))
    print(np.max(data))
    print(f"The first quartile of {feature} :")
    print(np.percentile(data, 25))
    print(f"The third quartile of {feature} :")
    print(np.percentile(data, 75))
    print(f"Mean of {feature}:")
    print(np.mean(data, dtype=np.float64))
    print(f"Median of {feature}:")
    data_sorted = sorted(data)
    print(np.median(data_sorted))
    print(f"Mode of {feature}")
    print(st.mode(data))
    print("\n Measure of Dispersion ")
    print(f"Variance of {feature}")
    print(np.var(data))
    print(f"Standard deviation of {feature}")
    print(np.std(data))
    print(f"The Inter-Quatile Range of {feature}")
    print(np.percentile(data, 75) - np.percentile(data, 25))


# The function to compute the measure of dispersion with two data features.
def cal__stat(data1, data2, feature1, feature2):

  #Covarience
  print("Measure of dispersion")
  print(f"The Covarience of {feature1} and {feature2} :")
  print(np.cov(data1, data2))

  #Correaltion Coefficient
  print(f"The Correlation Coefficient of {feature1} and {feature2} :")
  print(np.corrcoef(data1, data2))

  #Inter-Quatile Range
  print(f"The Inter-Quatile Range of {feature1} and {feature2} :")
  print(np.percentile(data1,75)-np.percentile(data1,25))
  print(np.percentile(data2,75)-np.percentile(data2,25))


# The function to draw scatter , line plot and bar graph of two features in order to visualize its distribution .
def plot__graph(data1, data2, feature1, feature2):

  #Line Graph
  plt.plot(data1, data2)
  plt.title(f"Line Plot of {feature1} v/s {feature2}")
  plt.xlabel(feature1)
  plt.ylabel(feature2)
  plt.show()

  #Scatter Plot
  plt.scatter(data1, data2)
  plt.title(f"Scatter Plot of {feature1} v/s {feature2}")
  plt.xlabel(feature1)
  plt.ylabel(feature2)
  plt.show()

  #Bar Graph
  plt.bar(data1, data2)
  plt.title(f"Bar Graph of {feature1} v/s {feature2}")
  plt.xlabel(feature1)
  plt.ylabel(feature2)
  plt.show()

# The loop which runs as long as the user wants according to the desired features of iris data set present in the file.
while True:
    msg ="Heyyyy!!!!!   we are currently working with iris data set and we have four features to analyze .Please enter which feature you would like to work with\n"
    msg += "Enter -1 if you want to analyze for a single feature or else 0 if you like to analyze for two features\n"
    msg += "Enter -3 if you want to quit\n"
    msg1 = "Enter 1 if you want to analyze the features of petal width , 2 for petal length ,3 for sepal width and 4 for sepal length\n"
    msg1 += "Enter 12for petal width and petal length , 13 for petal width and sepal width , 14 for petal width and sepal length\n"
    msg1 += "Enter 21 for petal length and petal width , 31 for sepal width and petal width , 41 for sepal length and petal width\n"
    msg1 += "Enter 23 for petal length and sepal width , 24 for petal length and sepal length, 34 for sepal width and sepal length\n"
    msg1 += "Enter 32 for sepal width and petal length , 42 for sepal length and petal length, 43 for sepal length and sepal width\n"
    msg1 += "Enter -3 to quit the program\n"
    msg2= "Enter 'a' for graphical representation of data , 'b' for statistical analysis and 'c' for both for one feature.\n"
    msg2 += "Enter 'aa' for graphical representation of data , 'bb' for statistical analysis and 'cc' for both for two features\n"
    prompt = int(input(msg))
    if prompt == -3:
        break
    prompt1 =int(input(msg1))
    if   prompt1 == -3:
        break
    else:
        prompt2 = input(msg2)
        if prompt == -1 :
               if prompt1 == 1 :
                 feature = "Petal Width"
                 d = convert_integer(1)
               elif prompt1 == 2:
                 feature = "Petal Length"
                 d =convert_integer(2)
               elif prompt1 == 3:
                 feature = "Sepal Width"
                 d = convert_integer(3)
               elif prompt1 == 4:
                 feature = "Sepal Width"
                 d = convert_integer(4)
               if prompt2 == 'a' :
                  print("---The graphical analysis of the data---")
                  plot_graph(d , feature)
               elif prompt2 == 'b' :
                   print("---The statistical analysis of the data---")
                   cal_stat(d,feature)
               elif prompt2 == 'c':
                   print("---The statistical analysis of the data---")
                   cal_stat(d, feature)
                   print("---The graphical analysis of the data---")
                   plot_graph(d, feature)


        elif prompt == 0 :
            if prompt1 == 12 or prompt1 == 21:
                if prompt1 == 12:
                 feature1 = "Petal Width"
                 feature2 = "Petal Length"
                 d1 = convert_integer(1)
                 d2 = convert_integer(2)

                else:
                    feature1 = "Petal Length"
                    feature2 = "Petal Width"
                    d1 = convert_integer(2)
                    d1 = convert_integer(1)

            elif prompt1 == 13 or prompt1 == 31:

                if prompt1 == 13:
                    feature1 = "Petal Width"
                    feature2 = "Sepal Width"
                    d1 = convert_integer(1)
                    d2 = convert_integer(3)

                else:
                    feature1 = "Sepal Width"
                    feature2 = "Petal Width"
                    d1 = convert_integer(3)
                    d2 = convert_integer(1)

            elif prompt1 == 14 or prompt1 == 41:
                if prompt1 == 14:
                 feature1 = "Petal Width"
                 feature2 = "Sepal Length"
                 d1 = convert_integer(1)
                 d2 =convert_integer(4)
                else:
                    feature1 = "Sepal Length"
                    feature2 = "Petal Width"
                    d1 = convert_integer(4)
                    d2 = convert_integer(1)

            elif prompt1 == 23 or prompt1 == 32:
                if prompt1 == 23:
                   feature1 = "Petal Length"
                   feature2 = "Sepal Width"
                   d1 = convert_integer(2)
                   d2 =convert_integer(3)
                else:
                    feature1 = "Sepal Width"
                    feature2 = "Petal Length"
                    d1 = convert_integer(3)
                    d2 = convert_integer(2)

            elif prompt1 == 24 or prompt1 == 42:

                if prompt1 == 24:
                 feature1 = "Petal Length"
                 feature2 = "Sepal Length"
                 d1 = convert_integer(2)
                 d2 = convert_integer(4)
                else:
                    feature1 = "Sepal Length"
                    feature2 = "Petal Length"
                    d1 = convert_integer(4)
                    d2 = convert_integer(2)

            elif prompt1 == 34 or prompt1 == 43:

                if prompt1 == 34:
                    feature1 = "Sepal Width"
                    feature2 = "Sepal Length"
                    d1 = convert_integer(3)
                    d2 = convert_integer(4)
                else:
                    feature1 = "Sepal Length"
                    feature2 = "SepalWidth"
                    d1 = convert_integer(4)
                    d2 = convert_integer(3)

        if prompt2 == 'aa' :
            print("--The graphical analysis of the data--")
            plot__graph(d1,d2, feature1,feature2)
        elif prompt2 == 'bb':
            print("--The statistical analysis of the data--")
            cal__stat(d1,d2, feature1,feature2)
        elif prompt2 == 'cc':
            print("--The statistical analysis of the data--")
            cal__stat(d1, d2, feature1, feature2)
            print("--The graphical analysis of the data--")
            plot__graph(d1, d2, feature1, feature2)

