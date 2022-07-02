from tabnanny import verbose
from django.db import models

# Create your models here.

# 主食材


class Zscai(models.Model):
    cpmcheng_zscai = models.CharField(max_length=100, verbose_name='菜谱名称')
    scmcheng_zscai = models.CharField(max_length=100, verbose_name='食材名称')
    sczliang_zscai = models.IntegerField(verbose_name='食材重量')

    class Meta:
        verbose_name = '主食材'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.scmcheng_zscai+'-'+self.cpmcheng_zscai

# 佐料


class Zliao(models.Model):
    cpmcheng_zliao = models.CharField(max_length=100, verbose_name='菜谱名称')
    scmcheng_zliao = models.CharField(max_length=100, verbose_name='食材名称')
    sczliang_zliao = models.IntegerField(verbose_name='食材重量')

    class Meta:
        verbose_name = '佐料'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.scmcheng_zliao+'-'+self.cpmcheng_zliao

# 调料


class Tliao(models.Model):
    cpmcheng_tliao = models.CharField(max_length=100, verbose_name='菜谱名称')
    scmcheng_tliao = models.CharField(max_length=100, verbose_name='食材名称')
    sczliang_tliao = models.IntegerField(verbose_name='食材重量')

    class Meta:
        verbose_name = '调料'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.scmcheng_tliao+'-'+self.cpmcheng_tliao
# 准备步骤


class Zbzhou(models.Model):
    cpmcheng_zbzhou = models.CharField(max_length=100, verbose_name='菜谱名称')
    zbzhou_zbzhou = models.TextField(verbose_name='准备步骤')

    class Meta:
        verbose_name = '准备步骤'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cpmcheng_zbzhou
# 炒菜步骤


class Caibzhou(models.Model):
    cpmcheng_caibzhou = models.CharField(max_length=100, verbose_name='菜谱名称')
    sjiedian_caibzhou = models.IntegerField(verbose_name='时间节点')
    hliang_caibzhou = models.IntegerField(verbose_name='火力')
    dzuo_caibzhou = models.TextField(verbose_name='动作')

    class Meta:
        verbose_name = '炒菜步骤'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cpmcheng_caibzhou
# 注意事项


class Zysxiang(models.Model):
    cpmcheng_zysxiang = models.CharField(max_length=100, verbose_name='菜谱名称')
    zysxiang_zysxiang = models.TextField(verbose_name='注意事项')

    class Meta:
        verbose_name = '注意事项'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cpmcheng_zysxiang

# 选中的菜谱
class Xzdcpu(models.Model):
    cpmcheng_xzdcpu = models.CharField(max_length=100, verbose_name='菜谱名称')

    class Meta:
        verbose_name = '选中的菜谱'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cpmcheng_xzdcpu

# 需要编辑的菜谱
class Xybji(models.Model):
    cpmcheng_xybji = models.CharField(max_length=100, verbose_name='菜谱名称')

    class Meta:
        verbose_name = '需要编辑的菜谱'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cpmcheng_xybji