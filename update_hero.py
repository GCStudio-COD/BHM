import sys

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_hero = """    <!-- banner area start -->
    <div class="rts-banner-area-two bmh-hero-section" style="background: linear-gradient(rgba(10, 74, 142, 0.85), rgba(0, 168, 204, 0.6)), url('assets/images/banner/bmh_hero_bg.png') center/cover no-repeat; padding: 180px 0 120px;">
        <div class="container">
            <div class="row">
                <div class="col-lg-10">
                    <div class="banner-content-area">
                        <h1 class="title" style="color: #ffffff; font-size: 54px; font-weight: 700; margin-bottom: 25px; line-height: 1.2;">Advanced Healthcare,<br>Closer to Home</h1>
                        <p class="disc" style="color: #f8f9fa; font-size: 18px; line-height: 1.6; margin-bottom: 40px; max-width: 700px;">
                            BMH Perumbavoor brings together experienced specialists, advanced medical technology, and compassionate patient care to deliver trusted healthcare for families across Perumbavoor and nearby regions.
                        </p>
                        
                        <div class="hero-highlights" style="display: flex; flex-wrap: wrap; gap: 20px; align-items: center;">
                            <span style="color: #fff; display: flex; align-items: center; gap: 8px; font-weight: 500;"><i class="fa-solid fa-check-circle" style="color: var(--color-success);"></i> 24x7 Emergency Services</span>
                            <span style="color: #fff; display: flex; align-items: center; gap: 8px; font-weight: 500;"><i class="fa-solid fa-check-circle" style="color: var(--color-success);"></i> Multi-speciality Care</span>
                            <span style="color: #fff; display: flex; align-items: center; gap: 8px; font-weight: 500;"><i class="fa-solid fa-check-circle" style="color: var(--color-success);"></i> Advanced Diagnostics</span>
                            <span style="color: #fff; display: flex; align-items: center; gap: 8px; font-weight: 500;"><i class="fa-solid fa-check-circle" style="color: var(--color-success);"></i> Expert Medical Team</span>
                            <span style="color: #fff; display: flex; align-items: center; gap: 8px; font-weight: 500;"><i class="fa-solid fa-check-circle" style="color: var(--color-success);"></i> Modern Infrastructure</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- banner area end -->
"""

# Delete lines 236 to 323 (0-indexed 236 to 324)
del lines[236:324]

# Insert new hero
lines.insert(236, new_hero)

# Fix head
for i, line in enumerate(lines):
    if '<title>Medical & Health Care' in line:
        lines[i] = '    <title>BMH Perumbavoor - Advanced Healthcare</title>\n'
        lines[i+1] = '' # Remove '        HTML Template</title>'
    if 'name="description"' in line:
        lines[i] = '    <meta name="description" content="BMH Perumbavoor brings together experienced specialists, advanced medical technology, and compassionate patient care to deliver trusted healthcare for families across Perumbavoor and nearby regions.">\n    <!-- FontAwesome for icons -->\n    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n'
        break

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
