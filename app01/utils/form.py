from django.forms import ModelChoiceField

from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django import forms
from app01.utils.bootstrap import BootStrapModelForm


class UserModelForm(BootStrapModelForm):
    name = forms.CharField(
        min_length=3,
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    create_time = forms.DateField(
        label="入职时间",
        widget=forms.DateInput(attrs={"class": "form-control date", "type": "date"})
    )

    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", 'gender', 'create_time', "depart"]
        exclude = ["account"]


class PrettyModelForm(BootStrapModelForm):
    # 验证：方式1
    mobile = forms.CharField(
        label="资产名称",
    )

    class Meta:
        model = models.PrettyNum
        fields = [
            "mobile", "level", "price", "status", "pretty_user"
        ]

    def __str__(self):
        return "{0}".format(self.pretty_user.name)

    # 验证：方式2
    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]

        exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("资产名称已存在")

        # 验证通过，用户输入的值返回
        return txt_mobile


class PrettyEditModelForm(BootStrapModelForm):
    # mobile = forms.CharField(disabled=True, label="手机号")
    mobile = forms.CharField(
        label="资产名称",
    )

    class Meta:
        model = models.PrettyNum
        fields = "__all__"

    # 验证：方式2
    def clean_mobile(self):
        # 当前编辑的哪一行的ID
        # print(self.instance.pk)
        txt_mobile = self.cleaned_data["mobile"]
        exists = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("资产名称已存在")

        # 验证通过，用户输入的值返回
        return txt_mobile
