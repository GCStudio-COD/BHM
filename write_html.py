<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" type="image/x-icon" href="assets/images/fav.png">
    <title>BMH Perumbavoor - Advanced Healthcare</title>
    <meta name="description" content="World-class healthcare backed by expert doctors, advanced technology, and compassionate care.">
    <link rel="stylesheet" href="assets/css/plugins/plugins.css">
    <link rel="stylesheet" href="assets/css/plugins/magnifying-popup.css">
    <link rel="stylesheet" href="assets/css/vendor/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/style.css">
    <!-- FontAwesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        html { scroll-behavior: smooth; }
        body { font-family: 'Inter', sans-serif; }
        h1, h2, h3, h4, h5, h6 { font-family: 'Outfit', sans-serif; }
        
        /* Floating CTA */
        .floating-cta { position: fixed; bottom: 30px; right: 30px; z-index: 999; display: flex; flex-direction: column; gap: 15px; }
        .floating-cta a { width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 28px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); transition: 0.3s; }
        .floating-cta a:hover { transform: translateY(-5px); color: #fff; }
        .btn-whatsapp { background-color: #25D366; }
        .btn-call { background-color: var(--color-primary); }

        /* Header Overrides */
        .header-one .logo img { max-height: 60px; }
        .header-wrapper-1 { display: flex; justify-content: space-between; align-items: center; padding: 20px 0; }
        .nav-area ul { margin: 0; padding: 0; display: flex; list-style: none; gap: 30px; }
        .nav-area ul li a { color: var(--color-heading-1); font-weight: 500; font-family: 'Outfit', sans-serif; transition: 0.3s; }
        .nav-area ul li a:hover { color: var(--color-primary); }

        /* Section Titles */
        .section-title { text-align: center; margin-bottom: 50px; }
        .section-title span { color: var(--color-primary); font-weight: 600; text-transform: uppercase; letter-spacing: 1px; display: block; margin-bottom: 10px; }
        .section-title h2 { font-size: 40px; font-weight: 700; color: var(--color-heading-1); margin-bottom: 15px; }
        .section-title p { max-width: 600px; margin: 0 auto; }

        /* 1. Hero Banner */
        .hero-banner {
            position: relative;
            padding: 200px 0 150px;
            background: linear-gradient(rgba(10, 74, 142, 0.8), rgba(0, 168, 204, 0.6)), url('assets/images/banner/bg-1.jpg') center/cover;
            color: #fff;
        }
        .hero-banner h1 { color: #fff; font-size: 64px; font-weight: 700; margin-bottom: 20px; line-height: 1.2; }
        .hero-banner p { color: #fff; font-size: 22px; margin-bottom: 40px; max-width: 600px; }
        .hero-buttons { display: flex; gap: 20px; }
        .btn-white { background: #fff; color: var(--color-primary); font-weight: 600; padding: 15px 30px; border-radius: var(--radius); transition: 0.3s; display: inline-flex; align-items: center;}
        .btn-white:hover { background: var(--color-success); color: #fff; }

        /* 2. Overview */
        .overview-img { border-radius: var(--radius); box-shadow: 0 20px 40px rgba(0,0,0,0.1); width: 100%; }
        .stats-wrapper { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 30px; }
        .stat-card { background: #f8f9fa; padding: 20px; border-radius: var(--radius); text-align: center; transition: 0.3s; }
        .stat-card:hover { background: var(--color-primary); }
        .stat-card h4 { font-size: 32px; color: var(--color-primary); margin-bottom: 5px; transition: 0.3s; }
        .stat-card:hover h4, .stat-card:hover p { color: #fff; }

        /* 3. Facilities */
        .facility-card { text-align: center; padding: 40px 20px; background: #fff; border-radius: var(--radius); box-shadow: 0 5px 20px rgba(0,0,0,0.05); transition: 0.3s; height: 100%; }
        .facility-card:hover { transform: translateY(-10px); background: var(--color-primary); }
        .facility-card:hover h4, .facility-card:hover p { color: #fff; }
        .facility-card i { font-size: 50px; color: var(--color-primary); margin-bottom: 20px; transition: 0.3s; }
        .facility-card:hover i { color: #fff; }

        /* 4. Specialities */
        .speciality-card { background: #fff; border-radius: var(--radius); overflow: hidden; box-shadow: 0 5px 20px rgba(0,0,0,0.05); transition: 0.3s; height: 100%; }
        .speciality-card img { width: 100%; height: 200px; object-fit: cover; }
        .speciality-card .content { padding: 25px; }
        .speciality-card:hover { transform: translateY(-10px); border-bottom: 4px solid var(--color-primary); }

        /* 5. Doctors Joining */
        .dr-joining { background: linear-gradient(to right, rgba(10, 74, 142, 0.9), rgba(0, 168, 204, 0.8)), url('assets/images/about/03.webp') center/cover fixed; padding: 100px 0; border-radius: var(--radius); margin: 60px 0; text-align: center; color: #fff; }
        .dr-joining h2, .dr-joining p { color: #fff; }

        /* 6. Gallery */
        .masonry-gallery { column-count: 3; column-gap: 20px; }
        .masonry-gallery img { width: 100%; border-radius: var(--radius); margin-bottom: 20px; transition: 0.3s; cursor: pointer; }
        .masonry-gallery img:hover { transform: scale(1.02); box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
        @media(max-width: 991px){ .masonry-gallery { column-count: 2; } }
        @media(max-width: 575px){ .masonry-gallery { column-count: 1; } }

        /* 7. Events */
        .event-card { background: #fff; border-radius: var(--radius); box-shadow: 0 5px 20px rgba(0,0,0,0.05); overflow: hidden; height: 100%; transition: 0.3s; }
        .event-card:hover { transform: translateY(-5px); }
        .event-card .date { background: var(--color-primary); color: #fff; padding: 10px 20px; display: inline-block; font-weight: 600; border-bottom-right-radius: var(--radius); }
        .event-card .content { padding: 20px; }

        /* 8. Environmental */
        .env-card { background: #f8f9fa; padding: 30px; border-radius: var(--radius); border-left: 5px solid var(--color-success); height: 100%; transition: 0.3s; }
        .env-card:hover { box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
        .env-card i { font-size: 40px; color: var(--color-success); margin-bottom: 15px; }

        /* 9. Nearby Attractions */
        .nearby-card { display: flex; align-items: center; gap: 15px; padding: 15px; background: #fff; border-radius: var(--radius); margin-bottom: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); }
        .nearby-card i { font-size: 24px; color: var(--color-primary); width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; background: #e2e8f0; border-radius: 50%; }

        /* 10. Leadership */
        .leadership-card { text-align: center; }
        .leadership-card img { width: 220px; height: 220px; border-radius: 50%; object-fit: cover; margin-bottom: 20px; border: 5px solid #fff; box-shadow: 0 10px 30px rgba(0,0,0,0.1); transition: 0.3s; }
        .leadership-card:hover img { transform: scale(1.05); border-color: var(--color-primary); }

        /* 11. Map & Reach */
        .map-container iframe { width: 100%; height: 400px; border-radius: var(--radius); border: none; }

        /* 12. Enquiry Form */
        .enquiry-form { background: #fff; padding: 40px; border-radius: var(--radius); box-shadow: 0 20px 50px rgba(0,0,0,0.1); }
        .enquiry-form .form-control { border-radius: 8px; padding: 12px 20px; margin-bottom: 20px; border: 1px solid var(--color-border); }

        /* Footer */
        .footer-area { background: var(--color-heading-1); color: #fff; padding: 80px 0 20px; }
        .footer-area h5 { color: #fff; margin-bottom: 30px; font-weight: 600; }
        .footer-area ul { list-style: none; padding: 0; }
        .footer-area ul li { margin-bottom: 15px; }
        .footer-area ul li a { color: #a0aec0; transition: 0.3s; text-decoration: none;}
        .footer-area ul li a:hover { color: var(--color-primary); padding-left: 5px; }
        .footer-bottom { border-top: 1px solid rgba(255,255,255,0.1); padding-top: 20px; margin-top: 40px; text-align: center; color: #a0aec0; }
    </style>
</head>
<body>

    <!-- Floating CTAs -->
    <div class="floating-cta">
        <a href="https://wa.me/1234567890" class="btn-whatsapp" title="WhatsApp Us"><i class="fa-brands fa-whatsapp"></i></a>
        <a href="tel:1234567890" class="btn-call" title="Call Emergency"><i class="fa-solid fa-phone"></i></a>
    </div>

    <!-- Header -->
    <header class="header-one header--sticky">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="header-wrapper-1">
                        <div class="logo-area-start">
                            <a href="index.html" class="logo" style="text-decoration: none;">
                                <h3 class="m-0" style="color: var(--color-primary); font-weight: 800;">BMH <span style="color: var(--color-secondary);">Perumbavoor</span></h3>
                            </a>
                        </div>
                        <div class="nav-area d-none d-lg-block">
                            <ul>
                                <li><a href="#hero">Home</a></li>
                                <li><a href="#overview">Overview</a></li>
                                <li><a href="#facilities">Facilities</a></li>
                                <li><a href="#specialities">Specialities</a></li>
                                <li><a href="#gallery">Gallery</a></li>
                            </ul>
                        </div>
                        <div class="header-right">
                            <a href="#enquiry" class="rts-btn btn-primary d-none d-md-inline-flex">Book Appointment</a>
                            <div class="menu-btn d-lg-none" id="menu-btn">
                                <svg width="20" height="16" viewBox="0 0 20 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <rect y="14" width="20" height="2" fill="#1F1F25"></rect>
                                    <rect y="7" width="20" height="2" fill="#1F1F25"></rect>
                                    <rect width="20" height="2" fill="#1F1F25"></rect>
                                </svg>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <!-- 1. Hero Section -->
    <section id="hero" class="hero-banner">
        <div class="container">
            <div class="row">
                <div class="col-lg-8">
                    <h1>Advanced Healthcare for Perumbavoor</h1>
                    <p>World-class healthcare backed by expert doctors, advanced technology, and compassionate care.</p>
                    <div class="hero-buttons">
                        <a href="#enquiry" class="btn-white">Book Appointment</a>
                        <a href="tel:1234567890" class="rts-btn btn-primary" style="background: var(--color-danger); border-color: var(--color-danger);">Emergency Contact</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 2. Overview Section -->
    <section id="overview" class="rts-section-gap">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6 mb-5 mb-lg-0">
                    <img src="assets/images/about/01.webp" alt="BMH Overview" class="overview-img">
                </div>
                <div class="col-lg-6 pl-lg-5">
                    <div class="section-title text-start mb-4">
                        <span>About Hospital</span>
                        <h2>Trusted Healthcare with Compassion & Precision</h2>
                    </div>
                    <p>BMH Perumbavoor is dedicated to providing world-class medical care to patients. Our mission is to enhance and protect your health through advanced treatments, compassionate service, and a commitment to excellence. We are NABH accredited, ensuring the highest quality standards in healthcare.</p>
                    
                    <div class="stats-wrapper">
                        <div class="stat-card">
                            <h4>250+</h4>
                            <p>Hospital Beds</p>
                        </div>
                        <div class="stat-card">
                            <h4>24/7</h4>
                            <p>Emergency Care</p>
                        </div>
                        <div class="stat-card">
                            <h4>40+</h4>
                            <p>Expert Specialists</p>
                        </div>
                        <div class="stat-card">
                            <h4>15+</h4>
                            <p>Departments</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 3. Facilities -->
    <section id="facilities" class="rts-section-gap bg-light">
        <div class="container">
            <div class="section-title">
                <span>Infrastructure</span>
                <h2>Advanced Facilities & Technology</h2>
                <p>Equipped with state-of-the-art medical technology to provide comprehensive patient care.</p>
            </div>
            <div class="row g-4">
                <div class="col-lg-3 col-md-6"><div class="facility-card"><i class="fa-solid fa-heart-pulse"></i><h4>ICU</h4><p>Advanced critical care</p></div></div>
                <div class="col-lg-3 col-md-6"><div class="facility-card"><i class="fa-solid fa-baby-carriage"></i><h4>NICU</h4><p>Neonatal intensive care</p></div></div>
                <div class="col-lg-3 col-md-6"><div class="facility-card"><i class="fa-solid fa-bed-pulse"></i><h4>Modular OT</h4><p>Infection-free surgeries</p></div></div>
                <div class="col-lg-3 col-md-6"><div class="facility-card"><i class="fa-solid fa-x-ray"></i><h4>Cath Lab</h4><p>Cardiac interventions</p></div></div>
                <div class="col-lg-3 col-md-6"><div class="facility-card"><i class="fa-solid fa-pills"></i><h4>Pharmacy</h4><p>24/7 medicine access</p></div></div>
                <div class="col-lg-3 col-md-6"><div class="facility-card"><i class="fa-solid fa-microscope"></i><h4>Laboratory</h4><p>Accurate diagnostics</p></div></div>
                <div class="col-lg-3 col-md-6"><div class="facility-card"><i class="fa-solid fa-truck-medical"></i><h4>Ambulance</h4><p>Emergency transport</p></div></div>
                <div class="col-lg-3 col-md-6"><div class="facility-card"><i class="fa-solid fa-droplet"></i><h4>Dialysis Unit</h4><p>Advanced renal care</p></div></div>
            </div>
        </div>
    </section>

    <!-- 4. Specialities -->
    <section id="specialities" class="rts-section-gap">
        <div class="container">
            <div class="section-title">
                <span>Departments</span>
                <h2>Our Centres of Excellence</h2>
            </div>
            <div class="row g-4">
                <div class="col-lg-4 col-md-6">
                    <div class="speciality-card">
                        <img src="assets/images/service/15.webp" alt="Cardiology">
                        <div class="content">
                            <h4>Cardiology</h4>
                            <p>Comprehensive heart care including angiography and angioplasty.</p>
                            <a href="#enquiry" class="rts-btn btn-primary btn-sm mt-3">Consult Doctor</a>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6">
                    <div class="speciality-card">
                        <img src="assets/images/service/08.webp" alt="Orthopaedics">
                        <div class="content">
                            <h4>Orthopaedics</h4>
                            <p>Advanced joint replacements, sports medicine, and trauma care.</p>
                            <a href="#enquiry" class="rts-btn btn-primary btn-sm mt-3">Consult Doctor</a>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6">
                    <div class="speciality-card">
                        <img src="assets/images/service/09.webp" alt="Neurology">
                        <div class="content">
                            <h4>Neurology</h4>
                            <p>Expert care for stroke, epilepsy, and nervous system disorders.</p>
                            <a href="#enquiry" class="rts-btn btn-primary btn-sm mt-3">Consult Doctor</a>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6">
                    <div class="speciality-card">
                        <img src="assets/images/service/10.webp" alt="Oncology">
                        <div class="content">
                            <h4>Oncology</h4>
                            <p>Comprehensive cancer care with advanced treatment options.</p>
                            <a href="#enquiry" class="rts-btn btn-primary btn-sm mt-3">Consult Doctor</a>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6">
                    <div class="speciality-card">
                        <img src="assets/images/service/11.webp" alt="Gynaecology">
                        <div class="content">
                            <h4>Gynaecology</h4>
                            <p>Women's health, maternity care, and minimally invasive surgeries.</p>
                            <a href="#enquiry" class="rts-btn btn-primary btn-sm mt-3">Consult Doctor</a>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6">
                    <div class="speciality-card">
                        <img src="assets/images/service/12.webp" alt="Paediatrics">
                        <div class="content">
                            <h4>Paediatrics</h4>
                            <p>Dedicated childcare from newborns to adolescents.</p>
                            <a href="#enquiry" class="rts-btn btn-primary btn-sm mt-3">Consult Doctor</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 5. Doctors Joining Section -->
    <div class="container">
        <section class="dr-joining">
            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <h2>Join the BMH Medical Team</h2>
                    <p class="mb-4 text-white">We are looking for passionate and experienced medical professionals to join our growing hospital. Build your career with state-of-the-art infrastructure and a supportive environment.</p>
                    <a href="#contact" class="rts-btn btn-primary" style="background: var(--color-success); border-color: var(--color-success);">Upload Your CV</a>
                </div>
            </div>
        </section>
    </div>

    <!-- 6. Gallery -->
    <section id="gallery" class="rts-section-gap bg-light">
        <div class="container">
            <div class="section-title">
                <span>Visual Tour</span>
                <h2>Hospital Gallery</h2>
            </div>
            <div class="masonry-gallery">
                <img src="assets/images/portfolio/01.jpg" alt="Gallery">
                <img src="assets/images/portfolio/02.jpg" alt="Gallery">
                <img src="assets/images/portfolio/03.jpg" alt="Gallery">
                <img src="assets/images/portfolio/04.jpg" alt="Gallery">
                <img src="assets/images/portfolio/05.jpg" alt="Gallery">
                <img src="assets/images/portfolio/06.jpg" alt="Gallery">
            </div>
        </div>
    </section>

    <!-- 7. Events -->
    <section class="rts-section-gap">
        <div class="container">
            <div class="section-title">
                <span>Community Updates</span>
                <h2>Latest Events & Programs</h2>
            </div>
            <div class="row g-4">
                <div class="col-lg-4">
                    <div class="event-card">
                        <span class="date">15 May 2026</span>
                        <div class="content">
                            <h4>Free Cardiac Camp</h4>
                            <p>Free ECG and cardiology consultation for senior citizens at BMH Perumbavoor.</p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="event-card">
                        <span class="date">02 Jun 2026</span>
                        <div class="content">
                            <h4>Blood Donation Drive</h4>
                            <p>Join us in saving lives. Blood donation camp organized in association with Rotary Club.</p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="event-card">
                        <span class="date">20 Jun 2026</span>
                        <div class="content">
                            <h4>Diabetes Awareness</h4>
                            <p>A comprehensive awareness seminar on diabetes management and healthy lifestyle.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 8. Environmental Assessment -->
    <section class="rts-section-gap bg-light">
        <div class="container">
            <div class="section-title">
                <span>Sustainability</span>
                <h2>Environmental Assessment</h2>
                <p>We are committed to responsible healthcare practices and sustainable growth.</p>
            </div>
            <div class="row g-4">
                <div class="col-md-4">
                    <div class="env-card">
                        <i class="fa-solid fa-leaf"></i>
                        <h4>Biomedical Waste Mgt</h4>
                        <p>Strict adherence to pollution control board guidelines for safe disposal.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="env-card">
                        <i class="fa-solid fa-solar-panel"></i>
                        <h4>Energy Efficiency</h4>
                        <p>Solar-powered water heating and LED lighting across the hospital.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="env-card">
                        <i class="fa-solid fa-water"></i>
                        <h4>Water Management</h4>
                        <p>Advanced STP (Sewage Treatment Plant) and rainwater harvesting.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 10. Leadership Team -->
    <section class="rts-section-gap">
        <div class="container">
            <div class="section-title">
                <span>Leadership</span>
                <h2>Our Guiding Pillars</h2>
            </div>
            <div class="row g-5 justify-content-center">
                <div class="col-lg-4 col-md-6">
                    <div class="leadership-card">
                        <img src="assets/images/team/01.jpg" alt="Chairman">
                        <h4>Dr. John Doe</h4>
                        <p class="text-primary font-weight-bold" style="color: var(--color-primary);">Chairman</p>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6">
                    <div class="leadership-card">
                        <img src="assets/images/team/02.jpg" alt="Managing Director">
                        <h4>Dr. Jane Smith</h4>
                        <p class="text-primary font-weight-bold" style="color: var(--color-primary);">Managing Director</p>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6">
                    <div class="leadership-card">
                        <img src="assets/images/team/03.jpg" alt="Medical Director">
                        <h4>Dr. Robert Wilson</h4>
                        <p class="text-primary font-weight-bold" style="color: var(--color-primary);">Medical Director</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 9 & 11. Nearby Attractions & How to Reach -->
    <section class="rts-section-gap bg-light">
        <div class="container">
            <div class="row">
                <div class="col-lg-5 pr-lg-5">
                    <div class="section-title text-start">
                        <span>Location</span>
                        <h2>How to Reach Us</h2>
                    </div>
                    <p class="mb-4">BMH Perumbavoor is centrally located and easily accessible by road.</p>
                    
                    <h5 class="mt-4 mb-3">Nearby Access</h5>
                    <div class="nearby-card">
                        <i class="fa-solid fa-bus"></i>
                        <div><strong>Perumbavoor Bus Stand</strong><br>1.5 km (5 mins)</div>
                    </div>
                    <div class="nearby-card">
                        <i class="fa-solid fa-train"></i>
                        <div><strong>Aluva Railway Station</strong><br>18 km (30 mins)</div>
                    </div>
                    <div class="nearby-card">
                        <i class="fa-solid fa-plane"></i>
                        <div><strong>Cochin International Airport</strong><br>16 km (25 mins)</div>
                    </div>
                    <div class="nearby-card">
                        <i class="fa-solid fa-bed"></i>
                        <div><strong>Hotels & Lodging</strong><br>Multiple options within 2 km radius</div>
                    </div>
                    
                    <a href="https://maps.google.com" target="_blank" class="rts-btn btn-primary mt-3"><i class="fa-solid fa-location-arrow me-2"></i> Get Directions</a>
                </div>
                <div class="col-lg-7 mt-5 mt-lg-0">
                    <div class="map-container">
                        <!-- Placeholder generic perumbavoor map -->
                        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d62854.73507026362!2d76.4357288636873!3d10.113271109033333!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3b07e2c91836ebed%3A0x892a0bd83196edc6!2sPerumbavoor%2C%20Kerala!5e0!3m2!1sen!2sin!4v1715760000000!5m2!1sen!2sin" allowfullscreen="" loading="lazy"></iframe>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 12. Enquiry CTA Form -->
    <section id="enquiry" class="rts-section-gap">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-lg-6 mb-5 mb-lg-0">
                    <div class="section-title text-start">
                        <span>Appointment</span>
                        <h2>Need Expert Medical Guidance?</h2>
                        <p>Book your consultation today. Fill out the form and our team will get back to you shortly.</p>
                    </div>
                    <img src="assets/images/appoinment/01.webp" alt="Appointment" style="border-radius: var(--radius); width: 100%;">
                </div>
                <div class="col-lg-6 pl-lg-5">
                    <div class="enquiry-form" style="border: 1px solid var(--color-border);">
                        <h4 class="mb-4">Book Your Consultation</h4>
                        <form action="#">
                            <div class="row">
                                <div class="col-md-6">
                                    <input type="text" class="form-control" placeholder="Full Name" required>
                                </div>
                                <div class="col-md-6">
                                    <input type="text" class="form-control" placeholder="Phone Number" required>
                                </div>
                                <div class="col-md-12">
                                    <select class="form-control" required style="height: 50px;">
                                        <option value="" disabled selected>Select Department</option>
                                        <option value="cardiology">Cardiology</option>
                                        <option value="orthopaedics">Orthopaedics</option>
                                        <option value="neurology">Neurology</option>
                                        <option value="other">Other</option>
                                    </select>
                                </div>
                                <div class="col-md-12">
                                    <input type="date" class="form-control" required style="height: 50px;">
                                </div>
                                <div class="col-md-12">
                                    <textarea class="form-control" rows="4" placeholder="Your Message / Symptoms"></textarea>
                                </div>
                                <div class="col-md-12">
                                    <button type="submit" class="rts-btn btn-primary w-100" style="padding: 15px; border:none; border-radius: var(--radius); width: 100%;">Submit Request</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer-area">
        <div class="container">
            <div class="row g-4">
                <div class="col-lg-4 col-md-6">
                    <h3 style="color: #fff; font-weight: 800;">BMH <span style="color: var(--color-secondary);">Perumbavoor</span></h3>
                    <p class="mt-3 text-light" style="opacity: 0.8;">World-class healthcare backed by expert doctors, advanced technology, and compassionate care.</p>
                    <div class="mt-4">
                        <a href="#" class="me-3 text-light fs-4"><i class="fa-brands fa-facebook"></i></a>
                        <a href="#" class="me-3 text-light fs-4"><i class="fa-brands fa-instagram"></i></a>
                        <a href="#" class="me-3 text-light fs-4"><i class="fa-brands fa-twitter"></i></a>
                    </div>
                </div>
                <div class="col-lg-2 col-md-6">
                    <h5>Quick Links</h5>
                    <ul>
                        <li><a href="#overview">About Us</a></li>
                        <li><a href="#specialities">Specialities</a></li>
                        <li><a href="#gallery">Gallery</a></li>
                        <li><a href="#">Careers</a></li>
                        <li><a href="#">Privacy Policy</a></li>
                    </ul>
                </div>
                <div class="col-lg-3 col-md-6">
                    <h5>Key Departments</h5>
                    <ul>
                        <li><a href="#">Cardiology</a></li>
                        <li><a href="#">Orthopaedics</a></li>
                        <li><a href="#">Neurology</a></li>
                        <li><a href="#">Oncology</a></li>
                        <li><a href="#">Paediatrics</a></li>
                    </ul>
                </div>
                <div class="col-lg-3 col-md-6">
                    <h5>Contact Info</h5>
                    <ul style="color: #a0aec0;">
                        <li class="d-flex mb-3"><i class="fa-solid fa-location-dot mt-1 me-3 text-primary"></i> <div>Main Road, Perumbavoor,<br>Kerala - 683542</div></li>
                        <li class="d-flex mb-3"><i class="fa-solid fa-phone mt-1 me-3 text-primary"></i> <div>+91 12345 67890<br>(Emergency 24x7)</div></li>
                        <li class="d-flex"><i class="fa-solid fa-envelope mt-1 me-3 text-primary"></i> <div>info@bmhperumbavoor.com</div></li>
                    </ul>
                </div>
            </div>
            <div class="row">
                <div class="col-12 footer-bottom">
                    <p class="m-0">&copy; 2026 BMH Perumbavoor. All rights reserved.</p>
                </div>
            </div>
        </div>
    </footer>

    <!-- Mobile Menu Overlay -->
    <div id="anywhere-home"></div>

    <!-- Mobile Menu -->
    <div class="side-bar">
        <button class="close-icon-menu"><i class="far fa-times"></i></button>
        <div class="inner-main-wrapper-desk">
            <div class="thumbnail">
                <h3 class="m-0" style="color: var(--color-primary); font-weight: 800;">BMH <span style="color: var(--color-secondary);">Perumbavoor</span></h3>
            </div>
            <div class="inner-content">
                <ul class="mobile-menu-link">
                    <li><a href="#hero">Home</a></li>
                    <li><a href="#overview">Overview</a></li>
                    <li><a href="#facilities">Facilities</a></li>
                    <li><a href="#specialities">Specialities</a></li>
                    <li><a href="#gallery">Gallery</a></li>
                    <li><a href="#enquiry">Contact</a></li>
                </ul>
            </div>
        </div>
    </div>

    <!-- Scripts -->
    <script src="assets/js/plugins/jquery.js"></script>
    <script src="assets/js/plugins/jquery-ui.js"></script>
    <script src="assets/js/vendor/waw.js"></script>
    <script src="assets/js/plugins/swiper.js"></script>
    <script src="assets/js/plugins/metismenu.js"></script>
    <script src="assets/js/plugins/jarallax.js"></script>
    <script src="assets/js/plugins/smooth-scroll.js"></script>
    <script src="assets/js/plugins/magnifying-popup.js"></script>
    <script src="assets/js/vendor/bootstrap.min.js"></script>
    <script src="assets/js/main.js"></script>
    
    <!-- Custom Scroll Script -->
    <script>
        $(document).ready(function(){
            // Smooth scrolling for anchor links
            $('a[href^="#"]').on('click', function(event) {
                var target = $(this.getAttribute('href'));
                if( target.length ) {
                    event.preventDefault();
                    $('html, body').stop().animate({
                        scrollTop: target.offset().top - 80
                    }, 1000);
                }
            });
            
            // Mobile menu toggle
            $('#menu-btn').on('click', function() {
                $('.side-bar').addClass('show');
                $('#anywhere-home').addClass('bgshow');
            });
            $('.close-icon-menu, #anywhere-home, .mobile-menu-link a').on('click', function() {
                $('.side-bar').removeClass('show');
                $('#anywhere-home').removeClass('bgshow');
            });
        });
    </script>
</body>
</html>