import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target_content_1 = '''                                        <div class="pre-title float-right-1">
                                            <img class="mr--5" src="assets/images/banner/icons/03.png" alt="icons">
                                            <span>Comprehensive Eye Care</span>
                                        </div>
                                        <h1 class="title float-right">Advanced Eye <br> Care Brighter <br> Future</h1>
                                        <p class="disc float-bottom">
                                            Discover quality eye care that puts your needs first. With a focus on
                                            precision and patient-centered service,Mediweb is here to help you see the
                                            world more clearly, ensuring a lifetime of healthy vision.
                                        </p>
                                        <a href="appoinment.html" class="rts-btn btn-primary float-bottom-2">Book
                                            Appointment</a>'''

target_content_2 = '''                                        <div class="pre-title float-right-1">
                                            <img class="mr--5" src="assets/images/banner/icons/03.png" alt="icons">
                                            <span>Advanced Diagnostic Technology</span>
                                        </div>
                                        <h1 class="title float-right">Advanced Eye <br> Care Brighter <br> Future</h1>
                                        <p class="disc float-bottom">
                                            Discover quality eye care that puts your needs first. With a focus on
                                            precision and patient-centered service,Mediweb is here to help you see the
                                            world more clearly, ensuring a lifetime of healthy vision.
                                        </p>
                                        <a href="appoinment.html" class="rts-btn btn-primary float-bottom-2">Book
                                            Appointment</a>'''

replacement = '''                                        <div class="pre-title float-right-1">
                                            <i class="fa-solid fa-heart-pulse mr--5" style="color: var(--color-success);"></i>
                                            <span>BMH Perumbavoor</span>
                                        </div>
                                        <h1 class="title float-right">Advanced Healthcare, <br> Closer to Home</h1>
                                        <p class="disc float-bottom">
                                            BMH Perumbavoor brings together experienced specialists, advanced medical technology, and compassionate patient care to deliver trusted healthcare for families across Perumbavoor and nearby regions.
                                        </p>
                                        <div class="d-flex flex-wrap gap-3 float-bottom-2 mb-4">
                                            <a href="#appoinment" class="rts-btn btn-primary">Book Appointment</a>
                                            <a href="#emergency" class="rts-btn btn-primary" style="background: var(--color-danger); border-color: var(--color-danger);">Emergency Care</a>
                                            <a href="#enquire" class="rts-btn btn-primary" style="background: transparent; border: 1px solid var(--color-primary); color: var(--color-primary);">Enquire Now</a>
                                        </div>
                                        <div class="hero-highlights float-bottom-2" style="display: flex; flex-wrap: wrap; gap: 15px; align-items: center;">
                                            <span style="font-weight: 500; font-size: 14px;"><i class="fa-solid fa-check-circle" style="color: var(--color-success);"></i> 24x7 Emergency Services</span>
                                            <span style="font-weight: 500; font-size: 14px;"><i class="fa-solid fa-check-circle" style="color: var(--color-success);"></i> Multi-speciality Care</span>
                                            <span style="font-weight: 500; font-size: 14px;"><i class="fa-solid fa-check-circle" style="color: var(--color-success);"></i> Advanced Diagnostics</span>
                                            <span style="font-weight: 500; font-size: 14px;"><i class="fa-solid fa-check-circle" style="color: var(--color-success);"></i> Expert Medical Team</span>
                                            <span style="font-weight: 500; font-size: 14px;"><i class="fa-solid fa-check-circle" style="color: var(--color-success);"></i> Modern Infrastructure</span>
                                        </div>'''

content = content.replace(target_content_1, replacement)
content = content.replace(target_content_2, replacement)

content = content.replace('<div class="banner-wrapper-bg bg_image ptb--180 ptb_sm--100">', '<div class="banner-wrapper-bg bg_image ptb--180 ptb_sm--100" style="background-image: url(\'assets/images/banner/bmh_hero_bg.png\');">')
content = content.replace('<div class="banner-wrapper-bg bg-2-banner-2 bg_image ptb--180 ptb_sm--100">', '<div class="banner-wrapper-bg bg-2-banner-2 bg_image ptb--180 ptb_sm--100" style="background-image: url(\'assets/images/banner/bmh_hero_bg.png\');">')
content = content.replace('<div class="banner-wrapper-bg bg-2-banner-3 bg_image ptb--180 ptb_sm--100">', '<div class="banner-wrapper-bg bg-2-banner-3 bg_image ptb--180 ptb_sm--100" style="background-image: url(\'assets/images/banner/bmh_hero_bg.png\');">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
