# <h1> Clarity in Chaos: Boosting Few-Shot Classification through Information Suppression and Sparsification 
# <h3> Abstract
<p>The advance of deep learning has invigorated the research of few-shot classification. However, the interference of non-target information in feature representations hampers classification generalization. To tackle this issue, we propose an irrelevant information suppression (IIS) module, which is focused on it suppressing the weight of unimportant information and elevating the sparsity of feature representations. An IIS network with three consecutive IIS modules is developed, to illustrate the progressive suppression of unimportant information and highlighting of key discriminative features of the target. Extensive experiments showcase the superior performance of our IIS network on four widely-used benchmark datasets. Furthermore, we show that the IIS module can be readily used as a plug-in module by state-of-the-art few-shot classifiers, and can clearly further improve their performance.</p>

<div style="text-align: center;">
  <img src="image/IISNet.png" alt="IISNet" style="max-width: 50%; height: auto; display: block; margin: 0 auto;">
  <img src="image/PI.png" alt="PI" style="max-width: 50%; height: auto; display: block; margin: 0 auto;">
</div>


# Change the Dataset_dir
Navigate to the directory /IISNet-main/common/ and edit the utils.py file. Replace the placeholder -data_dir with the path to your dataset directory.

# Training the code 
```cd /IISNet-main/train/xxx.sh <br>
Please set the gpu id which you want to run,then run the file such as "bash aircraft_5w1s.sh".<br>
```
# Testing the code 
```cd /IISNet-main/test/xxx.sh <br>
Please set the gpu id which you want to run,then run the file such as "bash cars_5w5s.sh".
```
# Acknowledgements
Our code is based on the [RENet](https://github.com/dahyun-kang/renet) repository. We extend our thanks to the authors for making their code available. If you use our model and code, please consider citing both the RENet work and our contributions.

# Performence of Aircraft、Cars and CUB
<img src="image/acc_fine graind.png" alt="acc_fine graind" style="max-width: 75%;height: auto;"> <br>

# Performence of mini-ImageNet
<img src="image/acc_mini.png" alt="acc_mini" style="max-width: 75%; height: auto;"> <br>

# Contact
If you have any questions, please create an issue on this repository or contact at [luchenji0310@163.com](mailto:luchenji0310@163.com).
