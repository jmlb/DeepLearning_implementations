## Genetic Algorithm for optimization of a ConvNet architecture for Dog/Cats image classification

<img src="../imgs_readme/woof_meow.jpg" alt="dataset" style="width: 400px;"/>

Implementation of the Genetic algorithm, where the design of Neural Networks are allowed to evolve so that the validation loss is minimized.
The datset used is the cats and dogs dataset from Kaggle. The model is a light-weight VGG16. 

<img src="../imgs_readme/model.png" alt="model" style="width: 400px;"/>


The feature extractor (Convolutional layers) are kept unchanged, and the fully connected layers ofthe classifier are modified through 4 processes: selection fo best network (lowest validation loss), random selection model, breed and mutation.

<table style="border=0px solid #000"><tr><td>
<img src="../imgs_readme/operator.png" alt="step-by-step" style="width: 400px;"/>
</td></tr>
</table>

Here is an example of distribution of model performance:

<img src="../imgs_readme/distribution.png" alt="model performance" style="width: 400px;"/>
