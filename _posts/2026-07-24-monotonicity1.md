---
title: "Monotonic Neural Networks 1"
date: 2026-07-24
excerpt: "What was Monotonicity again?"
marimo: true
thumbnail: /images/posts/monotonicity.png
---

{% comment %}
Niklas: paste your blog text into this file. Move the include line below to
wherever you want the interactive plot to appear in your text. To regenerate the
plot after editing notebooks/monotonicity.py, run:  pixi run build-notebooks
{% endcomment %}
*Authors note: The following is intended as a start of a series of blog posts on Monotone Neural Networks. I want to try to keep each item or chapter in the series short, to give myself small delivery goals that can be reached quickly and somewhat consistently. I do not have an overall progression for this in mind just yet and I am pretty sure that I also have much more to learn about it too.*  
*The danger with this approach is that it may be that the order will turn out weird in the end. At the same time, I do not want to confuse prospective readers by changing ordering of the posts, or editing posts before all are written. So, I think the best solution is that the posts will be ordered by number, and if there are newer posts that somehow fit between already existing ones, I will label them as fractions between existing numbers: I.e. 1, 2, 1.5*

Guiding the modelling of data-driven techniques with some kind of prior information is a pretty old idea. This idea is maybe also what inspired physics-informed neural networks (PINNs). In PINNs, a term is added to the loss function of the network which penalizes certain actions, such that the expressions of the network do not violate known physical laws. This is very much *informed* by the known *physical* properties of the problem which is supposed to be modelled. The probably simplest expression for this is a known monotonic relationship between a known variable in the input, and the variable of interest (the output).   

### But what was monotonicity again?

Monotone functions are a set of functions that develop in only one direction: **increasing** or **decreasing**. There is also a distinction between **weakly monotone** and **strictly monotone**. Strictly monotone requires the function to always be either increasing or decreasing, while weakly monotone relaxes this requirement and allows the function to stay constant too. 

In this context, we will mostly stick to weakly increasing monotonicity, as in reality, most relationships which are monotone are so weakly. Meanwhile the distinction between increasing and decreasing is simply a sign change.

We can define this monotonicity mathematically as follows: 
Let $f: X \to \mathbb{R}$ be a function on an ordered domain $X \subseteq \mathbb{R}$. We say $f$ is **weakly increasing** if

$$x_1 \leq x_2 \implies f(x_1) \leq f(x_2) \quad \text{for all } x_1, x_2 \in X.$$

That is, moving to a larger input never decreases the output. Replacing the second $\leq$ with a strict $<$ gives **strictly increasing** monotonicity, and reversing its direction ($\geq$) gives the weakly decreasing case. Note that we can refer to the weakly increasing case also as **non-decreasing**, which means the same. 

Below are examples of weakly increasing monotone functions:

{% include notebooks/monotonicity.html %}

We can see that those functions can still have a lot of different shapes!
