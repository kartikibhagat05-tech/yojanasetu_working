// YOJANA SETU - INTERACTIVE ENHANCEMENTS
document.addEventListener('DOMContentLoaded', function() {
    
    // === CUSTOM CURSOR ===
    const cursor = document.createElement('div');
    const cursorTrail = document.createElement('div');
    cursor.className = 'custom-cursor';
    cursorTrail.className = 'cursor-trail';
    document.body.appendChild(cursor);
    document.body.appendChild(cursorTrail);
    
    let mouseX = 0, mouseY = 0;
    let trailX = 0, trailY = 0;
    let cursorVisible = true;
    
    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        
        if (!cursorVisible) {
            cursor.style.opacity = '1';
            cursorTrail.style.opacity = '0.6';
            cursorVisible = true;
        }
    });
    
    document.addEventListener('mouseleave', () => {
        cursor.style.opacity = '0';
        cursorTrail.style.opacity = '0';
        cursorVisible = false;
    });
    
    function animateCursor() {
        // Smooth cursor movement
        let cursorX = mouseX;
        let cursorY = mouseY;
        
        cursor.style.left = cursorX + 'px';
        cursor.style.top = cursorY + 'px';
        
        // Trail effect with delay
        trailX += (mouseX - trailX) * 0.1;
        trailY += (mouseY - trailY) * 0.1;
        cursorTrail.style.left = trailX + 'px';
        cursorTrail.style.top = trailY + 'px';
        
        // Interactive elements effect
        const hoverElements = document.querySelectorAll('a, button, .portal-card, .feature-card');
        hoverElements.forEach(el => {
            el.addEventListener('mouseenter', () => {
                cursor.style.transform = 'scale(1.5)';
                cursor.style.borderColor = '#ff0080';
            });
            el.addEventListener('mouseleave', () => {
                cursor.style.transform = 'scale(1)';
                cursor.style.borderColor = 'var(--accent)';
            });
        });
        
        requestAnimationFrame(animateCursor);
    }
    animateCursor();
    
    // === SCROLL ANIMATIONS ===
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
    
    // Observe elements for fade-in
    document.querySelectorAll('.feature-card, .portal-card, .section-title').forEach(el => {
        el.classList.add('fade-in');
        observer.observe(el);
    });
    
    // === TILT EFFECT FOR CARDS ===
    VanillaTilt.init(document.querySelectorAll('.feature-card, .portal-card'), {
        max: 15,
        speed: 400,
        glare: true,
        'max-glare': 0.2,
        scale: 1.05
    });
    
    // === ENHANCED STATE PORTAL SEARCH ===
    const stateSelect = document.getElementById('state-select');
    const resultBox = document.getElementById('result-box');
    const searchBtn = document.querySelector('.footer-search button');
    
    function showPortal() {
        const url = stateSelect.value;
        if (url) {
            resultBox.innerHTML = `
                <strong>✅ Official Portal Found!</strong><br>
                <a href="${url}" target="_blank" class="portal-link">${url}</a>
                <div class="portal-actions">
                    <button onclick="window.open('${url}', '_blank')">Visit Now</button>
                    <button onclick="navigator.clipboard.writeText('${url}')">Copy Link</button>
                </div>
            `;
            resultBox.classList.add('show');
            
            // Add portal-actions styles
            const style = document.createElement('style');
            style.textContent = `
                .portal-actions {
                    display: flex;
                    gap: 10px;
                    margin-top: 10px;
                }
                .portal-actions button {
                    flex: 1;
                    padding: 8px;
                    background: var(--accent);
                    border: none;
                    border-radius: 5px;
                    color: white;
                    cursor: pointer;
                    transition: var(--transition);
                }
                .portal-actions button:hover {
                    background: var(--accent-dark);
                    transform: translateY(-2px);
                }
            `;
            document.head.appendChild(style);
        } else {
            resultBox.innerHTML = '<span style="color: #ff6b6b;">⚠️ Please select a state or union territory.</span>';
            resultBox.classList.add('show');
        }
    }
    
    // Attach event listeners
    if (searchBtn) {
        searchBtn.addEventListener('click', showPortal);
    }
    
    stateSelect.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') showPortal();
    });
    
    // === TYPEWRITER EFFECT FOR HERO TEXT ===
    const heroText = document.querySelector('.hero-content h2');
    const originalText = heroText.textContent;
    heroText.textContent = '';
    
    let i = 0;
    function typeWriter() {
        if (i < originalText.length) {
            heroText.textContent += originalText.charAt(i);
            i++;
            setTimeout(typeWriter, 50);
        }
    }
    
    // Start typing after 1 second
    setTimeout(typeWriter, 1000);
    
    // === PARTICLES BACKGROUND (Simplified) ===
    function createParticles() {
        const heroSection = document.querySelector('.hero');
        for (let i = 0; i < 20; i++) {
            const particle = document.createElement('div');
            particle.style.position = 'absolute';
            particle.style.width = Math.random() * 4 + 2 + 'px';
            particle.style.height = particle.style.width;
            particle.style.background = 'var(--accent)';
            particle.style.borderRadius = '50%';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.top = Math.random() * 100 + '%';
            particle.style.opacity = Math.random() * 0.3 + 0.1;
            particle.style.animation = `float ${Math.random() * 10 + 10}s infinite ease-in-out`;
            heroSection.appendChild(particle);
        }
    }
    createParticles();
    
    // === ADD CSS FOR PARTICLES ===
    const particleStyle = document.createElement('style');
    particleStyle.textContent = `
        @keyframes float {
            0%, 100% { transform: translate(0, 0); }
            50% { transform: translate(${Math.random() * 100 - 50}px, ${Math.random() * 100 - 50}px); }
        }
    `;
    document.head.appendChild(particleStyle);
    
    // === SCROLL PROGRESS INDICATOR ===
    const progressBar = document.createElement('div');
    progressBar.style.position = 'fixed';
    progressBar.style.top = '0';
    progressBar.style.left = '0';
    progressBar.style.height = '3px';
    progressBar.style.background = 'linear-gradient(90deg, var(--accent), #ff0080)';
    progressBar.style.zIndex = '9999';
    progressBar.style.width = '0%';
    progressBar.style.transition = 'width 0.1s';
    document.body.appendChild(progressBar);
    
    window.addEventListener('scroll', () => {
        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        progressBar.style.width = scrolled + '%';
    });
    
    // === HOVER SOUND EFFECT (Optional) ===
    const hoverSound = new Audio('https://assets.mixkit.co/sfx/preview/mixkit-select-click-1109.mp3');
    hoverSound.volume = 0.3;
    
    document.querySelectorAll('.search-btn, .btn-register, .portal-card').forEach(btn => {
        btn.addEventListener('mouseenter', () => {
            hoverSound.currentTime = 0;
            hoverSound.play().catch(() => {});
        });
    });
    
    // === DARK/LIGHT MODE TOGGLE (Bonus Feature) ===
    const modeToggle = document.createElement('button');
    modeToggle.innerHTML = '🌙';
    modeToggle.style.position = 'fixed';
    modeToggle.style.bottom = '100px';
    modeToggle.style.right = '30px';
    modeToggle.style.zIndex = '1000';
    modeToggle.style.background = 'var(--glass-bg)';
    modeToggle.style.border = '1px solid var(--glass-border)';
    modeToggle.style.borderRadius = '50%';
    modeToggle.style.width = '50px';
    modeToggle.style.height = '50px';
    modeToggle.style.fontSize = '20px';
    modeToggle.style.cursor = 'pointer';
    modeToggle.style.transition = 'var(--transition)';
    
    modeToggle.addEventListener('click', () => {
        document.body.classList.toggle('light-mode');
        if (document.body.classList.contains('light-mode')) {
            modeToggle.innerHTML = '☀️';
            document.documentElement.style.setProperty('--primary', '#f8fafc');
            document.documentElement.style.setProperty('--secondary', '#e2e8f0');
            document.documentElement.style.setProperty('--text', '#0f172a');
            document.documentElement.style.setProperty('--text-muted', '#64748b');
        } else {
            modeToggle.innerHTML = '🌙';
            document.documentElement.style.setProperty('--primary', '#0a0e17');
            document.documentElement.style.setProperty('--secondary', '#1a1f35');
            document.documentElement.style.setProperty('--text', '#ffffff');
            document.documentElement.style.setProperty('--text-muted', '#a0aec0');
        }
    });
    
    document.body.appendChild(modeToggle);
    
    // === LOADING ANIMATION ===
    window.addEventListener('load', () => {
        document.body.style.opacity = '0';
        document.body.style.transition = 'opacity 0.5s';
        
        setTimeout(() => {
            document.body.style.opacity = '1';
        }, 100);
    });
});
