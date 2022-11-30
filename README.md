# Weakening the Influence of Clothing: Universal Clothing Attribute Disentanglement for Person Re-Identification
Accepted by IJCAI-ECAI 2022.  


The Statistics and Comparison of dataset CSCC is listed below.  
## Statistics

|    Dataset                                         | IDs |  Imgs  | Cams |  Degree  |
| :------------:                                     | :---: | :---: |:---: | :---:   |
|  [LTCC](https://arxiv.org/abs/2005.12633)                                          | 152   |17,138 |12    |Moderate |
| [PRCC](https://arxiv.org/abs/2002.02295)           | 221   |33,698 |3     |Moderate |
| [NKUP](https://onlinelibrary.wiley.com/doi/epdf/10.1002/int.22276)         | 107   |9,738  |15    |Moderate |
|   CSCC (Ours)       | 267   |36,700 |13    |Severe   |
Folder structure is as follows:
```
|--train
   |--0001_0000_c12_00.jpg
|--test
   |--0000_0001_c12_00.jpg
|--query
   |--0000_0000_c11_00.jpg
```
The file name of images is organized as Id_Imgid_cCamid_Clothid.jpg  
Id denotes the identity of this person. Imgid denotes which pictures of this identity. Camid denotes the camera which takes this picture. Clothid denotes which set of outfit this identity is wearing. You can use the [python file](CSCC.py) we provided to load the dataset. 

## Privacy issue
As the faces of the people in our dataset are very clear, we mask the faces to protect the privacy. We use [MTCNN](https://ieeexplore.ieee.org/document/7553523/) to detect faces and mask them as a ablation study in our paper. However, we notice that a lot of faces are failed to be detected as the bad performance of MTCNN. Therefore, we use a more well-behaved face detector [RetinaFace](https://openaccess.thecvf.com/content_CVPR_2020/html/Deng_RetinaFace_Single-Shot_Multi-Level_Face_Localisation_in_the_Wild_CVPR_2020_paper.html) to detect faces and mask them. For faces that are still not detected by the face detector, we manually mask them when we think it is necessary.

## Dataset Application
Dataset are made available to researchers only after the receipt and acceptance of a completed and signed [Database Release Agreement](./Database_Release_Agreement.pdf). Dataset can only be used for academic research.  
Please submit requests for the dataset unless otherwise indicated: 12231016@zju.edu.cn
## Statements

## Citation

If you use this dataset for your research, please cite our paper.
```
@inproceedings{Yan_2022_ijcai,
  title="Weakening the Influence of Clothing: Universal Clothing Attribute Disentanglement for Person Re-Identification",
  author=" Yan, Yuming  and  Yu, Huimin  and  Li, Shuzhao  and  Lu, Zhaohui  and  He, Jianfeng and Zhang, Haozhuo and Wang, Runfa ",
  booktitle="IJCAI",
  year="2022",
}
```

