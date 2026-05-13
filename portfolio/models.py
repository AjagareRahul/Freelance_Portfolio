"""
Models for Portfolio Website
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from cloudinary_storage.storage import MediaCloudinaryStorage, RawMediaCloudinaryStorage


class SiteInfo(models.Model):
    """
    Store general site information
    """
    site_name = models.CharField(max_length=100, default="Ajagare Rahul - Python & Django Developer")
    site_title = models.CharField(max_length=200, default="Professional Python & Django Developer")
    site_description = models.TextField(default="Portfolio website of Ajagare Rahul, a Python and Django developer.")
    owner_name = models.CharField(max_length=100, default="Ajagare Rahul")
    email = models.EmailField(default="ajagare.rahul@example.com")
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True, storage='cloudinary_storage.storage.RawMediaCloudinaryStorage')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Site Information'
        verbose_name_plural = 'Site Information'

    def __str__(self):
        return self.site_name


class SocialLink(models.Model):
    """
    Store social media links
    """
    PLATFORM_CHOICES = [
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter'),
        ('x', 'X (Twitter)'),
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('youtube', 'YouTube'),
        ('stackoverflow', 'Stack Overflow'),
        ('medium', 'Medium'),
        ('blog', 'Blog'),
    ]
    
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    icon_class = models.CharField(max_length=50, default='fab fa-github')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'platform']
        verbose_name = 'Social Link'
        verbose_name_plural = 'Social Links'

    def __str__(self):
        return f"{self.get_platform_display()} - {self.url}"


class Skill(models.Model):
    """
    Store technical skills
    """
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('tools', 'Tools & Frameworks'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='backend')
    proficiency = models.IntegerField(default=50, help_text="Percentage proficiency (0-100)")
    icon_class = models.CharField(max_length=50, blank=True, help_text="Font Awesome icon class")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-proficiency', 'name']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name


class Project(models.Model):
    """
    Store portfolio projects
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    project_url = models.URLField(blank=True)
    source_code_url = models.URLField(blank=True)
    technology_used = models.CharField(max_length=500, help_text="Comma separated technologies")
    featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', '-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title
    
    def get_technology_list(self):
        return [tech.strip() for tech in self.technology_used.split(',')]


class Experience(models.Model):
    """
    Store work experience
    """
    company_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date']
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return f"{self.position} at {self.company_name}"


class Education(models.Model):
    """
    Store educational background
    """
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    grade = models.CharField(max_length=50, blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date']
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} - {self.institution}"


class BlogPost(models.Model):
    """
    Store blog posts
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    excerpt = models.CharField(max_length=300)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    category = models.CharField(max_length=100, default='General')
    tags = models.CharField(max_length=300, blank=True, help_text="Comma separated tags")
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title
    
    def get_tags_list(self):
        return [tag.strip() for tag in self.tags.split(',')]


class ContactMessage(models.Model):
    """
    Store contact form messages
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    phone = models.CharField(max_length=20, blank=True)
    is_read = models.BooleanField(default=False)
    is_replied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"{self.name} - {self.subject}"


class VisitorCount(models.Model):
    """
    Track visitor count
    """
    count = models.IntegerField(default=0)
    last_visitor = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Visitor Count'
        verbose_name_plural = 'Visitor Counts'

    def __str__(self):
        return f"Total Visitors: {self.count}"


class UserActivity(models.Model):
    """
    Track user activities
    """
    ACTIVITY_TYPES = [
        ('login', 'Login'),
        ('logout', 'Logout'),
        ('visit', 'Page Visit'),
        ('contact', 'Contact Form Submission'),
        ('register', 'Registration'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    description = models.TextField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'User Activity'
        verbose_name_plural = 'User Activities'

    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"


class Testimonial(models.Model):
    """
    Store client testimonials
    """
    client_name = models.CharField(max_length=100)
    client_title = models.CharField(max_length=100)
    client_company = models.CharField(max_length=100, blank=True)
    client_image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    testimonial = models.TextField()
    rating = models.IntegerField(default=5, help_text="Rating out of 5")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-order', '-created_at']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f"Testimonial by {self.client_name}"


class Service(models.Model):
    """
    Store services offered
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, help_text="Font Awesome icon class")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title


class Gallery(models.Model):
    """
    Store gallery images
    """
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='gallery/', help_text="Upload gallery image")
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return self.title if self.title else f"Gallery Image {self.id}"


class UpcomingProject(models.Model):
    """
    Store upcoming/planned projects to showcase future work
    """
    title = models.CharField(max_length=200, help_text="Title of the upcoming project")
    slug = models.SlugField(unique=True, help_text="URL-friendly slug for the project")
    description = models.TextField(help_text="Brief description of the project")
    short_description = models.CharField(max_length=200, help_text="Short description for cards/tiles")
    expected_launch = models.DateField(null=True, blank=True, help_text="Expected launch date")
    image = models.ImageField(upload_to='upcoming_projects/', blank=True, null=True, help_text="Preview or concept image")
    technologies = models.CharField(max_length=500, blank=True, help_text="Comma-separated list of technologies to be used")
    status = models.CharField(
        max_length=20,
        choices=[
            ('planned', 'Planned'),
            ('in_development', 'In Development'),
            ('testing', 'Testing'),
            ('launching_soon', 'Launching Soon'),
        ],
        default='planned',
        help_text="Current status of the project"
    )
    featured = models.BooleanField(default=False, help_text="Show in featured section on homepage")
    order = models.IntegerField(default=0, help_text="Display order (lower = first)")
    is_active = models.BooleanField(default=True, help_text="Show on website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'expected_launch', '-created_at']
        verbose_name = 'Upcoming Project'
        verbose_name_plural = 'Upcoming Projects'
        indexes = [
            models.Index(fields=['status', 'is_active', 'expected_launch']),
            models.Index(fields=['featured', 'is_active']),
        ]

    def __str__(self):
        status_badge = " 🚀" if self.status == 'launching_soon' else ""
        return f"{self.title}{status_badge}"

    def get_technology_list(self):
        """Parse comma-separated technologies into a list"""
        if not self.technologies:
            return []
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]

    @property
    def days_until_launch(self):
        """Calculate days until expected launch"""
        if not self.expected_launch:
            return None
        from django.utils import timezone
        delta = self.expected_launch - timezone.now().date()
        return delta.days

    @property
    def launch_status_display(self):
        """Get human-readable status with emoji"""
        status_display_map = {
            'planned': '📋 Planned',
            'in_development': '🔧 In Development',
            'testing': '🧪 Testing',
            'launching_soon': '🚀 Launching Soon!',
        }
        days = self.days_until_launch
        status_text = status_display_map.get(self.status, self.get_status_display())
        
        if days is not None and days > 0:
            return f"{status_text} ({days} days to go)"
        elif days is not None and days == 0:
            return f"{status_text} - Launching Today! 🎉"
        elif days is not None and days < 0:
            return f"{status_text} - {abs(days)} days past expected"
        
        return status_text
