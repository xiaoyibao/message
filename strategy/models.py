from django.db import models

# Create your models here.


class Receptor(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=50)
    # wechat_num = models.CharField(verbose_name='微信号', max_length=50)
    telephone = models.CharField(verbose_name='手机号', max_length=20)
    email = models.EmailField(verbose_name='邮箱', max_length=50)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    extend1 = models.CharField(max_length=1000, verbose_name='扩展字段1', blank=True, null=True)
    extend2 = models.CharField(max_length=1000, verbose_name='扩展字段2', blank=True, null=True)
    extend3 = models.CharField(max_length=1000, verbose_name='扩展字段3', blank=True, null=True)

    class Meta:
        # 定义model在数据库中的表名称
        db_table = "receptor"
        ordering = ['-id']

    def __str__(self):
        return self.name


class Group(models.Model):
    group_name = models.CharField(verbose_name='组名称', max_length=50)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    corpid = models.CharField(verbose_name='企业ID', max_length=100)
    corpsecret = models.CharField(verbose_name='app密钥', max_length=100)
    agentid = models.CharField(verbose_name='agentID', max_length=100)
    extend1 = models.CharField(max_length=1000, verbose_name='扩展字段1', blank=True, null=True)
    extend2 = models.CharField(max_length=1000, verbose_name='扩展字段2', blank=True, null=True)
    extend3 = models.CharField(max_length=1000, verbose_name='扩展字段3', blank=True, null=True)

    class Meta:
        # 定义model在数据库中的表名称
        db_table = "group"
        ordering = ['-id']

    def __str__(self):
        return self.group_name


class Relation(models.Model):
    receptor = models.ForeignKey(Receptor, verbose_name='接收人员外键')
    group = models.ForeignKey(Group, verbose_name='组外键')

    class Meta:
        # 定义model在数据库中的表名称
        db_table = "relation"
        ordering = ['-id']


class Strategy(models.Model):

    strategy_name = models.CharField(verbose_name='策略名称', max_length=50)
    time_quantum = models.CharField(verbose_name='时间段', max_length=50)
    # recept_group = models.CharField(verbose_name='接收组', max_length=50, choices=)
    recept_group = models.ForeignKey(Group, verbose_name='接收组', related_name='group', related_query_name='gruop_name')
    CHANNEL = (
        (1, '微信'),
        (2, '邮箱'),
        (3, '语音'),
        (4, '短信'),
    )

    channel = models.IntegerField(verbose_name='渠道', choices=CHANNEL)
    msg = models.TextField(verbose_name='告知信息')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    extend1 = models.CharField(max_length=1000, verbose_name='扩展字段1', blank=True, null=True)
    extend2 = models.CharField(max_length=1000, verbose_name='扩展字段2', blank=True, null=True)
    extend3 = models.CharField(max_length=1000, verbose_name='扩展字段3', blank=True, null=True)

    class Meta:
        # 定义model在数据库中的表名称
        db_table = "strategy"
        ordering = ['-id']

    def __str__(self):
        return self.strategy_name


# 记录所属策略的消息内容（方便查询历史消息）
class Log(models.Model):
    log_name = models.CharField(verbose_name='日志名称', max_length=100)
    log_info = models.TextField(verbose_name='日志内容', blank=True, null=True)
    strategy = models.ForeignKey(Strategy, verbose_name='策略外键', default=1)
    extend1 = models.CharField(max_length=1000, verbose_name='扩展字段1', blank=True, null=True)
    extend2 = models.CharField(max_length=1000, verbose_name='扩展字段2', blank=True, null=True)
    extend3 = models.CharField(max_length=1000, verbose_name='扩展字段3', blank=True, null=True)

    class Meta:
        # 定义model在数据库中的表名称
        db_table = "log"
        ordering = ['-id']
