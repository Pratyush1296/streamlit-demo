import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Support Chatbot",
    page_icon="💬",
    layout="wide"
)

# -----------------------------
# OpenAI client
# -----------------------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# -----------------------------
# MiniStore product catalog
# -----------------------------
products = [
    {
        "name": "Urban Backpack",
        "price": 2499,
        "description": "A sleek waterproof backpack with laptop storage and daily-use comfort.",
        "category": "Bags"
    },
    {
        "name": "Wireless Headphones",
        "price": 3999,
        "description": "Noise-isolating Bluetooth headphones with 30-hour battery life.",
        "category": "Electronics"
    },
    {
        "name": "Smart Fitness Watch",
        "price": 5999,
        "description": "Track steps, heart rate, workouts, sleep, and notifications in style.",
        "category": "Electronics"
    },
    {
        "name": "Cotton Casual Shirt",
        "price": 1299,
        "description": "Breathable premium cotton shirt for office, college, and casual outings.",
        "category": "Fashion"
    },
    {
        "name": "Ceramic Coffee Mug",
        "price": 499,
        "description": "Minimal ceramic mug perfect for coffee, tea, and cozy desk setups.",
        "category": "Home"
    },
    {
        "name": "Desk Organizer",
        "price": 899,
        "description": "Modern wooden organizer for pens, notes, gadgets, and workspace essentials.",
        "category": "Home"
    }
]

# -----------------------------
# Build product catalog text
# -----------------------------
catalog_text = "\n".join(
    [
        f"- {p['name']} | Category: {p['category']} | Price: ₹{p['price']} | Description: {p['description']}"
        for p in products
    ]
)

# -----------------------------
# System prompt
# -----------------------------
SYSTEM_PROMPT = f"""
You are MiniStore Support Assistant, a professional and friendly customer support representative for MiniStore.

Your job is to help customers with store-related questions only.

You can answer questions about:
- MiniStore products
- Product categories
- Product prices
- Product descriptions
- Delivery and shipping
- Refunds
- Returns and exchanges
- Payment methods
- Order status and tracking

MiniStore product catalog:
{catalog_text}

Store policies:
- Delivery usually takes 3–5 business days.
- Returns are accepted within 7 days of delivery if the product is unused, undamaged, and in original packaging.
- Refunds are processed after return quality inspection and usually take 5–7 business days after approval.
- Supported payment methods include UPI, debit cards, credit cards, net banking, and cash on delivery.
- Live order tracking is not connected in this demo app. If customers ask about order status, politely ask them for an order ID and explain that real tracking would require backend integration.

Important restrictions:
- Only answer questions related to MiniStore support.
- If the user asks about unrelated topics, politely redirect them back to MiniStore topics.
- Do not make up products that are not in the catalog.
- Do not claim that an order has shipped, failed, or been refunded unless the user provides information.
- Keep answers concise, helpful, and professional.
"""

# -----------------------------
# CSS
# -----------------------------
st.markdown(
    """
    <style>
    .chat-header {
        padding: 2rem;
        border-radius: 22px;
        background: linear-gradient(135deg, #111827, #4f46e5);
        color: white;
        margin-bottom: 2rem;
    }

    .chat-header h1 {
        margin-bottom: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Page header
# -----------------------------
st.markdown(
    """
    <div class="chat-header">
        <h1>💬 MiniStore Support Chatbot</h1>
        <p>Ask about products, delivery, refunds, returns, payments, or order status.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.page_link("app.py", label="← Back to MiniStore Homepage")

# -----------------------------
# Initialize chat history
# -----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "assistant",
            "content": "Hi! Welcome to MiniStore Support. How can I help you today?"
        }
    ]

# -----------------------------
# Show chat history
# -----------------------------
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Chat input
# -----------------------------
user_input = st.chat_input("Type your question here...")

if user_input:
    # Save user message
    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Prepare conversation for OpenAI
    conversation = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ] + st.session_state.chat_history

    try:
        with st.chat_message("assistant"):
            with st.spinner("MiniStore Support is typing..."):
                response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=conversation,
                    temperature=0.3,
                    max_tokens=400
                )

                assistant_reply = response.choices[0].message.content

                st.markdown(assistant_reply)

        # Save assistant response
        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": assistant_reply
            }
        )

    except Exception as e:
        error_message = (
            "Sorry, I could not connect to MiniStore Support right now. "
            "Please check your API key and try again."
        )

        with st.chat_message("assistant"):
            st.error(error_message)

        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": error_message
            }
        )