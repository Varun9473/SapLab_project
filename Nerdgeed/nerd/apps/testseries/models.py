# from django.db import models
# from apps.test_series.models import User
# from django.db.models.signals import pre_save
# from django.utils.text import slugify
# from apps.core.slugify import unique_slug_generator
# from django.core.validators import MaxValueValidator

# class Type(models.Model):

#     title       = models.CharField(max_length=120, null=True)
#     slug        = models.SlugField(unique=True, null=True, blank=True)
#     status      = models.BooleanField(default=True)
#     created_at  = models.DateTimeField(auto_now_add=True)
#     updated_at  = models.DateTimeField(auto_now=True)


#     # META CLASS
#     class Meta:
#         db_table = 'test_type'
#         verbose_name = 'test_type'
#         verbose_name_plural = 'test_types'

#     def __str__(self):
#         return self.title


# class TypeSection(models.Model):
#     title       = models.CharField(max_length=120, null=True)
#     type        = models.ForeignKey(Type, on_delete=models.CASCADE)
#     slug        = models.SlugField(unique=True, null=True, blank=True)
#     status      = models.BooleanField(default=True)
#     created_at  = models.DateTimeField(auto_now_add=True)
#     updated_at  = models.DateTimeField(auto_now=True)


#     class Meta:
#         db_table = 'test_section'
#         verbose_name = 'test_section'
#         verbose_name_plural = 'test_sections'

#     def __str__(self):
#         return self.title


# class SectionModule(models.Model):

#     title       = models.CharField(max_length=120, null=True)
#     section     = models.ForeignKey(TypeSection, on_delete=models.CASCADE)
#     slug        = models.SlugField(unique=True, null=True, blank=True)
#     status      = models.BooleanField(default=True)
#     created_at  = models.DateTimeField(auto_now_add=True)
#     updated_at  = models.DateTimeField(auto_now=True)


#     class Meta:
#         db_table = 'test_section_module'
#         verbose_name = 'test_section_module'
#         verbose_name_plural = 'test_section_modules'

#     def __str__(self):
#         return self.title


# class Series(models.Model):

#     title       = models.CharField(max_length=120, null=True)
#     slug        = models.SlugField(unique=True, null=True, blank=True)
#     input_ques  = models.PositiveIntegerField(validators=[MaxValueValidator(999999)], null=True)
#     output_ques = models.PositiveIntegerField(validators=[MaxValueValidator(999999)], null=True)
#     plus_point  = models.PositiveIntegerField(validators=[MaxValueValidator(999999)], null=True)
#     minus_point = models.PositiveIntegerField(validators=[MaxValueValidator(999999)], null=True)
#     test_time   = models.PositiveIntegerField(validators=[MaxValueValidator(999999)], null=True)
#     total_marks = models.PositiveIntegerField(validators=[MaxValueValidator(999999)], null=True)
#     section_module = models.ForeignKey(SectionModule, on_delete=models.CASCADE)
#     user        = models.ForeignKey(User, on_delete=models.CASCADE)
#     status      = models.BooleanField(default=True)
#     created_at  = models.DateTimeField(auto_now_add=True)
#     updated_at  = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'tests'
#         verbose_name = 'test'
#         verbose_name_plural = 'tests'

#     def __str__(self):
#         return self.title


# class Question(models.Model):

#     CORRECT_OPTIONS = (
#         ('A', 'A'),
#         ('B', 'B'),
#         ('C', 'C'),
#         ('D', 'D'),
#     )

#     title       = models.TextField(null=True)
#     slug        = models.SlugField(unique=True, null=True, blank=True)
#     option_1    = models.CharField(max_length=250, null=True, db_column='option_1')
#     option_2    = models.CharField(max_length=250, null=True, db_column='option_2')
#     option_3    = models.CharField(max_length=250, null=True, db_column='option_3')
#     option_4    = models.CharField(max_length=250, null=True, db_column='option_4')
#     correct_opt = models.CharField(max_length=1, choices=CORRECT_OPTIONS, db_column='correct_option')
#     explain     = models.BooleanField(default=False, blank=True)
#     solution    = models.TextField(null=True, blank=True)
#     test        = models.ManyToManyField(Series)
#     status      = models.BooleanField(default=True)
#     created_at  = models.DateTimeField(auto_now_add=True)
#     updated_at  = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'test_questions'
#         verbose_name = 'question'
#         verbose_name_plural = 'questions'

#     def __str__(self):
#         return self.title


# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)


# pre_save.connect(pre_save_post_receiver, sender=Type)
# pre_save.connect(pre_save_post_receiver, sender=TypeSection)
# pre_save.connect(pre_save_post_receiver, sender=SectionModule)
# pre_save.connect(pre_save_post_receiver, sender=Series)
# pre_save.connect(pre_save_post_receiver, sender=Question)

# from django.db import models

# # Create your models here.
