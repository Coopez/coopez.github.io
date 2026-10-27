---
title: "Monotonic Neural Networks 2"
date: 2026-07-30
excerpt: "What makes a neural network monotonic?"
# thumbnail: /images/posts/my-image.png   # optional; create images/posts/ and drop a file there
published: false   # kept as a template, hidden from the site. Set to true (and give a real date) to publish.
---



# What makes a neural network monotonic?
In the last blog post, we briefly explored what monotonicity means, what related terms there are and came to the realization that there are still quite a lot of different functions that can be monotonic and may be approximated by neural networks.

## Primer on Neural Networks

Neural networks are a data-driven function approximator in the category of machine learning models. In plain english, they are a type of mathematical tool that can learn (or be automatically adapted) to approximate any given function (given enough data and compute resources).
This was proven to be true for at least a single layer perceptron which is a very basic type of neural network. 
One way to think about neural networks is to think back on highschool and the concept of linear regression.
$$
y = a*x + b
$$
Here we try to fit parameters $(a,b)$ to a set of data points by minimizing the error between our line and each datapoint.  
Neural networks are similar, but extend this idea by introducing a non-linear component (the activation function) and a nested approach (layers) to the parameter arrangement.
Mathematically this can the looks as follows:
$$
y = a_1* (a_2* \sigma(x + b_2)) + b_1$$

## Where is the monotonicity coming in?

Now, we want to introduce a monotonic dependency of the approximated function of a neural network to a specific part of the input. That is the premise of what simple PINNs from blog post 1 are trying to achieve. This is also called a partial monotonic dependence of the output of the neural network to a subset of the input.



<!--
Talk about partial monotonicity Networks
primer on neural Networks
Lin reg, universal approximation
-->
