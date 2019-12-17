from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Market(models.Model):
    name=models.CharField(max_length=225)
    address=models.CharField(max_length=225)
    start_time=models.CharField(max_length=225)
    end_time=models.CharField(max_length=225)
    description=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # likes : 즐겨찾기
    likes =models.ManyToManyField(
        User, # User 모델과 Market 모델을 M : N 관계로 두겠다.
        through='Like', # Like라는 중개 모델을 통해 M : N 관계를 맺는다.
        through_fields=('market', 'user'), # Like에 market 속성, user 속성을 추가하겠다.
        related_name='likes' # 1 : N  관계에서 market과 연결된 comment를 가져올 때 comment_set으로 가져왔는데, 
                            # related_name을 설정하면 market.like_set이 아니라 market.likes로 market과 연결된 like를 가져올 수 있다.
        )
    
    # 이 객체를 가르키는 말을 title로 정하겠다.
    def __str__(self):
        return self.title
    
    # 몇 개의 like와 연결되어 있는가를 보여준다.
    def like_count(self):
        return self.likes.count() 

class Like(models.Model):
    # Market의 through_fields와 순서가 같아야 한다.
    market = models.ForeignKey(Market, on_delete=models.CASCADE, null=True) # 특정 market이 삭제되면, 그 market의 즐겨찾기 정보 제거
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Menu(models.Model):
    name=models.CharField(max_length=225)
    photo=models.ImageField(upload_to='images/')
    price=models.IntegerField()
    left=models.IntegerField() # 남은 수량
    description=models.CharField(max_length=1000)
    # Market 모델과 관계를 맺어준다. 1:N에서 N의 속성으로 들어간다.
    # on_delete는 관계를 맺고 있는 Market 객체가 삭제되면 관련된 Menu도 삭제시킨다.
    market=models.ForeignKey(Market, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.body

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    market = models.ForeignKey(Market, on_delete=models.CASCADE,null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField()
    Totalprice = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

