# Dacon Motion Keypoint Detection Challenge

Final Ranking : **50th** / 533 teams

본 대회는 특정 운동 동작을 수행하고 있는 사람의 미리 지정된 각 신체 부위의 위치에서 측정한 Data를 활용하여 신체 동작 마다의 Key Point를 Detection하는 Challenge



## Motion Keypoint Detection Algorithm

- Albumentation을 이용한 Data Augmentation
- EfficientNet-B5를 Base Network로 이용
- Modified Fully Connected Layer를 이용한 Regression 문제로 해결하려함

