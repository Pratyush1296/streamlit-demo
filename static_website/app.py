import streamlit as st

st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# -----------------------------
# Product Data
# -----------------------------
products = [
    {
        "name": "Urban Backpack",
        "price": 2499,
        "description": "A sleek waterproof backpack with laptop storage and daily-use comfort.",
        "category": "Bags",
        "emoji": "🎒"
    },
    {
        "name": "Wireless Headphones",
        "price": 3999,
        "description": "Noise-isolating Bluetooth headphones with 30-hour battery life.",
        "category": "Electronics",
        "emoji": "🎧"
    },
    {
        "name": "Smart Fitness Watch",
        "price": 5999,
        "description": "Track steps, heart rate, workouts, sleep, and notifications in style.",
        "category": "Electronics",
        "emoji": "⌚"
    },
    {
        "name": "Cotton Casual Shirt",
        "price": 1299,
        "description": "Breathable premium cotton shirt for office, college, and casual outings.",
        "category": "Fashion",
        "emoji": "👕"
    },
    {
        "name": "Ceramic Coffee Mug",
        "price": 499,
        "description": "Minimal ceramic mug perfect for coffee, tea, and cozy desk setups.",
        "category": "Home",
        "emoji": "☕"
    },
    {
        "name": "Desk Organizer",
        "price": 899,
        "description": "Modern wooden organizer for pens, notes, gadgets, and workspace essentials.",
        "category": "Home",
        "emoji": "🗂️"
    }
]

# -----------------------------
# CSS Styling
# -----------------------------
st.markdown(
    """
    <style>
    .hero {
        padding: 3rem 2rem;
        border-radius: 24px;
        background: linear-gradient(135deg, #111827, #4f46e5);
        color: white;
        margin-bottom: 2rem;
    }

    .hero h1 {
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }

    .hero p {
        font-size: 1.15rem;
        color: #e5e7eb;
        max-width: 720px;
    }

    .section-title {
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 1rem;
        margin-bottom: 1rem;
        color: #111827;
    }

    .product-card {
        background: white;
        padding: 1.5rem;
        border-radius: 20px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        border: 1px solid #eef0f4;
        min-height: 300px;
        margin-bottom: 1.5rem;
    }

    .product-emoji {
        font-size: 3rem;
    }

    .product-name {
        font-size: 1.25rem;
        font-weight: 700;
        color: #111827;
    }

    .product-category {
        display: inline-block;
        padding: 0.25rem 0.65rem;
        border-radius: 999px;
        background-color: #eef2ff;
        color: #4f46e5;
        font-size: 0.8rem;
        font-weight: 600;
        margin: 0.5rem 0;
    }

    .product-description {
        color: #4b5563;
        font-size: 0.95rem;
        min-height: 72px;
    }

    .product-price {
        font-size: 1.25rem;
        font-weight: 800;
        color: #16a34a;
        margin-top: 1rem;
    }

    .floating-support {
        position: fixed;
        bottom: 25px;
        right: 25px;
        background: #4f46e5;
        color: white !important;
        padding: 14px 22px;
        border-radius: 999px;
        font-weight: 700;
        text-decoration: none;
        box-shadow: 0 10px 25px rgba(79,70,229,0.35);
        z-index: 9999;
    }

    .floating-support:hover {
        background: #3730a3;
        color: white !important;
    }

    .footer {
        text-align: center;
        color: #6b7280;
        margin-top: 3rem;
        padding: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🛒 MiniStore")

categories = ["All"] + sorted(set(product["category"] for product in products))
selected_category = st.sidebar.selectbox("Browse by category", categories)

st.sidebar.markdown("---")
st.sidebar.subheader("Shopping Cart Summary")
st.sidebar.metric("Items in cart", 0)
st.sidebar.metric("Cart total", "₹0")
st.sidebar.info("This is a demo cart.")

# Streamlit multipage navigation link
st.sidebar.page_link("pages/support_chatbot.py", label="💬 Support Chatbot")

# -----------------------------
# Filter Products
# -----------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        product for product in products
        if product["category"] == selected_category
    ]

# -----------------------------
# Homepage
# -----------------------------
st.markdown(
    """
    <div class="hero">
        <h1>Welcome to MiniStore</h1>
        <p>
            Discover stylish, useful, and affordable products curated for everyday life.
            From smart gadgets to home essentials, MiniStore brings a clean shopping
            experience in one simple demo website.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Featured Products", "6+")

with col2:
    st.metric("Categories", "4")

with col3:
    st.metric("Demo Friendly", "100%")

st.markdown('<div class="section-title">Featured Products</div>', unsafe_allow_html=True)

# Product cards using st.columns
for i in range(0, len(filtered_products), 3):
    cols = st.columns(3)

    for col, product in zip(cols, filtered_products[i:i + 3]):
        with col:
            st.markdown(
                f"""
                <div class="product-card">
                    <div class="product-emoji">{product["emoji"]}</div>
                    <div class="product-name">{product["name"]}</div>
                    <div class="product-category">{product["category"]}</div>
                    <div class="product-description">{product["description"]}</div>
                    <div class="product-price">₹{product["price"]}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.button("Add to Cart", key=f"add_{product['name']}")

# Floating support button
st.markdown(
    """
    <a href="/support_chatbot" target="_self" class="floating-support">
        💬 Need Help?
    </a>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="footer">
        MiniStore Demo Website · Built with Streamlit
    </div>
    """,
    unsafe_allow_html=True
)