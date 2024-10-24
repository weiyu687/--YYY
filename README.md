# TE-GCN

2024年第六届全球校园人工智能算法精英大赛【算法挑战赛】

基于无人机的人体行为识别

参赛队伍:YYY

此仓库用于赛方复现

## 训练
根目录下`process_data/data`文件夹参照以下内容:
```
data
___ train_joint.npy
___ train_label.npy
___ test_A_joint.npy
___ test_A_label.npy
```
执行以下命令处理原始数据得到bone模态数据:
```commandline
cd ./process_data
python gen_modal.py --modal bone
```

将生成的bone模态数据和标签数据移动到data文件夹下,
根目录的`data`文件夹参照以下内容:
```
data
___ train_bone.npy
___ train_label.npy
___ test_A_bone.npy
___ test_A_label.npy
```
执行以下命令将标签文件转化为pkl格式:
```commandline
python npy2pkl.py data/train_label.npy data train_label
python npy2pkl.py data/test_A_label.npy data test_A_label
```
执行以下命令训练模型:
```commandline
python main.py --config ./config/train.yaml --device 0 --warm_up_epoch 30 --only_train_epoch 30 --seed 777
```
## 测试
将test_B_joint.npy文件移动到`process_data`文件夹下的`data`文件夹下

根目录下`process_data`文件夹参照以下内容:
```
process_data
___ data
  ___ test_B_joint.npy
```

执行以下命令获得bone模态数据:
```commandline
cd ./process_data
python edited_gen_modal.py
```
将获得的test_B_bone.npy文件移动到根目录下的`data`文件夹下

在项目根目录下执行以下命令获取label文件:
```commandline
python generate_npy.py
python npy2pkl.py ./data/test_B_label.npy ./data test_B_label 
```
从[Google Driver](https://drive.google.com/file/d/1-DZJEEIF-Di989yEcSjM4BZHJdhq9ctJ/view?usp=sharing)下载模型权重移动到checkpoint文件夹下

根目录下`checkpoint`文件夹参照以下内容:
```
checkpoint
___ model2-60-23520.pt
```
执行以下命令加载模型权重对测试集进行分类:
```commandline
python main.py --config ./config/test.yaml --device 0 --work-dir ./results/test
```

执行以下命令获取pred.npy文件，生成位置在根目录下:
```commandline
python get_results.py
```