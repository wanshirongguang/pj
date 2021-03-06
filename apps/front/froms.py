from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Regexp,InputRequired,Length,EqualTo
from apps.front.models import *
from wtforms.validators import ValidationError
from apps.common.memcachedUtil import *
class BaseForm(FlaskForm):
    @property    # 把函数变成了属性来调用
    def err(self):
        return self.errors.popitem()[1][0]

class SendSmsCodeForm(BaseForm):
    telephone = StringField(validators=[Regexp('^1[35786]\d{9}$',message='请输入正确电话号码')])
    def validate_telephone(self,filed):
        r = FrontUser.query.filter(FrontUser.telephone == filed.data).first()
        if r :
            raise ValidationError('手机号已被注册')

class SignupFrom(SendSmsCodeForm):
    username = StringField(validators=[InputRequired(message="必须输入用户名"), Length(min=6, max=20, message="用户名必须是6-20位")])
    password = StringField(validators=[InputRequired(message="必须输入密码"), Length(min=6, max=20, message="密码必须是6-20位")])
    password1 = StringField(validators=[EqualTo('password', message="两次密码必须一致")])
    smscode = StringField(validators=[InputRequired(message="必须输入手机验证码")])
    captchacode = StringField(validators=[InputRequired(message="必须输入图片验证码")])
    def validate_smscode(self,filed):
        # 从缓存中获取到，然后校验
        smscode = getCache(self.telephone.data)
        if not smscode :
            raise ValidationError('请输入正确的手机验证码')
        if smscode.upper() != filed.data :
            raise ValidationError('请输入正确的手机验证码')
    def validate_captchacode(self,filed):
        # 从缓存中获取到，然后校验
        if not getCache(filed.data):
            raise ValidationError('请输入正确的图片验证码')
    def validate_username(self,field):
        u = FrontUser.query.filter(FrontUser.username == field.data).first()
        if u :
            raise ValidationError('用户名已存在')

class SigninFrom(BaseForm):
    telephone = StringField(validators=[Regexp('^1[35786]\d{9}$', message='请输入正确电话号码')])
    password = StringField(validators=[InputRequired(message="必须输入密码"), Length(min=6, max=20, message="密码必须是6-20位")])
    def validate_telephone(self, filed):
        r = FrontUser.query.filter(FrontUser.telephone == filed.data).first()
        if not r:
            raise ValidationError('该账号未被注册')
    def validate_password(self,filed):
        r = FrontUser.query.filter(FrontUser.telephone == self.telephone.data).first()
        if r.checkPwd(filed.data) == False:
            raise ValidationError('密码错误')

class SendCodeForm(BaseForm):
    telephone = StringField(validators=[Regexp('^1[35786]\d{9}$',message='请输入正确电话号码')])
    def validate_telephone(self,filed):
        r = FrontUser.query.filter(FrontUser.telephone == filed.data).first()
        if not r :
            raise ValidationError('手机号未被注册')

class FindpwdFrom(SendCodeForm):
    password = StringField(validators=[InputRequired(message="必须输入密码"), Length(min=6, max=20, message="密码必须是6-20位")])
    password1 = StringField(validators=[EqualTo('password', message="两次密码必须一致")])
    smscode = StringField(validators=[InputRequired(message="必须输入手机验证码")])
    def validate_smscode(self,filed):
        # 从缓存中获取到，然后校验
        smscode = getCache(self.telephone.data)
        print("校验得到的验证码"+smscode)
        if not smscode :
            raise ValidationError('请输入正确的手机验证码')
        if smscode.upper() != filed.data :
            raise ValidationError('验证码错误')
