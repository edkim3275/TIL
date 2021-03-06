#   tree🌴

박영준 교수님

## 1. 개요

### 1.1. 목차

- 트리
- 이진 트리
- 이진탐색 트리
- 힙

---

### 1.2. 개념

![image-20210405101323141](tree.assets/image-20210405101323141.png)

![image-20210405101448418](tree.assets/image-20210405101448418.png)

![image-20210405101438817](tree.assets/image-20210405101438817.png)

![image-20210405101802972](tree.assets/image-20210405101802972.png)

![image-202104051018197](tree.assets/image-20210405101810997.png)![image-20210405102029796](tree.assets/image-20210405102029796.png)

![image-20210405102320825](tree.assets/image-20210405102320825.png)

- 차수

  ![image-20210405102402995](tree.assets/image-20210405102402995.png)

  - 노드의 차수 : 노드에 연결된 자식 노드의 수
  - 트리의 차수 : 트리에 있는 노드의 차수 중에서 가장 큰 값
  - 단말 노드 : 차수가 0인 노드

- 높이

  ![image-20210405102407486](tree.assets/image-20210405102407486.png)

  - 노드의 높이 : 루트에서 노드에 이르는 간선의 수, 노드의 레벨
    - B의 높이  = 1, F의 높이 = 2
  - 트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 값. 최대 레벨

**Q : 차수랑 높이가 다른건가요? 똑같은 느낌인데**

---

## 2. 이진트리

![image-20210405102907588](tree.assets/image-20210405102907588.png)

![image-20210405103200490](tree.assets/image-20210405103200490.png)

2진수로 생각하는게 좀 더 쉽습니다. h = 3 일때 -> 2^0 + 2^1 + 2^2 + 2^3 --> 1111 = 10000 - 1

![image-20210405104302869](tree.assets/image-20210405104302869.png)

- 포화 이진 트리

  ![image-20210405104621013](tree.assets/image-20210405104621013.png)

  - 모든 레벨에 노드가 포화상태로 차 있는 이진 트리(꽉 차있는 경우)
  - 따로 구분하는 이유는 이진트리중에서 노드번호를 붙이는, 항상 2개의 자식을 가지는 경우를 따로 취급하기 위해서

- 완전 이진 트리

  ![image-20210405104824632](tree.assets/image-20210405104824632.png)

  ![image-20210405104830741](tree.assets/image-20210405104830741.png)

  - 꽉 차있을수도있고 아니기도 하지만, 중간에 빈자리가 없어야만 합니다.(예를들어 이경우 9번이 없으면 완전 이진트리가 아닙니다)

- 편향 이진 트리

  ![image-20210405105210403](tree.assets/image-20210405105210403.png)

  ![image-20210405105216593](tree.assets/image-20210405105216593.png)

  - 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리
    - 왼쪽 편향 이진 트리
    - 오른쪽 편향 이진 트리
  - 비선형자료구조의 장점을 잃어버린 선형자료구조와 마찬가지

### 2.1. 이진트리 순회(traversal)

![image-20210405105411485](tree.assets/image-20210405105411485.png)

![image-20210405105420137](tree.assets/image-20210405105420137.png)

- 3가지 순회방법 : 용도, 상황에 맞게 활용하면 됩니다.

  ![image-20210405105519939](tree.assets/image-20210405105519939.png)

  ![image-20210405105718996](tree.assets/image-20210405105718996.png)

  - 전위순회 : 부모노드 방문 후, 자식노드를 좌, 우 순서로 방문
  - 중위순회 : (부모노드 접근은하지만) 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문
  - 후위순회 : 자식노드를 좌우 순서로 방문한 후, 부모노드로 방문

  하나의 상황에서 전위, 중위순회 둘 다 사용되기도 합니다.(섞어서 사용되는 경우도 존재합니다.)
  
  이거 진짜 쉽게 설명하는 방법을 고안해 냈습니다  
  
  1. 전위 => 노드에 도착하자 마자 찍는다
  2. 중위 => 왼쪽으로 내려보낸 친구가 나한테 '돌아올'때 찍는다
  3. 후위 -> 양옆으로 내려보낸 친구가 둘다 나한테  '돌아올때' 찍는다

#### 2.1.1. 전위순회(preorder traversal)

![image-20210405105909730](tree.assets/image-20210405105909730.png)

- 현재 노드를 방문하여 처리 -> 왼쪽 서브트리로 이동 -> 오른쪽 서브트리로 이동

- 유효한 노드 ?  존재여부에 통과한 노드

  ![image-20210405110323590](tree.assets/image-20210405110323590.png)

- 전위순회 예

  ![image-20210405110402493](tree.assets/image-20210405110402493.png)

  굳이 root부터 시작할 필요는 없습니다. 원하는 노드에서 시작하면 됨

  dfs와 같은경우지만 트리를 따로 사용하는 경우가 있습니다.

#### 2.1.2. 중위순회(inorder traversal)

![image-20210405110952563](tree.assets/image-20210405110952563.png)

왼쪽 -> 현재노드 -> 오른쪽

![image-20210405111052954](tree.assets/image-20210405111052954.png)

진입하면 일단 왼쪽으로 쭉 간다.

#### 2.1.3. 후위순회(postorder traversal)

![image-20210405111319201](tree.assets/image-20210405111319201.png)

![image-20210405111418182](tree.assets/image-20210405111418182.png)

마찬가지로 왼쪽으로 쭉 가다가 오른쪽 

D 가고 B처리하기 전에 오른쪽(T3)로 가서 H I B 그리고 A처리하기 전에 다시 왼쪽으로 쭉 가서 F G C A

후위 순위의 경우 root가 마지막으로 처리가 됩니다.

---

#### 2.1.4. 연습문제

![image-20210405111814938](tree.assets/image-20210405111814938.png)

- 전위순회 : A  B  D  H  I  E  J  C  F  K  G  L  M

  ![image-20210405112030705](tree.assets/image-20210405112030705.png)

- 중위순회 : H  D  I  B  J  E  A  F  K  C  L  G  M

  ![image-20210405112442128](tree.assets/image-20210405112442128.png)

- 후위순회 : H  I  D  J  E  B  K  F  L  M  G  C  A

  ![image-20210405112725526](tree.assets/image-20210405112725526.png)

### 2.2. 이진트리의 표현

![image-20210405112816799](tree.assets/image-20210405112816799.png)

- 노드 번호의 성질

  ![image-20210405140541191](tree.assets/image-20210405140541191.png)

  - 노드 번호를 배열의 인덱스로 활용. 포화이진트리에서 0번은 사용하지 않는다.

  - 노드 번호가 i인 노드의 부모 노드 번호 : i/2(내림)  이것을 floor연산이라 함

    - 첫번째는 -1.5가 나오면 소수점 밑의 수를 다 버리게 되고 두번째는 floor연산과 같이 -1.5보다 작은 정수값이 나오게 됩니다.
    - 알고리즘 문제에서 음수 나누기 할 때는 int(-3/2) 로 해야합니다. 왜냐면, 파이썬으로만 문제를 푸는게 아니라서. 다른 언어와 동일한 계산결과를 얻기 위해서..int()를 사용해서 소수점 이하를 버려야 합니다.

    ![image-20210405140938901](tree.assets/image-20210405140938901.png)

  - 노드 번호가 i인 노드의 왼쪽 자식 노드 번호 : 2*i

  - 노드 번호가 i인 노드의 오른쪽 자식 노드 번호 : 2*i+1

  - 레벨 n의 노드 번호 시작 번호 : 2^n

- 배열을 이용한 이진 트리표현

  ![image-20210405141515199](tree.assets/image-20210405141515199.png)

  편향 이진트리의 경우 빈공간이 너무많이 생겨난다.

  ![image-20210405141526632](tree.assets/image-20210405141526632.png)

  ![image-20210405141603468](tree.assets/image-20210405141603468.png)

  단순히 읽어와서 쓰는 것을 가능하나 전체 연결자체를 바꿀경우 이 방법은 조금 어렵다.

- 연결리스트

  ![image-20210405141711909](tree.assets/image-20210405141711909.png)

  ![image-20210405141722048](tree.assets/image-20210405141722048.png)

  왼쪽, 오른쪽 노드에대한 주소 2개를 가지고 있어야만 한다.

  ![image-20210405141911125](tree.assets/image-20210405141911125.png)

  - 리프노드는 더이상 주소가 필요없기 때문에 null로 표현

#### 연습문제

![image-20210405142037719](tree.assets/image-20210405142037719.png)

V = 간선수 + 1

- 정점의 개수 13개라는 말은 간선 + 1개 = 13이라는 의미

![image-20210405142239160](tree.assets/image-20210405142239160.png)

- 완전, 포화이진트리 아니고, 특별한 규칙이 없다. 보통의 트리는 위와 같이 주어진다.

- 1~6까지 노드가 존재한다.

- 5개 간선이 존재한다.

![image-20210405142343275](tree.assets/image-20210405142343275.png)

- root는 아무 번호나 가능하다(1번이 반드시 root는 아니다.)

![image-20210405142725393](tree.assets/image-20210405142725393.png)

순회는 굳이 root부터 할 필요없습니다. 탐색을 시작한 노드가 root가 됩니다. 나만 그래프 탐색과 다른점은 원래 시작점으로 돌아올 경우 상위트리로 올라가는 것이 아니라 탐색이 종료됩니다.

- 주의점

  포화이진트리 특징 가지고있느냐 아니냐

  부모와 자식에대한 예를 들면서 부모가 번호가 더 작은경우가 많은데, 더 클 수 도있다.

  ![image-20210405143503669](tree.assets/image-20210405143503669.png)

- 자식 노드를 인덱스로 부모 번호를 저장

  ![image-20210405143655689](tree.assets/image-20210405143655689.png)

- 활용

  ![image-20210405143839044](tree.assets/image-20210405143839044.png)

  - 부모가 없는 노드

  - 조상 찾기

- 3번부터 순회를 할경우(전위순회)

  ![image-20210405144441312](tree.assets/image-20210405144441312.png)

  3의 자손의 개수는 2개

#### 연습문제

![image-20210405144623184](tree.assets/image-20210405144623184.png)

---

### 2.3. 수식트리

- 수식을 표현하는 이진트리

- 수식 이진 트리라고 부르기도 함

- 연산자(operator)는 루트 노드이거나 가지 노드

- 피연산자(operand)는 모두 잎 노드

  ![image-20210405144726838](tree.assets/image-20210405144726838.png)

- 중위 순회 : A / B * C * D + E

- 후위 순회 : A B / C * D * E +

- 전위 순회 : + * * / A B C D E

  ![image-20210405144921014](tree.assets/image-20210405144921014.png)

---

## 3. 이진 탐색 트리

![image-20210405150053843](tree.assets/image-20210405150053843.png)

![image-20210405155935422](tree.assets/image-20210405155935422.png)

빠른속도로 추가 삭제가 가능

- 탐색연산

  ![image-20210405160001046](tree.assets/image-20210405160001046.png)

  ![image-20210405160157565](tree.assets/image-20210405160157565.png)

  탐색깊이, 횟수를 줄일 수 있다.

- 삽입연산

  ![image-20210405160308497](tree.assets/image-20210405160308497.png)

  ![image-20210405160316140](tree.assets/image-20210405160316140.png)

- 성능

  ![image-20210405160511219](tree.assets/image-20210405160511219.png)

- 검색 알고리즘의 비교

  ![image-20210405160601829](tree.assets/image-20210405160601829.png)

- 삭제연산

  ![image-20210405160814548](tree.assets/image-20210405160814548.png)

  해당 노드의 자식이 있다면 연결을 끊고 그 자식과 연결

  양쪽에 자식이 있으면?? 그 자리에 있어야하는 애들 찾아서 삽입해줘야함. 9의 경우 9보다 가장가까운애(오른쪽으로가서 가장 가까운 애 왼쪽자식이 없는 최초의 애 이 경우 15)

  고려할 상황이 많아진다.(이거 하고싶으면 연결리스트부터 시작해서 올라와야됨)

---

## 4. 힙(heap)

![image-20210405162211621](tree.assets/image-20210405162211621.png)

![image-20210405152821197](tree.assets/image-20210405152821197.png)

![image-20210405161310761](tree.assets/image-20210405161310761.png)

부모자식간의 관계가 최대힙의 경우 부모가 자식보다 크면되고, 최소힙의 경우 부모가 자식보다 작으면 됩니다.

![image-20210405161419757](tree.assets/image-20210405161419757.png)

- 완전이진트리 x
- 대소비교하면 크고작은게 뒤죽박죽

### 힙 연산 - 삽입

- 힙의 동작

![image-20210405161459106](tree.assets/image-20210405161459106.png)

노드추가해서 완전이진트리를 만들려면

마지막 노드 확장, 거기에 숫자를 삽입.

최대힙 조건은 부모 > 자식이므로 방금 전 삽입한 녀석과 부모 대소비교해서 옳으면 삽입완료, 그렇지 않으면 자리 change

![image-20210405161823947](tree.assets/image-20210405161823947.png)

### 힙 연산 - 삭제

![image-20210405161954338](tree.assets/image-20210405161954338.png)

![image-20210405162034244](tree.assets/image-20210405162034244.png)

- 힙을 이용하여 우선순위 큐 구현 가능

### 연습문제

![image-20210405162347941](tree.assets/image-20210405162347941.png)

```python
def preorder(n):
    if n>0:
        print(n, end=' ')
		preorder(left[n])
        preorder(right[n])

# 1번부터V까지 노드
V, E = map(int, input().split())
edge = list(map(int, input().split()))

left = [0]*(V+1) # 부모를 인덱스로 왼쪽 자식번호 저장
right = [0]*(V+1) # 부모를 인덱스로 오른쪽 자식번호 저장

pa = [0]*(V+1)  # 자식을 인덱스로 부모번호 저장

for i in range(E):
    n1, n2 = edge[i*2], edge[i*2+1] # n1부모 n2 자식노드
    if left[n1] == 0:  # 왼쪽자식이 없으면
        left[n1] = n2  # 부모를 인덱스로 자식번호 저장
    else:  # 왼쪽 자식있으면
        right[n1] = n2  # 부모를 인덱스로 자식번호 저장
        
        pa[n2] = n1 # 자식을 인덱스로 부모를 저장
        
root = 0
for i in range(1, V+1):
    if pa[i] == 0:
        root = i
        break
        
preorder(4)
```







































포화이진트리, 완전이지트리 번호, 저장방식

## 웹엑스시간

### 용어정리

- 트리는 비선형 구조
- 원소들 간에 1:N관계를 가지는 자료구조
- 뒤집어진 나무모양

![image-20210405124201547](tree.assets/image-20210405124201547.png)

- 다대다 n:m => 그래프. 결국 트리도 그래프의 일종

- 큐, 스택과 같은 자료구조중 하나

- 노드 : DATA, 정보, 어떻게 연결되어있는지에 대한 주소

  ![image-20210405124417356](tree.assets/image-20210405124417356.png)

  - 데이터엔 무수히 많은 테이터가 들어가 있고

- 노드하나를 새롭게 루트로 정해서 서브트리로 볼 수 있다.

  ![image-20210405124512088](tree.assets/image-20210405124512088.png)

- 간선 : 노드를 연결하는 선
- 형제노드 : 같은 부모 노드의 자식 노드들
- 서브트리(subtree) : 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- 단말/리프/잎 노드 : 자식이 하나도 없는 노드들
- 차수(degree) : 노드에서 퍼져나간 자식의 수, 그중에서 가장 큰값이 트리의 차수
- 높이=레벨

### 이진트리

- 모든 노드들이 **'최대 2개'**의 서브트리를 갖는 특별한 형태의 트리

- 레벨 i 에서의 노드 최대 개수는 2^i개

- 높의가 h인 이진 트리가 가질 수 있는 노드 개수는 h+1개, 최대개수는 2^h+1-1

- 포화이진트리(Full Binary Tree)

  ![image-20210405125041314](tree.assets/image-20210405125041314.png)

  - 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
  - 높이가 h일 때, 최대의 노드 개수인(2^h+1-1)의 노드를 가진 이진 트리
  - 루트를 1번으로하여 2^h+1-1까지 정해진 위치에 대한 노드 번호를 가짐

  - 왜 1번부터 시작?? 배열에 저장할 때 계산편리를 위해서

    ![image-20210405125212087](tree.assets/image-20210405125212087.png)

    왼쪽자식은 *2, 오른쪽자식은 *2+1을 하면 구할 수 가있다.

    자식이 부모를 구할때는 반대로 하면 되기때문에 계산이 편리해진다.

- 완전 이진트리(Complete Binary Tree)

  ![image-20210405125408024](tree.assets/image-20210405125408024.png)

  - 높이가 h이고 노드 수가 n개일 때(단 h+1 <= n < 2^h+1-1), 포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리

- 편향 이진트리(Skewed Binary Tree)
  
  - 높이 h에 대한 최소 개수의 노드를 가지는 이진 트리

### 순회

각 노드를 중복되지 않게 전부 방문하는 것.

![image-20210405125533529](tree.assets/image-20210405125533529.png)

![image-20210405125650184](tree.assets/image-20210405125650184.png)

V는 방문한자리(Visited)

- 전위(VLR) 순회(preorder traversal)

  현재노드 -> 왼쪽 서브트리 -> 오른쪽 서브트리

  ![image-20210405125843784](tree.assets/image-20210405125843784.png)

  전위순회 예

  ![image-20210405130437960](tree.assets/image-20210405130437960.png)

  A - B - D - E - H - I - C - F - G

- 중위(LVR) 순회(inorder traversal)

  현재 노드의 왼쪽 서브트리 -> 현재 노드 방문 -> 현재 노드의 오른쪽 서브트리

  ![image-20210405130725116](tree.assets/image-20210405130725116.png)

  중위 순회의 예

  ![image-20210405130832589](tree.assets/image-20210405130832589.png)

  D - B - H - E - I - A - F - C - G

- 후위(LRV) 순회

  왼쪽 ->  오른쪽 -> 현재노드

  ![image-20210405131222741](tree.assets/image-20210405131222741.png)

### 이진트리의 표현

- 배열을 이용한 이진 트리의 표현

  ![image-20210405131525803](tree.assets/image-20210405131525803.png)

  - 이진 트리에 각 노드 번호를 위와 같이 부여합니다

- ![image-20210405131646120](tree.assets/image-20210405131646120.png)

  - 내림표시

  ![image-20210405131723561](tree.assets/image-20210405131723561.png)

- 배열로 저장하면 단점이 하나 있습니다

  ![image-20210405131927663](tree.assets/image-20210405131927663.png)

  편향 이진트리의 경우 배열로 저장시 빈 공간을 만들어놔야한다는 단점

  ![image-20210405132003164](tree.assets/image-20210405132003164.png)

  보통 노드의 수가 엄청많을경우에는 배열로 표현할 수가 없기때문에 다른 표현방식을 사용

  ![image-20210405132026163](tree.assets/image-20210405132026163.png)

---

연결리스트를 이용한 트리표현은 연결리스트 안배웠으니까 패스함![image-20210405163523056](tree.assets/image-20210405163523056.png)

### 연습문제

![image-20210405163601410](tree.assets/image-20210405163601410.png)

전위순회, 중위순회, 후위순회 정점 번호 출력

### 트리저장방법

이진트리는 자식이 최대 2개니까 배열을 2개로 만들어 버렸음

![image-20210405163805455](tree.assets/image-20210405163805455.png)

라이브에서는 left, right로 이름 정해줌

![image-20210405163828097](tree.assets/image-20210405163828097.png)

- 부모 노드를 인덱스로 자식 번호를 저장

![image-20210405163739890](tree.assets/image-20210405163739890.png)

- 자식 노드를 인덱스로 부모 번호를 저장

![image-20210405164154186](tree.assets/image-20210405164154186.png)

### 이진탐색트리

Binary Search Tree

중위순회하면 오름차순 가능

- 탐색연산

  ![image-20210405164725676](tree.assets/image-20210405164725676.png)

- 삽입연산

  ![image-20210405164758625](tree.assets/image-20210405164758625.png)

- 성능

  ![image-20210405164906397](tree.assets/image-20210405164906397.png)

  ​	![image-20210405165226562](tree.assets/image-20210405165226562.png)

- 삭제연산

  ![image-20210405165436656](tree.assets/image-20210405165436656.png)

  자식이 없다면 바로 연결을 끊어버리면 됨

  자식이 한개가 있다면 부모와의 연결을 끊고 그 자식과 연결을 이어주면 된다.(여기서는 순서가 중요한데 )

### 힙

heapq라는 라이브러리가 존재하긴 합니다.

![image-20210405170034380](tree.assets/image-20210405170034380.png)

- 삽입

  ![image-20210405170900166](tree.assets/image-20210405170900166.png)

- 삭제

  ![image-20210405171304301](tree.assets/image-20210405171304301.png)

![image-20210406143835683](tree.assets/image-20210406143835683.png)

![image-20210406144151959](tree.assets/image-20210406144151959.png)

![image-20210406172355682](tree.assets/image-20210406172355682.png)















### 정리

트리 자료구조

다대다관계 => 비선형구조

노드에는 데이터, 주소가 들어있다. (일반적으로 연결리스트로 구현했을때)

트리정보 저장, 배열로 저장하는 법, 전위/중위/후위순회하는 법, 리스트로 저장하는 법



## 0406 실습

### 연습문제

![image-20210406091615855](tree.assets/image-20210406091615855.png)

### 1231_중위순회

저장을 어떻게 할 것인지에 대한 문제

### 5176_이진탐색

![image-20210406135602487](tree.assets/image-20210406135602487.png)

### 재귀

![image-20210406162758350](tree.assets/image-20210406162758350.png)

return을 하는 경우와 하지 않는 경우

![image-20210406163841158](tree.assets/image-20210406163841158.png)

## 0408 실습

### subtree(트리기본문제)

> 주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램을 만드시오.

```
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 간선의 개수 E와 N이 주어지고, 다음 줄에 E개의 부모 자식 노드 번호 쌍이 주어진다.
# 노드 번호는 1번부터 E+1번까지 존재한다. 1<=E<=1000, 1<=N<=E+1
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
```

![image-20210408093027646](tree.assets/image-20210408093027646.png)

![image-20210408093808579](tree.assets/image-20210408093808579.png)

![image-20210408094408544](tree.assets/image-20210408094408544.png)

### 이진탐색

- 정웅님코드

![image-20210408101442687](tree.assets/image-20210408101442687.png)

## 노드의합

![image-20210408110635152](tree.assets/image-20210408110635152.png)

![image-20210408111313766](tree.assets/image-20210408111313766.png)

- 국현님 코드

![image-20210408111420081](tree.assets/image-20210408111420081.png)

### 이진힙

![image-20210408113041953](tree.assets/image-20210408113041953.png)

![image-20210408113111756](tree.assets/image-20210408113111756.png)

- 주희님꺼

![image-20210408113315186](tree.assets/image-20210408113315186.png)