### 프로젝트 설명

---

NVIDIA의 Jetson Nano Board 위에서 GAN 모델(없는 이미지를 그럴듯하게 생성해내는 컴퓨터비전 모델) 중 하나인 Virtual Clothes Fitting(가상 의류 피팅) model인 pf-afn의 속도 최적화를 진행. 

성능이 좋은 타 GPU들과는 다르게 Jetson Nano Board는 저렴한 가격으로 매우 간단한 성능만을 가지고 있기에 다른 GPU보다 속도가 느려 최적화가 필수적

![image](https://user-images.githubusercontent.com/74050826/168761866-abefac57-6468-449a-b3c0-1c849a2f9060.png)

Jetson Nano Board

따라서 가상 의류 피팅 모델을 이루는 두 가지 모델 warping model과 gen model 중 gen model에 tensorRT를 적용하여 평균 추론 속도를 약 10배 빠르게 만드는 데 성공하였다.

![image](https://user-images.githubusercontent.com/74050826/168762113-7e360a75-7dc3-4e3c-a42c-67f1ebfa4731.png)

가상 옷 피팅 inference 결과

![image](https://user-images.githubusercontent.com/74050826/168762140-34caa1eb-c045-407c-bb24-81e1669f5837.png)

tensorRT 적용 전(평균 0.053)

![image](https://user-images.githubusercontent.com/74050826/168762167-05fcc6ee-33da-4c79-9ea2-d2c86a5d895c.png)

tensorRT 적용 후(평균 0.0038)

### 코드

---

![image](https://user-images.githubusercontent.com/74050826/168762205-854c77ce-80f7-442b-a4c0-720bac7f91c0.png)

### 어려웠던 점

---

1. MLOps 개발환경 구성 - 라이브러리들 간의 호환성
- Jetpack 을 사용하여 필요한 OS image와 라이브러리들을 구성하였는데, 이 과정에서 pf-afn 모델에 필요한 라이브러리와 Jetson Nano Board의 JetPack이 가진 호환성의 한계로 인해 개발환경을 구성하는데에 어려움이 있었음

![image](https://user-images.githubusercontent.com/74050826/168762249-64b1c7ae-e014-400b-b17c-01f558a37a9e.png)

1. Optimization 의 원리 이해 
- 왜 tensorRT를 사용하면 인공지능의 추론 속도가 빨라지는지?

tensorRT : 딥러닝 모델에 GPU 최적화 기술(Quantization & Precision Calibration / Graph Optimization / Kernel Auto-tuning / Dynamic Tensor Memory & Multi-stream execution)을 적용시켜  NVIDIA GPU 상에서 추론 속도를 수배~수십배 향상시켜주는 모델 최적화 엔진. 

[[TensorRT] NVIDIA TensorRT 개념, 설치방법, 사용하기](https://eehoeskrap.tistory.com/414)

- tensorRT를 복잡한 GAN 모델에 어떻게 적용해야 할지?

우리가 사용한 GAN 모델은 총 2개의 모델 : warping model과 gen model로 이루어져 있었고, torch2trt를 이용해 gen model에 tensorRT를 적용할 수 있었다.

pytorch 모델 → torch2trt → tensorRT 적용(FP32 → FP16)

### 해결방법

---

1. 사전학습 모델 원작자의 환경이 아닌 보급형 사양의 Jetson Nano Board에 적합한 개발환경 마련
    
    (swap 메모리 할당, 호환이 맞는 라이브러리 탐색 후 설치)
    
2. gen model 에 tensorRT 적용
    
    (model 분석 후 torch2trt 적용)
    

### 추후 진행방향

---

- Pretrained 된 모델의 속도를 최적화한 것이라 training을 진행하지는 않았다. 주어진 VITON Dataset과 추가 데이터셋을 합하여 더 정교한 데이터셋을 직접 구성하여 고사양의 GPU에서 training을 직접 시켜봄으로써 GAN모델의 inference의 속도 뿐 아니라 정확도(더 그럴듯하게 옷을 합성) 해보고 싶음.
- warping 모델에도 tensorRT 또는 타 최적화방법 적용시켜보고 싶음.
