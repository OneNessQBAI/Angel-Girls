import streamlit as st
import os
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Angel Girls - Exclusive Escort Agency",
    page_icon="👼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        border-radius: 15px;
        margin-bottom: 2rem;
        color: white;
    }
    .main-header h1 {
        font-size: 3.5rem;
        margin-bottom: 0.5rem;
        background: linear-gradient(90deg, #e94560, #ff6b6b, #e94560);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: none;
    }
    .main-header p {
        font-size: 1.2rem;
        color: #ccc;
        font-style: italic;
    }
    .profile-card {
        background: linear-gradient(145deg, #1e1e2f, #2a2a40);
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid #333;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .profile-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(233, 69, 96, 0.2);
        border-color: #e94560;
    }
    .profile-name {
        font-size: 1.8rem;
        font-weight: bold;
        color: #e94560;
        margin-bottom: 0.3rem;
    }
    .profile-age {
        font-size: 1rem;
        color: #aaa;
        margin-bottom: 0.8rem;
    }
    .profile-desc {
        color: #ddd;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 0.8rem;
    }
    .profile-stats {
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
        margin-bottom: 0.8rem;
    }
    .stat-badge {
        background: rgba(233, 69, 96, 0.15);
        color: #e94560;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        border: 1px solid rgba(233, 69, 96, 0.3);
    }
    .contact-btn {
        background: linear-gradient(90deg, #e94560, #ff6b6b);
        color: white;
        border: none;
        padding: 0.5rem 1.5rem;
        border-radius: 25px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        text-align: center;
        display: inline-block;
    }
    .contact-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 15px rgba(233, 69, 96, 0.4);
    }
    .footer {
        text-align: center;
        padding: 2rem;
        color: #666;
        font-size: 0.85rem;
        border-top: 1px solid #333;
        margin-top: 3rem;
    }
    .section-title {
        color: #e94560;
        font-size: 2rem;
        font-weight: bold;
        margin: 2rem 0 1.5rem 0;
        text-align: center;
        border-bottom: 2px solid #333;
        padding-bottom: 0.5rem;
    }
    .about-section {
        background: linear-gradient(145deg, #1e1e2f, #2a2a40);
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        border: 1px solid #333;
    }
    .about-section h2 {
        color: #e94560;
        margin-bottom: 1rem;
    }
    .about-section p {
        color: #ccc;
        line-height: 1.8;
        font-size: 1.05rem;
    }
    .testimonial-card {
        background: linear-gradient(145deg, #1e1e2f, #2a2a40);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid #e94560;
    }
    .testimonial-text {
        color: #ddd;
        font-style: italic;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    .testimonial-author {
        color: #e94560;
        font-weight: bold;
        margin-top: 0.5rem;
        font-size: 0.9rem;
    }
    .stApp {
        background: #0a0a1a;
    }
    .stButton button {
        background: linear-gradient(90deg, #e94560, #ff6b6b);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 15px rgba(233, 69, 96, 0.4);
    }
    .disclaimer {
        background: rgba(233, 69, 96, 0.1);
        border: 1px solid rgba(233, 69, 96, 0.3);
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        color: #ccc;
        font-size: 0.85rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>👼 Angel Girls</h1>
    <p>✦ Exclusive Companion Agency — Discretion, Elegance & Sophistication ✦</p>
</div>
""", unsafe_allow_html=True)

# Navigation tabs
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "👩‍🦰 Our Angels", "📖 About Us", "📞 Contact"])

# ==================== TAB 1: HOME ====================
with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div style="padding: 2rem 0;">
            <h2 style="color: #e94560; font-size: 2.5rem;">Welcome to Angel Girls</h2>
            <p style="color: #ccc; font-size: 1.2rem; line-height: 1.8; margin-top: 1rem;">
                Discover the finest companionship experience with our carefully selected 
                angels. Each of our companions embodies elegance, intelligence, and charm — 
                ensuring every moment spent together is truly unforgettable.
            </p>
            <p style="color: #aaa; font-size: 1rem; line-height: 1.8;">
                Whether you're looking for a dinner date, a travel companion, or simply 
                someone to share quality time with, Angel Girls provides a discreet and 
                professional service tailored to your desires.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="display: flex; gap: 2rem; flex-wrap: wrap; margin: 2rem 0;">
            <div style="flex: 1; min-width: 150px; text-align: center; background: linear-gradient(145deg, #1e1e2f, #2a2a40); padding: 1.5rem; border-radius: 12px; border: 1px solid #333;">
                <h3 style="color: #e94560; font-size: 2rem;">50+</h3>
                <p style="color: #aaa;">Exclusive Angels</p>
            </div>
            <div style="flex: 1; min-width: 150px; text-align: center; background: linear-gradient(145deg, #1e1e2f, #2a2a40); padding: 1.5rem; border-radius: 12px; border: 1px solid #333;">
                <h3 style="color: #e94560; font-size: 2rem;">100%</h3>
                <p style="color: #aaa;">Discretion Guaranteed</p>
            </div>
            <div style="flex: 1; min-width: 150px; text-align: center; background: linear-gradient(145deg, #1e1e2f, #2a2a40); padding: 1.5rem; border-radius: 12px; border: 1px solid #333;">
                <h3 style="color: #e94560; font-size: 2rem;">24/7</h3>
                <p style="color: #aaa;">Premium Service</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(145deg, #1e1e2f, #2a2a40); border-radius: 15px; padding: 2rem; border: 1px solid #333; margin-top: 2rem;">
            <h3 style="color: #e94560; margin-bottom: 1rem;">✨ Why Choose Us</h3>
            <ul style="color: #ccc; line-height: 2.2; list-style: none; padding: 0;">
                <li>✓ Carefully vetted companions</li>
                <li>✓ Absolute privacy & discretion</li>
                <li>✓ Professional & respectful service</li>
                <li>✓ Available for any occasion</li>
                <li>✓ International companions</li>
                <li>✓ VIP experiences available</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ==================== TAB 2: OUR ANGELS ====================
with tab2:
    st.markdown('<div class="section-title">✨ Meet Our Angels ✨</div>', unsafe_allow_html=True)
    
    # Profile data
    profiles = [
        {
            "name": "Sofia",
            "age": 24,
            "image": "assets/11.jpg",
            "description": "Elegant and sophisticated, Sofia is the perfect companion for high-end events and romantic dinners. With her captivating smile and intelligent conversation, she will make any occasion special.",
            "stats": ["175 cm", "55 kg", "Brown Eyes", "Brunette", "Spanish"],
            "rate": "$300/hr"
        },
        {
            "name": "Isabella",
            "age": 26,
            "image": "assets/22.jpg",
            "description": "A true goddess with mesmerizing blue eyes. Isabella is passionate, adventurous, and loves to travel. She speaks three languages and is the ideal companion for international trips.",
            "stats": ["170 cm", "58 kg", "Blue Eyes", "Blonde", "Italian"],
            "rate": "$310/hr"
        },
        {
            "name": "Valentina",
            "age": 23,
            "image": "assets/33.jpg",
            "description": "Exotic beauty with a warm heart. Valentina is known for her sensual dance moves and charming personality. She will make you feel like the most special person in the world.",
            "stats": ["168 cm", "52 kg", "Green Eyes", "Red Hair", "Brazilian"],
            "rate": "$280/hr"
        },
        {
            "name": "Camila",
            "age": 25,
            "image": "assets/44.jpg",
            "description": "Athletic and energetic, Camila is the perfect partner for active dates. From hiking to dancing, she brings positive energy and a radiant smile to every encounter.",
            "stats": ["172 cm", "60 kg", "Hazel Eyes", "Brown", "Colombian"],
            "rate": "$320/hr"
        },
        {
            "name": "Luna",
            "age": 22,
            "image": "assets/55.jpg",
            "description": "Mysterious and alluring, Luna has a magnetic presence that draws people in. She is an artist and a dreamer, with a deep appreciation for fine wine and classical music.",
            "stats": ["165 cm", "50 kg", "Dark Eyes", "Black", "French"],
            "rate": "$290/hr"
        },
        {
            "name": "Gabriela",
            "age": 27,
            "image": "assets/66.jpg",
            "description": "Mature and refined, Gabriela offers a premium VIP experience. With her extensive knowledge of fine dining and fashion, she is the ultimate companion for discerning gentlemen.",
            "stats": ["178 cm", "62 kg", "Amber Eyes", "Blonde", "Russian"],
            "rate": "$300/hr"
        },
        {
            "name": "Angelina",
            "age": 24,
            "image": "assets/77.jpg",
            "description": "Sweet and affectionate, Angelina has a natural talent for making people feel comfortable. Her warm personality and stunning looks make her one of our most requested angels.",
            "stats": ["167 cm", "54 kg", "Brown Eyes", "Light Brown", "American"],
            "rate": "$310/hr"
        },
        {
            "name": "Victoria",
            "age": 25,
            "image": "assets/88.jpg",
            "description": "Confident and charismatic, Victoria commands attention wherever she goes. A former model, she knows how to present herself with grace and style for any high-profile event.",
            "stats": ["180 cm", "63 kg", "Gray Eyes", "Platinum Blonde", "Swedish"],
            "rate": "$300/hr"
        }
    ]
    
    # Display profiles in a grid (2 columns)
    for i in range(0, len(profiles), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(profiles):
                profile = profiles[i + j]
                with col:
                    # Load and display image
                    img = Image.open(profile["image"])
                    st.image(img, width=400, caption=profile["name"])
                    
                    st.markdown(f"""
                    <div class="profile-card">
                        <div class="profile-name">{profile["name"]}</div>
                        <div class="profile-age">Age: {profile["age"]} | Rate: {profile["rate"]}</div>
                        <div class="profile-desc">{profile["description"]}</div>
                        <div class="profile-stats">
                            {"".join([f'<span class="stat-badge">{stat}</span>' for stat in profile["stats"]])}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button(f"📩 Book {profile['name']}", key=f"book_{profile['name']}"):
                        st.success(f"Thank you for your interest in {profile['name']}! Please contact us via the Contact tab for booking arrangements.")

# ==================== TAB 3: ABOUT US ====================
with tab3:
    st.markdown("""
    <div class="about-section">
        <h2>About Angel Girls</h2>
        <p>
            Angel Girls is a premier escort agency dedicated to providing exceptional 
            companionship experiences. Founded on the principles of discretion, respect, 
            and professionalism, we have been connecting discerning clients with 
            extraordinary companions since 2020.
        </p>
        <p>
            Our carefully curated selection of angels represents the finest companions 
            from around the world. Each angel is thoroughly vetted and chosen not only 
            for their stunning beauty but also for their intelligence, charm, and 
            ability to engage in meaningful conversation.
        </p>
        <p>
            We understand that every client is unique, which is why we offer personalized 
            matching services to ensure the perfect connection. Whether you need a 
            companion for a corporate event, a romantic getaway, or a quiet evening, 
            Angel Girls is here to make your experience unforgettable.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">💬 What Our Clients Say</div>', unsafe_allow_html=True)
    
    testimonials = [
        ("An absolutely incredible experience. Sofia was charming, intelligent, and made my business dinner a huge success. Highly recommended!", "— James R., Business Executive"),
        ("I was nervous at first, but Valentina made me feel completely at ease. She's not just beautiful but genuinely kind and fun to be with.", "— Michael T., Entrepreneur"),
        ("The level of professionalism and discretion at Angel Girls is unmatched. Gabriela accompanied me to a gala and was the perfect date.", "— David L., Investor"),
        ("I've used several agencies before, but Angel Girls is by far the best. Isabella is a dream come true. Will definitely book again!", "— Alexander K., Lawyer"),
    ]
    
    for text, author in testimonials:
        st.markdown(f"""
        <div class="testimonial-card">
            <div class="testimonial-text">"{text}"</div>
            <div class="testimonial-author">{author}</div>
        </div>
        """, unsafe_allow_html=True)

# ==================== TAB 4: CONTACT ====================
with tab4:
    st.markdown("""
    <div class="about-section">
        <h2>📞 Get in Touch</h2>
        <p>
            For bookings, inquiries, or any questions, please reach out to us. 
            Our team is available 24/7 to assist you with discretion and professionalism.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(145deg, #1e1e2f, #2a2a40); border-radius: 15px; padding: 2rem; border: 1px solid #333;">
            <h3 style="color: #e94560; margin-bottom: 1.5rem;">Contact Information</h3>
            <p style="color: #ccc; margin-bottom: 1rem;">📧 <strong>Email:</strong> businessalmonte@gmail.com</p>
            <p style="color: #ccc; margin-bottom: 1rem;">📱 <strong>Phone:</strong> +1 (343) 961-6995</p>
            <p style="color: #ccc; margin-bottom: 1rem;">📍 <strong>Location:</strong> Ottawa Gatineau</p>
            <p style="color: #ccc;">🕐 <strong>Hours:</strong> 24/7 - Always available</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(145deg, #1e1e2f, #2a2a40); border-radius: 15px; padding: 2rem; border: 1px solid #333;">
            <h3 style="color: #e94560; margin-bottom: 1.5rem;">Send a Message</h3>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("contact_form"):
            name = st.text_input("Your Name", placeholder="Enter your name")
            email = st.text_input("Your Email", placeholder="Enter your email")
            phone = st.text_input("Your Phone", placeholder="Enter your phone number")
            preferred = st.selectbox("Preferred Angel", ["Any", "Sofia", "Isabella", "Valentina", "Camila", "Luna", "Gabriela", "Angelina", "Victoria"])
            occasion = st.text_area("Occasion / Message", placeholder="Tell us about the occasion and your preferences...")
            submitted = st.form_submit_button("📩 Send Inquiry")
            
            if submitted:
                st.success("Thank you for your inquiry! We will contact you within 24 hours with absolute discretion.")
    

# Footer
st.markdown("""
<div class="footer">
    <p>👼 Angel Girls — Exclusive Companion Agency</p>
    <p>© 2026 Angel Girls. All rights reserved. | Discretion & Elegance Since 2020</p>
    <p style="font-size: 0.75rem; margin-top: 0.5rem; color: #555;">
        This is a fictional demo application. All content is simulated for demonstration purposes.
    </p>
</div>
""", unsafe_allow_html=True)
