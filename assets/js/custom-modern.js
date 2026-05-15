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

                // Save scroll position for seamless return
                scrollPosition = window.pageYOffset;
                
                // Reset state
                cards.forEach(c => c.classList.remove('expanded'));
                
                // Add active classes
                this.classList.add('expanded');
                this.closest('.gallery-item-col').classList.add('active-col');
                wrapper.classList.add('active-expansion');
                
                // Apply absolute scroll lock
                body.style.top = `-${scrollPosition}px`;
                html.classList.add('no-scroll');
                body.classList.add('no-scroll');
            });

            // Close Handler
            const closeBtn = card.querySelector('.close-card');
            if (closeBtn) {
                closeBtn.addEventListener('click', function(e) {
                    e.stopPropagation(); // Prevent re-triggering expansion
                    
                    // Remove active classes
                    card.classList.remove('expanded');
                    card.closest('.gallery-item-col').classList.remove('active-col');
                    wrapper.classList.remove('active-expansion');
                    
                    // Disable scroll lock
                    html.classList.remove('no-scroll');
                    body.classList.remove('no-scroll');
                    
                    // Restore original position
                    body.style.top = '';
                    window.scrollTo(0, scrollPosition);
                });
            }
        });

        // Global Touch Interception for iOS/Touch devices during expansion
        window.addEventListener('touchmove', function(e) {
            if (html.classList.contains('no-scroll')) {
                e.preventDefault();
            }
        }, { passive: false });
    }
});
