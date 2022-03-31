Sampling Strategies [<img src="https://github.com/StarlangSoftware/Sampling/blob/master/video.jpg" width="10%">](https://youtu.be/wijWOiv70nE)
============

## K-Fold cross-validation
In K-fold cross-validation, the aim is to generate K training/validation set pair, where training and validation sets on fold i do no overlap. First, we divide the dataset X into K parts as X<sub>1</sub>; X<sub>2</sub>; ... ; X<sub>K</sub>. Then for each fold i, we use X<sub>i</sub> as the validation set and the remaining as the training set.

Possible values of K are 10 or 30. One extreme case of K-fold cross-validation is leave-one-out, where K = N and each validation set has only one instance.
If we have more computation power, we can have multiple runs of K-fold cross-validation, such as 10 x 10 cross-validation or 5 x 2 cross-validation.

## Bootstrapping

If we have very small datasets, we do not insist on the non-overlap of training and validation sets. In bootstrapping, we generate K multiple training sets, where each training set contains N examples (like the original dataset). To get N examples, we draw examples with replacement. For the validation set, we use the original dataset. The drawback of bootstrapping is that the bootstrap samples overlap more than the cross-validation sample, hence they are more dependent.

For Developers
============

You can also see [Cython](https://github.com/starlangsoftware/Sampling-Cy), [Java](https://github.com/starlangsoftware/Sampling), [C++](https://github.com/starlangsoftware/Sampling-CPP), [Swift](https://github.com/starlangsoftware/Sampling-Swift), [Js](https://github.com/starlangsoftware/Sampling-Js), or [C#](https://github.com/starlangsoftware/Sampling-CS) repository.

## Requirements

* [Python 3.7 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Pip Install

	pip3 install NlpToolkit-Sampling

## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called Sampling will be created. Or you can use below link for exploring the code:

	git clone https://github.com/starlangsoftware/Sampling-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `Sampling-PY` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 

Detailed Description
============

+ [CrossValidation](#crossvalidation)
+ [Bootstrap](#bootstrap)
+ [KFoldCrossValidation](#kfoldcrossvalidation)
+ [StratifiedKFoldCrossValidation](#stratifiedkfoldcrossvalidation)

## CrossValidation

k. eğitim kümesini elde etmek için

	getTrainFold(self, k: int) -> list

k. test kümesini elde etmek için

	getTestFold(self, k: int) -> list

## Bootstrap

Bootstrap için BootStrap sınıfı

	Bootstrap(self, instanceList: list, seed: int)

Örneğin elimizdeki veriler a adlı ArrayList'te olsun. Bu veriler üstünden bir bootstrap 
örneklemi tanımlamak için (5 burada rasgelelik getiren seed'i göstermektedir. 5 
değiştirilerek farklı samplelar elde edilebilir)

	bootstrap = Bootstrap(a, 5)

ardından üretilen sample'ı çekmek için ise

	sample = bootstrap.getSample()

yazılır.

## KFoldCrossValidation

K kat çapraz geçerleme için KFoldCrossValidation sınıfı

	KFoldCrossValidation(self, instanceList: list, K: int, seed: int)

Örneğin elimizdeki veriler a adlı ArrayList'te olsun. Bu veriler üstünden 10 kat çapraz 
geçerleme yapmak için (2 burada rasgelelik getiren seed'i göstermektedir. 2 
değiştirilerek farklı samplelar elde edilebilir)

	kfold = KFoldCrossValidation(a, 10, 2)

ardından yukarıda belirtilen getTrainFold ve getTestFold metodları ile sırasıyla i. eğitim
ve test kümeleri elde edilebilir. 

## StratifiedKFoldCrossValidation

Stratified K kat çapraz geçerleme için StratifiedKFoldCrossValidation sınıfı

	StratifiedKFoldCrossValidation(self, instanceLists: list, K: int, seed: int)

Örneğin elimizdeki veriler a adlı ArrayList of listte olsun. Stratified bir çapraz 
geçerlemede sınıflara ait veriler o sınıfın oranında temsil edildikleri için her bir 
sınıfa ait verilerin ayrı ayrı ArrayList'te olmaları gerekmektedir. Bu veriler üstünden 
30 kat çapraz geçerleme yapmak için (4 burada rasgelelik getiren seed'i göstermektedir. 4 
değiştirilerek farklı samplelar elde edilebilir)

	stratified = StratifiedKFoldCrossValidation(a, 30, 4)

ardından yukarıda belirtilen getTrainFold ve getTestFold metodları ile sırasıyla i. eğitim
ve test kümeleri elde edilebilir. 
