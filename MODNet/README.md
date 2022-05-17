<h2 align="center">MODNet: Trimap-Free Portrait Matting in Real Time</h2>

<div align="center"><i>MODNet: Real-Time Trimap-Free Portrait Matting via Objective Decomposition (AAAI 2022)</i></div>

<br />

<img src="doc/gif/homepage_demo.gif" width="100%">

<div align="center">MODNet is a model for <b>real-time</b> portrait matting with <b>only RGB image input</b></div>

ModNet이란?
---
- 사람, 옷 등 전경(background)를 제거해주는 네트워크.   
- 의미론적 추정을 위한 다중 스케일 기능을 융합하기 위해 e-ASPP(Efficient Atrous Spatial Pyramid Pooling) 모듈을 사용하고,   
Trimap이 없는 방법에 공통적인 도메인 이동 문제를 해결하기 위해 자체 감독 SOC(Sub-Objective Consistency) 전략을 사용하였다.   
- 훈련하기가 쉽고, 1080Ti GPU에서 초당 67프레임으로 매우 빠른 실행속도를 보유했다. 또한 MODNet은 일상 사진과 비디오에서 결과가 좋다. 

가상 의류 피팅 GAN 모델에서 사용하는 이유
---
- inference 확인 및 input에 필요한 전경이 제거된 의류 이미지 사진을 얻기 위해 해당 모델을 적용하였다. (전처리 단계)  
![image](https://user-images.githubusercontent.com/74050826/168763275-29cb677b-9eaf-4264-8a08-36ed7b6fc49d.png)  
- 우리 프로젝트에서 필요한 전경이 제거된 의류의 edge 이미지 생성의 예시이다. 구찌 옷 이미지를 사용하였다.
