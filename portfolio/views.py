"""
Views for Portfolio Website
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.utils import timezone

from .models import (
    Project, Skill, Experience, Education, BlogPost, ContactMessage,
    Testimonial, Service, SocialLink, SiteInfo, VisitorCount, UserActivity, Gallery,
    UpcomingProject
)
from .forms import (
    ContactForm, RegistrationForm, LoginForm, ProjectForm, SkillForm,
    ExperienceForm, EducationForm, BlogPostForm, TestimonialForm,
    ServiceForm, SocialLinkForm
)


# ==================== Public Views ====================

class HomeView(TemplateView):
    """
    Home page view with hero section and overview
    """
    template_name = 'portfolio/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        try:
            context['site_info'] = SiteInfo.objects.first()
        except Exception:
            context['site_info'] = None
        
        try:
            context['featured_projects'] = Project.objects.filter(
                is_published=True, 
                featured=True
            ).order_by('-created_at')[:6]
        except Exception:
            context['featured_projects'] = []
        
        try:
            skills = Skill.objects.filter(is_active=True).order_by('-proficiency')
            context['skills'] = skills
            context['backend_skills'] = skills.filter(category='backend')
            context['frontend_skills'] = skills.filter(category='frontend')
            context['database_skills'] = skills.filter(category='database')
            context['tools_skills'] = skills.filter(category='tools')
        except Exception:
            context['skills'] = Skill.objects.none()
            context['backend_skills'] = Skill.objects.none()
            context['frontend_skills'] = Skill.objects.none()
            context['database_skills'] = Skill.objects.none()
            context['tools_skills'] = Skill.objects.none()
        
        try:
            context['testimonials'] = Testimonial.objects.filter(
                is_active=True
            ).order_by('-order', '-created_at')[:5]
        except Exception:
            context['testimonials'] = []
        
        try:
            context['experiences'] = Experience.objects.order_by('-start_date')[:3]
        except Exception:
            context['experiences'] = []
        
        try:
            context['upcoming_projects'] = UpcomingProject.objects.filter(
                is_active=True
            ).order_by('order', 'expected_launch')[:3]
        except Exception:
            context['upcoming_projects'] = []
        
        return context


class AboutView(TemplateView):
    """
    About page with biography and experience
    """
    template_name = 'portfolio/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        try:
            context['site_info'] = SiteInfo.objects.first()
        except Exception:
            context['site_info'] = None
        
        try:
            context['experiences'] = Experience.objects.order_by('-start_date')
        except Exception:
            context['experiences'] = []
        
        try:
            context['educations'] = Education.objects.order_by('-start_date')
        except Exception:
            context['educations'] = []
        
        return context


class ProjectsView(ListView):
    """
    Portfolio projects listing page
    """
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'
    paginate_by = 9
    
    def get_queryset(self):
        try:
            return Project.objects.filter(
                is_published=True
            ).order_by('-featured', '-created_at')
        except Exception:
            return Project.objects.none()


class ProjectDetailView(DetailView):
    """
    Single project detail page
    """
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'
    
    def get_queryset(self):
        try:
            return Project.objects.filter(is_published=True)
        except Exception:
            return Project.objects.none()
    
    def get_context_data(self, **context):
        context = super().get_context_data(**context)
        try:
            context['related_projects'] = Project.objects.filter(
                is_published=True
            ).exclude(pk=self.object.pk)[:3]
        except Exception:
            context['related_projects'] = Project.objects.none()
        return context


class SkillsView(TemplateView):
    """
    Skills and expertise page
    """
    template_name = 'portfolio/skills.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        try:
            # Get all skills grouped by category
            skills = Skill.objects.filter(is_active=True).order_by('-proficiency')
            context['all_skills'] = skills
            context['backend_skills'] = skills.filter(category='backend')
            context['frontend_skills'] = skills.filter(category='frontend')
            context['database_skills'] = skills.filter(category='database')
            context['tools_skills'] = skills.filter(category='tools')
        except Exception:
            context['all_skills'] = Skill.objects.none()
            context['backend_skills'] = Skill.objects.none()
            context['frontend_skills'] = Skill.objects.none()
            context['database_skills'] = Skill.objects.none()
            context['tools_skills'] = Skill.objects.none()
        
        return context


class BlogView(ListView):
    """
    Blog listing page
    """
    model = BlogPost
    template_name = 'portfolio/blog.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        try:
            return BlogPost.objects.filter(
                is_published=True
            ).order_by('-published_at')
        except Exception:
            return BlogPost.objects.none()


class BlogDetailView(DetailView):
    """
    Single blog post detail page
    """
    model = BlogPost
    template_name = 'portfolio/blog_detail.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        try:
            return BlogPost.objects.filter(is_published=True)
        except Exception:
            return BlogPost.objects.none()
    
    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        try:
            # Increment views
            post.views += 1
            post.save()
        except Exception:
            pass
        return post
    
    def get_context_data(self, **context):
        context = super().get_context_data(**context)
        try:
            context['related_posts'] = BlogPost.objects.filter(
                is_published=True,
                category=self.object.category
            ).exclude(pk=self.object.pk)[:3]
        except Exception:
            context['related_posts'] = BlogPost.objects.none()
        return context


class ContactView(TemplateView):
    """
    Contact page with form
    """
    template_name = 'portfolio/contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(
                    request, 
                    'Thank you for contacting me! I will get back to you soon.',
                    extra_tags='alert-success'
                )
            except Exception:
                messages.error(
                    request, 
                    'Failed to send message. Please try again later.',
                    extra_tags='alert-danger'
                )
            return redirect('portfolio:contact')
        
        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)


class GalleryView(TemplateView):
    """
    Gallery page
    """
    template_name = 'portfolio/gallery.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['gallery_images'] = Gallery.objects.filter(
                is_active=True
            ).order_by('order', '-created_at')
        except Exception:
            context['gallery_images'] = Gallery.objects.none()
        return context


# ==================== Authentication Views ====================

def register_view(request):
    """
    User registration view
    """
    if request.user.is_authenticated:
        return redirect('portfolio:dashboard')
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        try:
            is_valid = form.is_valid()
        except Exception:
            is_valid = False
        
        if is_valid:
            try:
                user = form.save()
                login(request, user)
                messages.success(
                    request, 
                    f'Welcome {user.username}! Your account has been created successfully.',
                    extra_tags='alert-success'
                )
                return redirect('portfolio:dashboard')
            except Exception:
                messages.error(
                    request, 
                    'Registration failed. Please try again.',
                    extra_tags='alert-danger'
                )
        else:
            # Form errors or validation exception
            if not form.errors:
                form.add_error(None, 'Form submission error. Please try again.')
    else:
        form = RegistrationForm()
    
    return render(request, 'portfolio/register.html', {'form': form})


def login_view(request):
    """
    User login view
    """
    if request.user.is_authenticated:
        return redirect('portfolio:dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        try:
            is_valid = form.is_valid()
        except Exception:
            is_valid = False
        
        if is_valid:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                try:
                    login(request, user)
                    
                    # Log activity
                    UserActivity.objects.create(
                        user=user,
                        activity_type='login',
                        description=f'User logged in'
                    )
                except Exception:
                    pass  # Allow login even if activity logging fails
                
                messages.success(
                    request, 
                    f'Welcome back, {username}!',
                    extra_tags='alert-success'
                )
                
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('portfolio:dashboard')
            else:
                messages.error(
                    request, 
                    'Invalid username or password.',
                    extra_tags='alert-danger'
                )
        else:
            if not form.errors:
                form.add_error(None, 'Invalid username or password.')
            messages.error(
                request, 
                'Invalid username or password.',
                extra_tags='alert-danger'
            )
    else:
        form = LoginForm()
    
    return render(request, 'portfolio/login.html', {'form': form})


def logout_view(request):
    """
    User logout view
    """
    if request.user.is_authenticated:
        # Try to log activity, ignore failures
        try:
            UserActivity.objects.create(
                user=request.user,
                activity_type='logout',
                description=f'User logged out'
            )
        except Exception:
            pass
        
        # Logout the user, ignore signal failures
        try:
            logout(request)
        except Exception:
            pass
        
        messages.success(
            request, 
            'You have been logged out successfully.',
            extra_tags='alert-info'
        )
    
    return redirect('portfolio:home')


# ==================== Dashboard Views ====================

@login_required
def dashboard_view(request):
    """
    User dashboard view
    """
    try:
        # Get user's recent activities
        recent_activities = UserActivity.objects.filter(
            user=request.user
        )[:10]
    except Exception:
        recent_activities = []
    
    try:
        # Get statistics
        total_projects = Project.objects.count()
    except Exception:
        total_projects = 0
    
    try:
        published_projects = Project.objects.filter(is_published=True).count()
    except Exception:
        published_projects = 0
    
    try:
        total_skills = Skill.objects.filter(is_active=True).count()
    except Exception:
        total_skills = 0
    
    try:
        total_messages = ContactMessage.objects.count()
    except Exception:
        total_messages = 0
    
    try:
        unread_messages = ContactMessage.objects.filter(is_read=False).count()
    except Exception:
        unread_messages = 0
    
    context = {
        'recent_activities': recent_activities,
        'total_projects': total_projects,
        'published_projects': published_projects,
        'total_skills': total_skills,
        'total_messages': total_messages,
        'unread_messages': unread_messages,
    }
    
    return render(request, 'portfolio/dashboard.html', context)


@login_required
def profile_view(request):
    """
    User profile view - for updating own profile (requires login)
    """
    try:
        site_info = SiteInfo.objects.first()
    except Exception:
        site_info = None
    
    if request.method == 'POST':
        # Update user profile
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        try:
            user.save()
        except Exception:
            pass
        
        # Update site info email as well
        email_value = request.POST.get('email', '')
        if site_info:
            try:
                site_info.email = email_value
                site_info.save()
            except Exception:
                pass
        else:
            try:
                SiteInfo.objects.create(email=email_value)
            except Exception:
                pass
        
        # Handle profile image upload
        if 'profile_image' in request.FILES:
            if site_info:
                try:
                    site_info.profile_image = request.FILES['profile_image']
                    site_info.save()
                except Exception:
                    pass
            else:
                try:
                    SiteInfo.objects.create(profile_image=request.FILES['profile_image'])
                except Exception:
                    pass
        
        # Handle resume upload
        if 'resume' in request.FILES:
            if site_info:
                try:
                    site_info.resume = request.FILES['resume']
                    site_info.save()
                except Exception:
                    pass
            else:
                try:
                    SiteInfo.objects.create(resume=request.FILES['resume'])
                except Exception:
                    pass
        
        messages.success(
            request, 
            'Profile updated successfully!',
            extra_tags='alert-success'
        )
        return redirect('portfolio:profile')
    
    return render(request, 'portfolio/profile.html', {'user': request.user, 'site_info': site_info})


def public_profile_view(request):
    """
    Public profile view - shows portfolio owner's profile to visitors (no login required)
    """
    try:
        site_info = SiteInfo.objects.first()
    except Exception:
        site_info = None
    
    # Get the first superuser as the owner
    try:
        User = get_user_model()
        owner = User.objects.filter(is_superuser=True).first()
    except Exception:
        owner = None
    
    # Get additional details
    try:
        experiences = Experience.objects.order_by('-start_date')
    except Exception:
        experiences = []
    
    try:
        educations = Education.objects.order_by('-start_date')
    except Exception:
        educations = []
    
    try:
        skills = Skill.objects.filter(is_active=True).order_by('-proficiency')
    except Exception:
        skills = Skill.objects.none()
    
    return render(request, 'portfolio/public_profile.html', {
        'site_info': site_info,
        'owner': owner,
        'experiences': experiences,
        'educations': educations,
        'skills': skills,
    })


def download_resume(request):
    """
    Download resume view - serves the resume file for download
    """
    try:
        site_info = SiteInfo.objects.first()
        if site_info and site_info.resume:
            # Try to serve the file - handle Cloudinary storage properly
            try:
                # For Cloudinary storage, we need to fetch the file from the URL
                file_url = site_info.resume.url
                
                # Fetch the file from the URL (works for both local and Cloudinary)
                import requests
                response = requests.get(file_url, stream=True, timeout=10)
                
                if response.status_code == 200:
                    # Create Django response with appropriate headers for download
                    django_response = HttpResponse(
                        response.content,
                        content_type='application/pdf'
                    )
                    # Set filename for download
                    filename = site_info.resume.name.split('/')[-1]  # Get just the filename part
                    if not filename.endswith('.pdf'):
                        filename += '.pdf'
                    django_response['Content-Disposition'] = f'attachment; filename="{filename}"'
                    return django_response
                else:
                    # If fetching fails, fall back to redirecting to the URL
                    return redirect(file_url)
            except Exception as fetch_error:
                # If fetching fails, fall back to redirecting to the URL
                return redirect(site_info.resume.url)
        else:
            messages.error(request, 'Resume not found.')
            return redirect('portfolio:public_profile')
    except Exception as e:
        messages.error(request, f'Error downloading resume: {str(e)}')
        return redirect('portfolio:public_profile')
    except Exception as e:
        messages.error(request, f'Error downloading resume: {str(e)}')
        return redirect('portfolio:public_profile')


@login_required
def messages_view(request):
    """
    View all contact messages
    """
    try:
        messages_list = ContactMessage.objects.order_by('-created_at')
        paginator = Paginator(messages_list, 10)
        page = request.GET.get('page')
        try:
            messages_page = paginator.page(page)
        except PageNotAnInteger:
            messages_page = paginator.page(1)
        except EmptyPage:
            messages_page = paginator.page(paginator.num_pages)
    except Exception:
        # Return empty page with pagination
        paginator = Paginator([], 10)
        messages_page = paginator.page(1)
    
    return render(request, 'portfolio/messages.html', {'messages': messages_page})


@login_required
def mark_message_read(request, pk):
    """
    Mark a contact message as read
    """
    try:
        message = get_object_or_404(ContactMessage, pk=pk)
        message.is_read = True
        message.save()
        messages.success(request, 'Message marked as read.')
    except Exception:
        messages.error(request, 'Failed to update message.')
    return redirect('portfolio:messages')


# ==================== API Views ====================

def api_skills(request):
    """
    API endpoint to get all skills
    """
    try:
        skills = Skill.objects.filter(is_active=True).order_by('-proficiency')
        data = [
            {
                'id': skill.id,
                'name': skill.name,
                'category': skill.category,
                'proficiency': skill.proficiency,
                'icon_class': skill.icon_class,
            }
            for skill in skills
        ]
    except Exception:
        data = []
    return JsonResponse(data, safe=False)


def api_projects(request):
    """
    API endpoint to get all published projects
    """
    try:
        projects = Project.objects.filter(is_published=True).order_by('-created_at')
        data = [
            {
                'id': project.id,
                'title': project.title,
                'slug': project.slug,
                'short_description': project.short_description,
                'image': project.image.url if project.image else None,
                'project_url': project.project_url,
                'source_code_url': project.source_code_url,
                'technology_used': project.get_technology_list(),
            }
            for project in projects
        ]
    except Exception:
        data = []
    return JsonResponse(data, safe=False)


def api_contact(request):
    """
    API endpoint to submit contact form
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
            except Exception:
                return JsonResponse({'success': False, 'errors': {'__all__': ['Database error. Please try again later.']}}, status=500)
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)


def create_admin(request):
    User = get_user_model()
    try:
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@gmail.com',
                password='admin123'
            )
            return HttpResponse("Superuser created successfully ✅")
    except Exception:
        pass
    return HttpResponse("Superuser already exists 👍")

