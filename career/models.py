from django.db import models

# Create your models here.

class ResumePrimary(models.Model):
    account_id = models.PositiveIntegerField(primary_key=True)
    real_name = models.CharField(max_length=24)
    mobile_phone = models.CharField(max_length=32)
    contact_email = models.CharField(max_length=128)
    birthday = models.DateField()
    gender = models.CharField(max_length=1)
    register_location = models.CharField(max_length=128)
    current_location = models.CharField(max_length=128)
    job_title =  models.CharField(max_length=32)

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_resume_primary'


class ResumeWorkExperience(models.Model):
    work_id = models.AutoField(primary_key=True)
    account_id = models.PositiveIntegerField(db_index=True)
    start_time = models.DateField(default=None)
    end_time = models.DateField(default=None)
    company_name = models.CharField(max_length=128)
    job_position = models.CharField(max_length=64)
    description = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_resume_work_experience'

class ResumeEduExperience(models.Model):
    edu_id = models.AutoField(primary_key=True)
    account_id = models.PositiveIntegerField(db_index=True)
    start_time = models.DateField(default=None)
    end_time = models.DateField(default=None)
    colledge_name = models.CharField(max_length=128)
    major = models.CharField(max_length=64)
    degree = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_resume_edu_experience'

class ResumeSupplement(models.Model):
    supplement_id = models.AutoField(primary_key=True)
    account_id = models.PositiveIntegerField(db_index=True)
    seq = models.PositiveIntegerField()
    desc_title = models.CharField(max_length=64)
    desc_content = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_resume_supplement'


class JDPost(models.Model):
    job_id = models.AutoField(primary_key=True)
    account_id = models.PositiveIntegerField(db_index=True)

    title = models.CharField(max_length=64)
    job_position = models.CharField(max_length=64)
    salary =  models.IntegerField(default=-1)
    location = models.CharField(max_length=128)
    company_name =  models.CharField(max_length=64)
    work_years = models.IntegerField()
    job_position_desc = models.TextField()
    job_require_desc = models.TextField()
    deadline = models.DateField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_jd_post'


class JDApplyFeedBack(models.Model):
    job_id = models.BigIntegerField(primary_key=True)
    account_id = models.PositiveIntegerField(db_index=True)
    real_desc_score = models.IntegerField(default=5)
    interviewer_score = models.IntegerField(default=5)
    company_score = models.IntegerField(default=5)
    comment = models.CharField(max_length=128)
    relpy = models.CharField(max_length=128)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tb_jd_apply_feedback'


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=128)
    logo = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    homepage = models.CharField(max_length=128)
    scale = models.IntegerField()
    description = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_company'


class AccountApplyJD(models.Model):
    account_id = models.PositiveIntegerField()
    job_id = models.BigIntegerField()
    status = models.PositiveIntegerField()
    reply = models.CharField(max_length=128)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tb_account_apply_jd'
        unique_together = ("account_id", "job_id") 

class AccountFavoriteJD(models.Model):
    account_id = models.PositiveIntegerField()
    job_id = models.BigIntegerField()
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tb_account_favorite_jd'
        unique_together = ("account_id", "job_id") 











