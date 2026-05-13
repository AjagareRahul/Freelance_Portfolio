from rest_framework import serializers
from .models import Project, Gallery, Skill, SiteInfo, SocialLink, Experience, Education, BlogPost, Testimonial, Service, UpcomingProject


class SiteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteInfo
        fields = '__all__'


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    technology_list = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = '__all__'
    
    def get_technology_list(self, obj):
        return obj.get_technology_list()


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    tags_list = serializers.SerializerMethodField()
    
    class Meta:
        model = BlogPost
        fields = '__all__'
    
    def get_tags_list(self, obj):
        return obj.get_tags_list()


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class UpcomingProjectSerializer(serializers.ModelSerializer):
    technology_list = serializers.SerializerMethodField()
    days_until_launch = serializers.SerializerMethodField()
    launch_status_display = serializers.SerializerMethodField()
    
    class Meta:
        model = UpcomingProject
        fields = '__all__'
    
    def get_technology_list(self, obj):
        return obj.get_technology_list()
    
    def get_days_until_launch(self, obj):
        return obj.days_until_launch
    
    def get_launch_status_display(self, obj):
        return obj.launch_status_display