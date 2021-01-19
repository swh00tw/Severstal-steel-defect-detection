import gdown
#binary_class
url1="https://drive.google.com/u/0/uc?id=1ZzkCjh-8Map8c37LztmOXSmqfqeUC3b_&export=download"
output1= "binary_model_1204.hdf5"
#multi_class
url2="https://drive.google.com/u/0/uc?id=19BRMQhzIlBit_d7FjDABVDowwQrt4k4u&export=download"
output2="multi_class_model_1229.h5"
#defect1
url3="https://drive.google.com/u/0/uc?id=1wI-S_kXT7KJPBZ9Uu-C2SHsa50kcRt0A&export=download"
output3="segment_model_defect1_0110_2.h5"
#defect2
url4="https://drive.google.com/u/0/uc?id=1wrx28rCt_7YAfPKTvtX6Aj-eAWlfKra-&export=download"
output4="segment_model_defect2_0110_2.h5"
#defect3
url5="https://drive.google.com/u/0/uc?id=1-PQZMyN34ZR2SEqxxwg47DWOt6AXTtm7&export=download"
output5="segment_model_defect3_0110_2.h5"
#defect4
url6="https://drive.google.com/u/0/uc?id=1jyffGZqf1lEBTNjYbpMzJiJeG6TtZKF8&export=download"
output6="segment_model_defect4_0110_2.h5"

#download
gdown.download(url1,output1)
gdown.download(url2,output2)
gdown.download(url3,output3)
gdown.download(url4,output4)
gdown.download(url5,output5)
gdown.download(url6,output6)
