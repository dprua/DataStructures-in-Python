The fear of the LORD is the beginning of knowledge, but fools despise wisdom and discipline. Proverbs 1:7

-------

Honor Code: On my honour, I pledge that I have neither received nor provided improper assistance 
in the completion of this assignment. 
Signed: 박예겸 Student Number: 21600277

<img src="https://github.com/idebtor/DSpy/blob/cab9662b5ff01661ef8034289c92287d02b8e1ed/images/chap2/markdown_tutorial.jpg?raw=true" width=1000>

----

# [퍼셉트론](https://en.wikipedia.org/wiki/Perceptron) 알고리즘

## 알고리즘$^{algorithm}$

우리가 구하고자 하는 것은 입력한 $x$들을 분류해 낼 수 있는 가중치 $w$인데, [로젠블라크](https://en.wikipedia.org/wiki/Frank_Rosenblatt)가 처음 제안한 학습 알고리즘은 다음과 같이 요약할 수 있습니다.

1. 가중치를 0 혹은 무작위 작은 수로 초기화 한다.
1. 각 학습 자료$^{Training Sample} x^{(i)}$에 대해 다음을 실행한다.
    - 출력 $\hat{y}$를 계산한다. 즉 $\hat{y} = h(\mathbf{w^Tx})$
    - 가중지 $w_j$를 조정한다. 즉 $w_j := w_j + \Delta w_j$
<center><img src = "https://github.com/idebtor/KMOOC-ML/blob/master/ipynb/images/person.png?raw=true" width=200 ><br>
그림 1:마크다운 문석 작성하기
</center>