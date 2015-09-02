# ARMA-stock-index-predict

This is a simple program to predict closing point of EURONEXT 100 index . The program attempts to model EURONEXT 100 index into an Autoregressive–moving-average(ARMA) model.
<br /> 
<br />

#How to run project:

<br />

#Requirements:
UNIX environment. <br />

Anaconda 2.3.0
<br />

The project uses extensively several Python data analysis and machine learning libraries, including Pandas, SciPy, Scikit-learn and Matplotlib for plotting result.
Most of these libraries are ready-installed with Anaconda, or can be easily install with Anaconda tool

#Design : 

1.Load EURONEXT 100 index into training data(from starting date(t0) to current date(t(n-1))). <br />
2. Model training data using ARMA
<br />
3. Predict EURONEXT 100 index at date t(n)
