/**
 * Main JavaScript for Portfolio Website - Modern Digital Edition
 * For Ajagare Rahul - Python & Django Developer
 * Enhanced with modern animations, interactions, and features
 */

// ==========================================
// Font Awesome Icon Fallback Handler
// ==========================================
(function() {
    const iconFallbacks = {
        'fa-home': 'home',
        'fa-user': 'person',
        'fa-briefcase': 'work',
        'fa-code': 'code',
        'fa-envelope': 'email',
        'fa-phone': 'phone',
        'fa-map-marker-alt': 'location_on',
        'fa-globe': 'public',
        'fa-github': 'code',
        'fa-github-alt': 'code',
        'fa-linkedin': 'work',
        'fa-linkedin-in': 'work',
        'fa-x-twitter': 'alternate_email',
        'fa-twitter': 'send',
        'fa-facebook': 'public',
        'fa-facebook-f': 'public',
        'fa-instagram': 'photo_camera',
        'fa-youtube': 'video',
        'fa-stack-overflow': 'code',
        'fa-medium': 'article',
        'fa-blog': 'article',
        'fa-check-circle': 'check_circle',
        'fa-exclamation-circle': 'error',
        'fa-exclamation-triangle': 'warning',
        'fa-info-circle': 'info',
        'fa-star': 'star',
        'fa-heart': 'favorite',
        'fa-bookmark': 'bookmark',
        'fa-share': 'share',
        'fa-download': 'download',
        'fa-upload': 'upload',
        'fa-search': 'search',
        'fa-filter': 'filter_list',
        'fa-sort': 'sort',
        'fa-calendar': 'calendar_today',
        'fa-calendar-alt': 'calendar_today',
        'fa-calendar-times': 'event',
        'fa-clock': 'schedule',
        'fa-tags': 'local_offer',
        'fa-folder': 'folder',
        'fa-folder-open': 'folder_open',
        'fa-file': 'description',
        'fa-file-alt': 'description',
        'fa-link': 'link',
        'fa-external-link-alt': 'open_in_new',
        'fa-chevron-left': 'chevron_left',
        'fa-chevron-right': 'chevron_right',
        'fa-chevron-up': 'expand_less',
        'fa-chevron-down': 'expand_more',
        'fa-arrow-left': 'arrow_back',
        'fa-arrow-right': 'arrow_forward',
        'fa-arrow-up': 'arrow_upward',
        'fa-arrow-down': 'arrow_downward',
        'fa-refresh': 'refresh',
        'fa-sync': 'sync',
        'fa-sync-alt': 'sync',
        'fa-spinner': 'progress_activity',
        'fa-circle': 'circle',
        'fa-circle-o': 'circle',
        'fa-square': 'square',
        'fa-database': 'database',
        'fa-server': 'dns',
        'fa-cloud': 'cloud',
        'fa-lock': 'lock',
        'fa-unlock': 'lock_open',
        'fa-shield-alt': 'shield',
        'fa-shield': 'shield',
        'fa-comment': 'comment',
        'fa-comments': 'forum',
        'fa-bell': 'notifications',
        'fa-cog': 'settings',
        'fa-cogs': 'settings_suggest',
        'fa-tools': 'build',
        'fa-wrench': 'build',
        'fa-rocket': 'rocket_launch',
        'fa-lightbulb': 'lightbulb',
        'fa-chart-line': 'trending_up',
        'fa-chart-bar': 'bar_chart',
        'fa-chart-area': 'show_chart',
        'fa-users': 'group',
        'fa-user-tie': 'person',
        'fa-graduation-cap': 'school',
        'fa-certificate': 'workspace_premium',
        'fa-trophy': 'emoji_events',
        'fa-award': 'military_tech',
        'fa-python': 'code',
        'fa-js': 'javascript',
        'fa-html5': 'html',
        'fa-css3': 'css',
        'fa-css3-alt': 'css',
        'fa-bootstrap': 'layers',
        'fa-react': 'react',
        'fa-vuejs': 'view_module',
        'fa-angular': 'angular',
        'fa-node-js': 'nodejs',
        'fa-docker': 'docker',
        'fa-git': 'git',
        'fa-git-alt': 'git',
        'fa-linux': 'computer',
        'fa-project-diagram': 'account_tree',
        'fa-folder-open': 'folder_open',
        'fa-eye': 'visibility',
        'fa-eye-slash': 'visibility_off',
        'fa-paper-plane': 'send',
        'fa-tachometer-alt': 'speed',
        'fa-tachometer': 'speed',
        'fa-sign-out-alt': 'logout',
        'fa-sign-in-alt': 'login',
        'fa-id-badge': 'badge',
        'fa-images': 'collections',
        'fa-pen-fancy': 'edit',
        'fa-edit': 'edit',
        'fa-history': 'history',
        'fa-bolt': 'flash_on',
        'fa-plus': 'add',
        'fa-minus': 'remove',
        'fa-times': 'close',
        'fa-times-circle': 'cancel',
        'fa-check': 'check',
        'fa-question-circle': 'help',
        'fa-info': 'info',
        'fa-copyright': 'copyright',
        'fa-registered': 'copyright',
        'fa-lightbulb': 'lightbulb',
        'fa-flask': 'science',
        'fa-flask-vial': 'science',
        'fa-at': 'alternate_email',
    };

    function checkFontAwesome() {
        const testIcon = document.createElement('i');
        testIcon.className = 'fas fa-home';
        testIcon.style.position = 'absolute';
        testIcon.style.visibility = 'hidden';
        testIcon.style.fontSize = '1px';
        document.body.appendChild(testIcon);

        const before = window.getComputedStyle(testIcon, '::before');
        const fontFamily = before.fontFamily || '';
        const content = before.content || '';
        const hasValidContent = content && content !== 'none' && content !== '';

        document.body.removeChild(testIcon);

        if (!hasValidContent || fontFamily.indexOf('Font Awesome') === -1) {
            document.documentElement.classList.add('fa-fallback');
            applyFallbackIcons();
        }
    }

    function applyFallbackIcons() {
        const faIcons = document.querySelectorAll('[class*="fa-"]:not([class*="fab-"]):not(.fa-spinner)');
        faIcons.forEach(icon => {
            const classes = Array.from(icon.classList);
            for (const cls of classes) {
                if (cls.startsWith('fa-') && iconFallbacks[cls]) {
                    const materialIcon = document.createElement('span');
                    materialIcon.className = 'material-icons-outlined fallback-icon';
                    materialIcon.textContent = iconFallbacks[cls];
                    materialIcon.style.fontSize = 'inherit';
                    materialIcon.style.verticalAlign = 'middle';
                    icon.style.display = 'none';
                    icon.parentNode.insertBefore(materialIcon, icon.nextSibling);
                    break;
                }
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', checkFontAwesome);
    } else {
        checkFontAwesome();
    }
})();

// Enhanced icon error handling for dynamic content
function handleIconError(iconElement, iconClass) {
    const fallbacks = iconClass.match(/fa-[a-z0-9-]+/g);
    if (fallbacks && fallbacks.length > 0) {
        const key = fallbacks[0];
        if (iconClass.match(/fab/)) {
            iconElement.className = 'fab ' + key;
        } else {
            iconElement.className = 'fas ' + key;
        }
    }
}

document.addEventListener('DOMContentLoaded', function() {
    // ==========================================
    // Initialize AOS Animation Library
    // ==========================================
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            once: true,
            offset: 100,
            easing: 'ease-out-cubic'
        });
    }
    
    // ==========================================
    // Navbar Scroll Effect
    // ==========================================
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
        
        // Initial check
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        }
    }
    
    // ==========================================
    // Back to Top Button
    // ==========================================
    const backToTopBtn = document.getElementById('backToTop');
    if (backToTopBtn) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 300) {
                backToTopBtn.classList.add('show');
            } else {
                backToTopBtn.classList.remove('show');
            }
        });
        
        backToTopBtn.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
    
    // ==========================================
    // Auto-hide Alerts
    // ==========================================
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
    
    // ==========================================
    // Smooth Scroll for Anchor Links
    // ==========================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // ==========================================
    // Form Validation
    // ==========================================
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
    
    // ==========================================
    // Contact Form AJAX Submission
    // ==========================================
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            
            // Show loading state
            submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Sending...';
            submitBtn.disabled = true;
            
            fetch(this.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    showAlert('success', 'Message sent successfully! I\'ll get back to you soon.');
                    contactForm.reset();
                } else {
                    showAlert('danger', 'Failed to send message. Please try again.');
                }
            })
            .catch(error => {
                showAlert('danger', 'An error occurred. Please try again.');
            })
            .finally(() => {
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            });
        });
    }
    
    // ==========================================
    // Search Functionality
    // ==========================================
    const searchInput = document.getElementById('search-input');
    if (searchInput) {
        searchInput.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase();
            const cards = document.querySelectorAll('.project-card, .blog-card, .skill-card');
            
            cards.forEach(card => {
                const title = card.querySelector('.card-title, h5, .skill-title');
                if (title) {
                    const titleText = title.textContent.toLowerCase();
                    const text = card.querySelector('.card-text');
                    const textText = text ? text.textContent.toLowerCase() : '';
                    
                    if (titleText.includes(searchTerm) || textText.includes(searchTerm)) {
                        card.style.display = '';
                        card.style.opacity = '1';
                    } else {
                        card.style.opacity = '0.3';
                    }
                }
            });
        });
    }
    
    // ==========================================
    // Lazy Loading Images
    // ==========================================
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.removeAttribute('data-src');
                        img.classList.add('loaded');
                    }
                    imageObserver.unobserve(img);
                }
            });
        }, {
            rootMargin: '50px'
        });
        
        document.querySelectorAll('img[data-src]').forEach(img => {
            img.classList.add('lazy-load');
            imageObserver.observe(img);
        });
    }
    
    // ==========================================
    // Counter Animation
    // ==========================================
    const counters = document.querySelectorAll('.counter');
    if (counters.length > 0) {
        const counterObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const counter = entry.target;
                    const target = parseInt(counter.dataset.target);
                    const duration = 2000;
                    const increment = target / (duration / 16);
                    let current = 0;
                    
                    const updateCounter = () => {
                        current += increment;
                        if (current < target) {
                            counter.textContent = Math.ceil(current);
                            requestAnimationFrame(updateCounter);
                        } else {
                            counter.textContent = target;
                        }
                    };
                    
                    updateCounter();
                    counterObserver.unobserve(counter);
                }
            });
        }, {
            threshold: 0.5
        });
        
        counters.forEach(counter => {
            counterObserver.observe(counter);
        });
    }
    
    // ==========================================
    // Progress Bar Animation
    // ==========================================
    const progressBars = document.querySelectorAll('.progress-bar');
    if (progressBars.length > 0) {
        const progressObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const bar = entry.target;
                    const targetWidth = bar.style.width;
                    bar.style.width = '0';
                    setTimeout(() => {
                        bar.style.width = targetWidth;
                    }, 100);
                    progressObserver.unobserve(bar);
                }
            });
        }, {
            threshold: 0.5
        });
        
        progressBars.forEach(bar => {
            progressObserver.observe(bar);
        });
    }
    
    // ==========================================
    // Card Hover Effects
    // ==========================================
    const cards = document.querySelectorAll('.card, .service-card, .skill-card, .project-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = '';
        });
    });
    
    // ==========================================
    // Navbar Active Link Highlight
    // ==========================================
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
    
    // ==========================================
    // Scroll Reveal Animation
    // ==========================================
    const revealElements = document.querySelectorAll('.reveal');
    if (revealElements.length > 0) {
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('revealed');
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });
        
        revealElements.forEach(el => revealObserver.observe(el));
    }
    
    // ==========================================
    // Typing Animation (if applicable)
    // ==========================================
    const typingElements = document.querySelectorAll('.typing-text');
    typingElements.forEach(element => {
        const text = element.textContent;
        element.textContent = '';
        let i = 0;
        
        const typeWriter = () => {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            }
        };
        
        // Start typing when element is in view
        const typingObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    setTimeout(typeWriter, 500);
                    typingObserver.unobserve(element);
                }
            });
        });
        
        typingObserver.observe(element);
    });
    
    // ==========================================
    // Parallax Effect (optional)
    // ==========================================
    const parallaxElements = document.querySelectorAll('[data-parallax]');
    if (parallaxElements.length > 0 && window.matchMedia('(min-width: 992px)').matches) {
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            parallaxElements.forEach(el => {
                const speed = el.dataset.parallax || 0.5;
                el.style.transform = `translateY(${scrolled * speed}px)`;
            });
        });
    }
});

// ==========================================
// Helper: Show Alert
// ==========================================
function showAlert(type, message) {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed top-0 start-50 translate-middle-x mt-5 z-index-9999`;
    alertDiv.setAttribute('role', 'alert');
    alertDiv.innerHTML = `
        <strong>${type === 'success' ? '<i class="fas fa-check-circle me-2"></i>' : '<i class="fas fa-exclamation-circle me-2"></i>'}
        ${message}</strong>
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    document.body.appendChild(alertDiv);
    
    setTimeout(() => {
        alertDiv.remove();
    }, 5000);
}

// ==========================================
// Helper: CSRF Token
// ==========================================
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Set CSRF token for AJAX
const csrfToken = getCookie('csrftoken');
if (csrfToken && typeof $ !== 'undefined') {
    $.ajaxSetup({
        headers: {
            'X-CSRFToken': csrfToken
        }
    });
}

// ==========================================
// Preloader (optional)
// ==========================================
window.addEventListener('load', function() {
    const preloader = document.querySelector('.page-loader');
    if (preloader) {
        preloader.classList.add('fade-out');
        setTimeout(() => {
            preloader.remove();
        }, 500);
    }
});

// ==========================================
// Smooth Page Transitions
// ==========================================
document.querySelectorAll('a:not([href^="#"]):not([href^="mailto"]):not([href^="tel"])').forEach(link => {
    link.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href && !href.startsWith('http') && !href.startsWith('//')) {
            // Add fade-out effect before navigation
            document.body.style.opacity = '0';
            document.body.style.transition = 'opacity 0.3s ease';
        }
    });
});

// ==========================================
// UI Reliability Enhancements
// ==========================================
(function() {
    // Ensure body stays visible after page load
    document.body.style.opacity = '1';
    
    // Handle browser back/forward cache
    window.addEventListener('pageshow', function(event) {
        if (event.persisted) {
            document.body.style.opacity = '1';
        }
    });
    
    // Accessibility: Add skip link for keyboard users
    const skipLink = document.createElement('a');
    skipLink.href = '#main-content';
    skipLink.className = 'skip-link btn btn-primary position-absolute';
    skipLink.style.top = '-40px';
    skipLink.style.left = '0';
    skipLink.style.zIndex = '10000';
    skipLink.textContent = 'Skip to main content';
    skipLink.addEventListener('focus', function() {
        this.style.top = '0';
    });
    skipLink.addEventListener('blur', function() {
        this.style.top = '-40px';
    });
    document.body.insertBefore(skipLink, document.body.firstChild);
    
    // Add id to main content if not present
    const mainContent = document.querySelector('main') || document.querySelector('.main-content');
    if (mainContent && !mainContent.id) {
        mainContent.id = 'main-content';
    }
    
    // Keyboard navigation improvements
    document.addEventListener('keydown', function(e) {
        if (e.key === '/' && e.target.tagName !== 'INPUT' && e.target.tagName !== 'TEXTAREA') {
            e.preventDefault();
            const searchInput = document.querySelector('#search-input, input[type="search"]');
            if (searchInput) {
                searchInput.focus();
            }
        }
    });
    
    // Handle reduced motion preference
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        document.body.classList.add('reduced-motion');
        const style = document.createElement('style');
        style.textContent = `
            *, *::before, *::after {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }
        `;
        document.head.appendChild(style);
    }
    
    // Performance monitoring
    if ('performance' in window) {
        window.addEventListener('load', function() {
            setTimeout(function() {
                const perfData = performance.getEntriesByType('navigation')[0];
                if (perfData && perfData.domContentLoadedEventEnd > 3000) {
                    console.warn('Page load time exceeded 3 seconds');
                }
            }, 0);
        });
    }
})();


