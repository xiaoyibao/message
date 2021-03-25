# encoding: utf-8

'''
@author: leon
@project: Message
@created: 2018/10/15 10:08
@ide: PyCharm 
@url: www.sinosoft.com.cn
@desc: a file named serializers.py in Message
'''
from rest_framework import serializers
from strategy.models import *


# from django.contrib.auth.models import User

class ReceptorSerializer(serializers.HyperlinkedModelSerializer):
    # 这里需要将校验的数据进行返回(估计和django的版本相关)
    def validate(self, data):
        if data['telephone'].__len__() != 11:
            raise serializers.ValidationError({'telephone': '电话号码位数不正确,请核对后填写!'})
        return data
    receptor = serializers.HyperlinkedIdentityField(view_name='receptor-detail')
    # receptor = serializers.HyperlinkedIdentityField(view_name='receptor-detail', read_only=True)

    class Meta:
        model = Receptor
        fields = ('name', 'telephone', 'email', 'create_time', 'receptor')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    group = serializers.HyperlinkedIdentityField(view_name='group-detail')

    class Meta:
        model = Group
        fields = ('group_name', 'create_time', 'corpid', 'corpsecret', 'agentid', 'group')


class RelationSerializer(serializers.HyperlinkedModelSerializer):
    relation = serializers.HyperlinkedIdentityField(view_name='relation-detail')

    class Meta:
        model = Relation
        fields = ('receptor', 'group', 'relation')


class StrategySerializer(serializers.HyperlinkedModelSerializer):
    def validate(self, data):
        strategy_names = Strategy.objects.all().values('strategy_name')

        # if data['strategy_name'].__len__() != 11:
        #     raise serializers.ValidationError({'telephone': '电话号码位数不正确,请核对后填写!'})
        # return data

    strategy = serializers.HyperlinkedIdentityField(view_name='strategy-detail')

    class Meta:
        model = Strategy
        fields = ('strategy_name', 'time_quantum', 'recept_group', 'channel', 'msg', 'create_time', 'strategy')


class LogSerializer(serializers.HyperlinkedModelSerializer):
    log = serializers.HyperlinkedIdentityField(view_name='log-detail')

    class Meta:
        model = Log
        fields = ('log_name', 'log_info', 'strategy', 'log')
