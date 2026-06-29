
    // Mobile Navigation
    const mobileToggle = document.querySelector('.mobile-toggle');
    const nav = document.querySelector('nav ul');

    mobileToggle.addEventListener('click', () => {
      nav.classList.toggle('active');
    });

    // Close mobile nav on link click
    document.querySelectorAll('nav a').forEach(link => {
      link.addEventListener('click', () => {
        nav.classList.remove('active');
      });
    });

    // Smooth Scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
          window.scrollTo({
            top: target.offsetTop - 60,
            behavior: 'smooth'
          });
        }
      });
    });

    // Scroll to Top Button
    const scrollTop = document.querySelector('.scroll-top');
    window.addEventListener('scroll', () => {
      if (window.scrollY > 100) {
        scrollTop.classList.add('active');
      } else {
        scrollTop.classList.remove('active');
      }
    });

    // Fade-in Animation on Scroll
    const observerOptions = {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    }, observerOptions);

    document.querySelectorAll('.fade-in').forEach(el => {
      observer.observe(el);
    });

    // Form Submissions
    document.getElementById('quoteForm').addEventListener('submit', function(e) {
      e.preventDefault();
      const message = document.getElementById('formMessage');
      message.className = 'message success';
      message.style.display = 'block';
      message.textContent = 'Your quote request has been sent successfully. Thank you!';
      this.reset();
      setTimeout(() => {
        message.style.display = 'none';
      }, 5000);
    });

    document.getElementById('contactForm').addEventListener('submit', function(e) {
      e.preventDefault();
      const message = document.getElementById('contactMessage');
      message.className = 'message success';
      message.style.display = 'block';
      message.textContent = 'Your message has been sent successfully. Thank you!';
      this.reset();
      setTimeout(() => {
        message.style.display = 'none';
      }, 5000);
    });
  