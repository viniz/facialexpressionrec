# Cross-Database Facial Expression Recognition Based on Fine-Tuned Deep Convolutional Network

Follow link to access [full paper](http://urlib.net/rep/8JMKD3MGPAW/3PFBDPL?ibiurl.language=en) on SIBGRAPI library.

## Abstract

![ExpressionsImages](https://github.com/viniz/facialexpressionrec/blob/master/7Subjects7Expressions.png?raw=true)
Facial expression recognition is a very important research field to understand human emotions. Many facial expression recognition systems have been proposed in the literature over the years. Some of these methods use neural network approaches with deep architectures to address the problem. Although it seems that the facial expression recognition problem has been solved, there is a large difference between the results achieved using the same database to train and test the network and the cross-database protocol. In this paper, we extensively investigate the performance influence of fine-tuning with cross-database approach. In order to perform the study, the VGG-Face Deep Convolutional Network model (pre-trained for face recognition) was fine-tuned to recognize facial expressions considering different well-established databases in the literature: CK+, JAFFE, MMI, RaFD, KDEF, BU3DFE, and AR Face. The cross-database experiments were organized so that one of the databases was separated as test set and the others as training, and each experiment was ran multiple times to ensure the results. Our results show a significant improvement on the use of pre-trained models against randomly initialized Convolutional Neural Networks on the facial expression recognition problem, for example achieving 88.58\%, 67.03\%, 85.97\%, and 72.55\% average accuracy testing in the CK+, MMI, RaFD, and KDEF, respectively. Additionally, in absolute terms, the results show an improvement in the literature for cross-database facial expression recognition with the use of pre-trained models.


## Models and Codes
The models of the best result in each of five groups on VGG-FineTuning and VGG-Random can be found [here](https://drive.google.com/drive/folders/0B28GajqdPp8_eGtfRkxxdWZjY1E?usp=sharing).

## Aditional information
More informations about this paper at [LCAD wiki](http://www.lcad.inf.ufes.br/wiki/index.php/Cross-Database_Facial_Expression_Recognition_Based_on_Fine-Tuned_Deep_Convolutional_Network)

## Poster
![PosterImage](https://github.com/viniz/facialexpressionrec/blob/master/conference_poster_6-1.png?raw=true)
