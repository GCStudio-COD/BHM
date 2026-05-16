/**
 * BMH Perumbavoor Modernization - Custom JS
 * Handles interactive gallery expansion and scroll locking logic
 */

document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.gallery-expand-card');
    const wrapper = document.querySelector('.gallery-grid-wrapper');
    const html = document.documentElement;
    const body = document.body;
    let scrollPosition = 0;

    if (cards.length > 0) {
        cards.forEach(card => {
            // Expansion Handler
            card.addEventListener('click', function(e) {
                if (this.classList.contains('expanded')) return;

                // Save scroll position
                scrollPosition = window.pageYOffset;
                
                // Get initial position
                const rect = this.getBoundingClientRect();
                
                // Set initial fixed position matching current relative position
                this.style.top = rect.top + 'px';
                this.style.left = rect.left + 'px';
                this.style.width = rect.width + 'px';
                this.style.height = rect.height + 'px';
                
                // Force layout
                this.offsetHeight;
                
                // Add classes
                this.classList.add('expanded');
                this.closest('.gallery-item-col').classList.add('active-col');
                wrapper.classList.add('active-expansion');
                
                // Transition to full screen
                requestAnimationFrame(() => {
                    this.style.top = '0';
                    this.style.left = '0';
                    this.style.width = '100vw';
                    this.style.height = '100vh';
                    this.style.borderRadius = '0';
                });
                
                // Apply scroll lock after transition starts
                setTimeout(() => {
                    body.style.top = `-${scrollPosition}px`;
                    html.classList.add('no-scroll');
                    body.classList.add('no-scroll');
                }, 600);
            });

            // Close Handler
            const closeBtn = card.querySelector('.close-card');
            if (closeBtn) {
                closeBtn.addEventListener('click', function(e) {
                    e.stopPropagation();
                    
                    // Disable scroll lock first to get accurate coordinates
                    html.classList.remove('no-scroll');
                    body.classList.remove('no-scroll');
                    body.style.top = '';
                    window.scrollTo(0, scrollPosition);
                    
                    // Get return position (from the parent column)
                    const parent = card.closest('.gallery-item-col');
                    const rect = parent.getBoundingClientRect();
                    
                    // Transition back to original position
                    card.style.top = rect.top + 'px';
                    card.style.left = rect.left + 'px';
                    card.style.width = rect.width + 'px';
                    card.style.height = rect.height + 'px';
                    card.style.borderRadius = '24px';
                    
                    // Cleanup after transition
                    setTimeout(() => {
                        card.classList.remove('expanded');
                        parent.classList.remove('active-col');
                        wrapper.classList.remove('active-expansion');
                        card.style.top = '';
                        card.style.left = '';
                        card.style.width = '';
                        card.style.height = '';
                        card.style.borderRadius = '';
                    }, 600);
                });
            }
        });

        // Global Touch Interception
        window.addEventListener('touchmove', function(e) {
            if (html.classList.contains('no-scroll')) {
                e.preventDefault();
            }
        }, { passive: false });

        // Email Obfuscation Recovery
        const obfuscatedEmails = document.querySelectorAll('.email-obfuscated, .email-link-obfuscated');
        obfuscatedEmails.forEach(el => {
            const user = el.getAttribute('data-user');
            const domain = el.getAttribute('data-domain');
            const email = `${user}@${domain}`;
            
            if (el.classList.contains('email-link-obfuscated')) {
                el.href = `mailto:${email}`;
            }
            el.textContent = email;
        });
    }

    // Unified Facilities Swiper Initialization moved from index.html
    $(function() {
        // Initialize BMH Banner Swiper
        if ($(".mySwiper-banner-bmh").length) {
            new Swiper(".mySwiper-banner-bmh", {
                slidesPerView: 1,
                loop: true,
                effect: "slide",
                speed: 1000,
                autoplay: {
                    delay: 5000,
                    disableOnInteraction: false,
                },
            });
        }

        // Initialize Unified Facilities Swiper
        if ($(".mySwiper-facilities").length) {
            new Swiper(".mySwiper-facilities", {
                slidesPerView: 3,
                spaceBetween: 30,
                centeredSlides: false,
                loop: true,
                watchSlidesProgress: true,
                grabCursor: true,
                allowTouchMove: true,
                autoplay: {
                    delay: 4500,
                    disableOnInteraction: false,
                },
                navigation: {
                    nextEl: ".swiper-button-next",
                    prevEl: ".swiper-button-prev",
                },
                scrollbar: {
                    el: ".swiper-scrollbar",
                    draggable: true,
                    hide: false,
                },
                breakpoints: {
                    1024: {
                        slidesPerView: 2.2,
                        spaceBetween: 20,
                    },
                    767: {
                        slidesPerView: 1.2,
                        spaceBetween: 15,
                    }
                }
            });
        }

        // Initialize Bento Mobile Swiper
        if ($(".mySwiper-bento-mobile").length) {
            new Swiper(".mySwiper-bento-mobile", {
                slidesPerView: 2.2,
                spaceBetween: 15,
                centeredSlides: false,
                loop: true,
                autoplay: {
                    delay: 3500,
                    disableOnInteraction: false,
                },
                scrollbar: {
                    el: ".swiper-scrollbar",
                    draggable: true,
                    hide: false,
                },
                breakpoints: {
                    767: {
                        slidesPerView: 1.2,
                    }
                }
            });
        }

        // Initialize Mobile Gallery Swiper
        if ($(".mySwiper-gallery-mobile").length) {
            new Swiper(".mySwiper-gallery-mobile", {
                slidesPerView: 1.2,
                spaceBetween: 20,
                centeredSlides: false,
                loop: true,
                autoplay: {
                    delay: 4000,
                    disableOnInteraction: false,
                },
                scrollbar: {
                    el: ".swiper-scrollbar",
                    draggable: true,
                    hide: false,
                },
            });
        }

        // Initialize Nearby Facilities Swiper
        if ($(".mySwiper-nearby").length) {
            new Swiper(".mySwiper-nearby", {
                slidesPerView: 3,
                spaceBetween: 30,
                loop: true,
                autoplay: {
                    delay: 3000,
                    disableOnInteraction: false,
                },
                pagination: {
                    el: ".swiper-pagination",
                    clickable: true,
                },
                breakpoints: {
                    1024: {
                        slidesPerView: 2.2,
                        spaceBetween: 20,
                    },
                    767: {
                        slidesPerView: 1.2,
                        spaceBetween: 15,
                    }
                }
            });
        }
    });
});
