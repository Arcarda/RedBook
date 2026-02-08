import os

def create_svg_assets():
    # Dimensions (Points)
    # 5in x 7in page
    # Margins: Top 0.5in (36pt), Bottom 0.625in (45pt), Inner 0.75in (54pt), Outer 0.5in (36pt)
    
    # SVG Viewport should match the PAGE size 5x7 so they can be dropped in place?
    # Or just the content area? 
    # Better to match the full page 360pt x 504pt (5x72, 7x72) so alignment is automatic (0,0)
    
    w_pt = 360
    h_pt = 504
    
    # Left Page Content Area
    # x = Outer Margin = 36
    # y = Top Margin = 36
    # w_content = 360 - 36 - 54 = 270
    # h_content = 504 - 36 - 45 = 423
    
    # Styles
    style_line = 'stroke="black" stroke-width="1"'
    style_text_head_main = 'font-family="Arial" font-size="14" font-weight="bold" fill="#8B0000" text-anchor="middle"'
    style_text_head_sub = 'font-family="Arial" font-size="12" font-weight="bold" fill="#8B0000" text-anchor="start"'
    style_text_label = 'font-family="Arial" font-size="10" font-weight="bold" fill="black" text-anchor="middle"'
    style_text_body = 'font-family="Garamond" font-size="11" fill="black"'
    style_box = 'fill="none" stroke="black" stroke-width="1"'
    
    # ---------------------------------------------------------
    # 1. Master C Left (Morning Watch)
    # ---------------------------------------------------------
    svg_left = f'''<svg width="{w_pt}pt" height="{h_pt}pt" viewBox="0 0 {w_pt} {h_pt}" xmlns="http://www.w3.org/2000/svg">
    <!-- Guides for Margins (Optional, remove before print) -->
    <rect x="36" y="36" width="270" height="423" fill="none" stroke="#ccc" stroke-dasharray="4"/>
    
    <!-- Title -->
    <text x="{36 + 135}" y="70" {style_text_head_main}>MORNING WATCH</text>
    <line x1="36" y1="80" x2="306" y2="80" stroke="black" stroke-width="2"/>
    
    <!-- H.A.L.T Check -->
    <g transform="translate(36, 110)">
        <text x="0" y="10" {style_text_body} font-weight="bold">H.A.L.T.:</text>
        <rect x="60" y="0" width="10" height="10" {style_box}/> <text x="75" y="10" {style_text_body}>Hungry</text>
        <rect x="120" y="0" width="10" height="10" {style_box}/> <text x="135" y="10" {style_text_body}>Angry</text>
        <rect x="175" y="0" width="10" height="10" {style_box}/> <text x="190" y="10" {style_text_body}>Lonely</text>
        <rect x="230" y="0" width="10" height="10" {style_box}/> <text x="245" y="10" {style_text_body}>Tired</text>
    </g>
    
    <!-- Section 1 -->
    <g transform="translate(36, 150)">
        <text x="0" y="0" {style_text_head_sub}>1. PRIMARY OBJECTIVE</text>
        <text x="0" y="20" {style_text_body}>What is the ONE thing that makes today successful?</text>
        <line x1="0" y1="40" x2="270" y2="40" {style_line}/>
        <line x1="0" y1="65" x2="270" y2="65" {style_line}/>
    </g>
    
    <!-- Section 2 -->
    <g transform="translate(36, 240)">
        <text x="0" y="0" {style_text_head_sub}>2. THREAT ASSESSMENT</text>
        <text x="0" y="20" {style_text_body}>Where are the traps? (Calendar, events, triggers)</text>
        <line x1="0" y1="40" x2="270" y2="40" {style_line}/>
        <line x1="0" y1="65" x2="270" y2="65" {style_line}/>
    </g>
    
    <!-- Section 3 -->
    <g transform="translate(36, 330)">
        <text x="0" y="0" {style_text_head_sub}>3. PASSENGER ALERT</text>
        <text x="0" y="20" {style_text_body}>What is the resistance telling you right now?</text>
        <line x1="0" y1="40" x2="270" y2="40" {style_line}/>
        <line x1="0" y1="65" x2="270" y2="65" {style_line}/>
    </g>
    
    </svg>'''
    
    with open('Affinity_Asset_Master_C_Left.svg', 'w') as f:
        f.write(svg_left)
        
    # ---------------------------------------------------------
    # 2. Master C Right (Evening Debrief)
    # ---------------------------------------------------------
    # Margins Shifted: Left (Inner) 54, Right (Outer) 36
    
    svg_right = f'''<svg width="{w_pt}pt" height="{h_pt}pt" viewBox="0 0 {w_pt} {h_pt}" xmlns="http://www.w3.org/2000/svg">
    <!-- Guides -->
    <rect x="54" y="36" width="270" height="423" fill="none" stroke="#ccc" stroke-dasharray="4"/>
    
    <!-- Title -->
    <text x="{54 + 135}" y="70" {style_text_head_main}>EVENING DEBRIEF</text>
    <line x1="54" y1="80" x2="{54+270}" y2="80" stroke="black" stroke-width="2"/>
    
    <!-- Section 1 -->
    <g transform="translate(54, 120)">
        <text x="0" y="0" {style_text_head_sub}>1. THE WIN</text>
        <text x="0" y="20" {style_text_body}>One thing I did well today.</text>
        <line x1="0" y1="40" x2="270" y2="40" {style_line}/>
        <line x1="0" y1="65" x2="270" y2="65" {style_line}/>
    </g>
    
    <!-- Section 2 -->
    <g transform="translate(54, 210)">
        <text x="0" y="0" {style_text_head_sub}>2. THE VARIANCE</text>
        <text x="0" y="20" {style_text_body}>Where did I drift? Why?</text>
        <line x1="0" y1="40" x2="270" y2="40" {style_line}/>
        <line x1="0" y1="65" x2="270" y2="65" {style_line}/>
    </g>
    
    <!-- Rating Box -->
    <g transform="translate(54, 350)">
        <rect x="0" y="0" width="270" height="60" fill="#f5f5f5" stroke="black" stroke-width="1"/>
        <text x="135" y="20" {style_text_label}>DAILY RATING</text>
        <text x="135" y="45" {style_text_body} text-anchor="middle">Sleep: ___ / Fuel: ___ / Move: ___</text>
    </g>
    
    </svg>'''
    
    with open('Affinity_Asset_Master_C_Right.svg', 'w') as f:
        f.write(svg_right)

    print("SVG Assets Created: Affinity_Asset_Master_C_Left.svg, Affinity_Asset_Master_C_Right.svg")

    # ---------------------------------------------------------
    # 3. Master A Frame (Standard Text Page)
    # ---------------------------------------------------------
    # Split into Left/Right to handle Asymmetric Margins (Gutter = 54pt, Outer = 36pt)
    
    # Master A LEFT (Outer=36, Inner=54) -> width 270 starts at 36, ends at 306
    svg_master_a_left = f'''<svg width="{w_pt}pt" height="{h_pt}pt" viewBox="0 0 {w_pt} {h_pt}" xmlns="http://www.w3.org/2000/svg">
    <!-- Header Line -->
    <line x1="36" y1="36" x2="306" y2="36" stroke="black" stroke-width="2"/>
    <!-- Footer Line -->
    <line x1="{36 + 90}" y1="468" x2="{36 + 180}" y2="468" stroke="black" stroke-width="1"/>
    </svg>'''

    with open('Affinity_Asset_Master_A_Left.svg', 'w') as f:
        f.write(svg_master_a_left)
        
    # Master A RIGHT (Inner=54, Outer=36) -> width 270 starts at 54, ends at 324
    svg_master_a_right = f'''<svg width="{w_pt}pt" height="{h_pt}pt" viewBox="0 0 {w_pt} {h_pt}" xmlns="http://www.w3.org/2000/svg">
    <!-- Header Line -->
    <line x1="54" y1="36" x2="324" y2="36" stroke="black" stroke-width="2"/>
    <!-- Footer Line -->
    <line x1="{54 + 90}" y1="468" x2="{54 + 180}" y2="468" stroke="black" stroke-width="1"/>
    </svg>'''

    with open('Affinity_Asset_Master_A_Right.svg', 'w') as f:
        f.write(svg_master_a_right)

    # ---------------------------------------------------------
    # 4. Master B Divider (Section Title)
    # ---------------------------------------------------------
    # Decorative Anchor for Chapter Starts (Usually Right Page)
    # Right Page Margins: Inner=54, Outer=36
    svg_master_b = f'''<svg width="{w_pt}pt" height="{h_pt}pt" viewBox="0 0 {w_pt} {h_pt}" xmlns="http://www.w3.org/2000/svg">
    <!-- Top Divider -->
    <line x1="54" y1="100" x2="324" y2="100" stroke="black" stroke-width="4"/>
    
    <!-- Bottom Anchor Icon (Centered in Content Area) -->
    <!-- Content Center is 54 + 135 = 189 -->
    <g transform="translate(189, 400)">
        <path d="M-20,0 Q0,30 20,0 M0,-20 L0,20 M-10,-10 L10,-10" stroke="black" stroke-width="2" fill="none"/>
    </g>
    </svg>'''

    with open('Affinity_Asset_Master_B_Right.svg', 'w') as f:
        f.write(svg_master_b)

    print("SVG Assets Updated: Master C (L/R), Master A (L/R), Master B (Right)")

if __name__ == '__main__':
    create_svg_assets()
