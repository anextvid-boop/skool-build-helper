// Custom Cursor Logic
const cursor = document.querySelector('.cursor');
const clickableElements = document.querySelectorAll('a, .btn, button, .feature-card');

// Update cursor position
document.addEventListener('mousemove', (e) => {
  // Use requestAnimationFrame for smoother performance
  requestAnimationFrame(() => {
    if(cursor) {
      cursor.style.left = e.clientX + 'px';
      cursor.style.top = e.clientY + 'px';
    }
  });
});

// Add hover effect classes to cursor
clickableElements.forEach(el => {
  el.addEventListener('mouseenter', () => {
    if(cursor) cursor.classList.add('hovered');
  });
  el.addEventListener('mouseleave', () => {
    if(cursor) cursor.classList.remove('hovered');
  });
});

// Interactive hover effect for glass cards (subtle dynamic lighting)
const glassCards = document.querySelectorAll('.glass-card, .feature-card');

glassCards.forEach(card => {
  card.addEventListener('mousemove', (e) => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    
    // Apply radial gradient that follows the mouse
    const currentBg = getComputedStyle(card).backgroundColor;
    // Extract base rgba from computed style or fallback
    card.style.background = `rgba(30,30,40,0.4) radial-gradient(circle at ${x}px ${y}px, rgba(160,32,255,0.1), transparent 50%)`;
  });
  
  card.addEventListener('mouseleave', () => {
    card.style.background = ''; // reset to CSS defined background
  });
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        
        const targetId = this.getAttribute('href');
        if(targetId === '#') return;
        
        const targetElement = document.querySelector(targetId);
        if(targetElement) {
            targetElement.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Mobile menu logic
const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
const mobileNav = document.querySelector('.mobile-nav');
const mobileNavLinks = document.querySelectorAll('.mobile-nav a');

if (mobileMenuToggle && mobileNav) {
  mobileMenuToggle.addEventListener('click', () => {
    mobileMenuToggle.classList.toggle('active');
    mobileNav.classList.toggle('open');
    // Prevent background scrolling when menu is open
    document.body.style.overflow = mobileNav.classList.contains('open') ? 'hidden' : '';
  });

  mobileNavLinks.forEach(link => {
    link.addEventListener('click', () => {
      mobileMenuToggle.classList.remove('active');
      mobileNav.classList.remove('open');
      document.body.style.overflow = '';
    });
  });
}
