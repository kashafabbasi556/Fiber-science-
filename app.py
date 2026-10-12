import streamlit as st

st.set_page_config(
    page_title="Fiber Science Lab",
    page_icon="🧵",
    layout="wide"
)

# ---------- COLOR THEME ----------
st.markdown("""
<style>
.stApp {
    background-color: #F7F6EF;
    color: #193D32;
}

[data-testid="stSidebar"] {
    background-color: #123B32;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.hero {
    background: linear-gradient(120deg, #123B32, #23866A);
    padding: 35px;
    border-radius: 20px;
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    color: white;
    font-size: 38px;
}

.hero p {
    color: #D8EFE5;
    font-size: 17px;
}

.card {
    background: white;
    border-left: 5px solid #299879;
    padding: 22px;
    border-radius: 14px;
    margin: 12px 0;
    box-shadow: 0 4px 15px rgba(18,59,50,0.07);
}

.card h3 {
    color: #17664F;
}

.stButton > button {
    background: #23866A;
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: bold;
}

.stButton > button:hover {
    background: #123B32;
    color: white;
}

div[data-testid="stMetric"] {
    background: white;
    padding: 15px;
    border-radius: 12px;
    border-bottom: 3px solid #299879;
}

h1, h2, h3 {
    color: #123B32;
}
</style>
""", unsafe_allow_html=True)


# ---------- FIBER DATABASE ----------
fibers = {
    "Cotton": {
        "type": "Natural Cellulosic Fiber",
        "source": "Cotton plant seed hairs",
        "composition": "Mainly cellulose",
        "properties": [
            "Good moisture absorption",
            "Comfortable and breathable",
            "Good strength, especially when wet",
            "Can wrinkle easily"
        ],
        "uses": "Shirts, bedsheets, towels and denim",
        "test": "Burns readily and leaves soft gray ash. Burn tests must only be conducted under laboratory supervision."
    },

    "Wool": {
        "type": "Natural Protein Fiber",
        "source": "Fleece of sheep",
        "composition": "Keratin protein",
        "properties": [
            "Good warmth and insulation",
            "Naturally crimped",
            "Good moisture absorption",
            "May shrink or felt during unsuitable washing"
        ],
        "uses": "Sweaters, coats, blankets and carpets",
        "test": "Burning behavior may include a hair-like odor and crushable ash. Confirm using approved laboratory procedures."
    },

    "Silk": {
        "type": "Natural Protein Fiber",
        "source": "Cocoon of the silkworm",
        "composition": "Mainly fibroin protein",
        "properties": [
            "Smooth and lustrous",
            "Fine and lightweight",
            "Good drape",
            "Sensitive to some chemicals and sunlight"
        ],
        "uses": "Scarves, dresses, ties and luxury fabrics",
        "test": "Has a natural sheen and a smooth filament appearance."
    },

    "Flax": {
        "type": "Natural Bast Fiber",
        "source": "Stem of the flax plant",
        "composition": "Mainly cellulose",
        "properties": [
            "High strength",
            "Good moisture absorption",
            "Cool and comfortable",
            "Wrinkles easily"
        ],
        "uses": "Linen clothing, tablecloths and home textiles",
        "test": "Microscopic examination can show characteristic nodes along the fiber."
    },

    "Polyester": {
        "type": "Synthetic Fiber",
        "source": "Manufactured from polymer materials",
        "composition": "Polyester polymer, commonly PET",
        "properties": [
            "Good wrinkle resistance",
            "Low moisture absorption",
            "Good dimensional stability",
            "Dries relatively quickly"
        ],
        "uses": "Sportswear, curtains, shirts and blended fabrics",
        "test": "Microscopy and suitable chemical identification methods help distinguish polyester."
    },

    "Nylon": {
        "type": "Synthetic Polyamide Fiber",
        "source": "Manufactured polymer",
        "composition": "Polyamide",
        "properties": [
            "High strength",
            "Good abrasion resistance",
            "Lightweight",
            "Thermoplastic"
        ],
        "uses": "Ropes, hosiery, sportswear and carpets",
        "test": "Fiber identification may use microscopy and validated chemical methods."
    },

    "Viscose": {
        "type": "Regenerated Cellulosic Fiber",
        "source": "Regenerated cellulose, commonly from wood pulp",
        "composition": "Cellulose",
        "properties": [
            "Soft feel",
            "Good moisture absorption",
            "Good drape",
            "May lose strength when wet"
        ],
        "uses": "Dresses, linings, shirts and blended fabrics",
        "test": "Microscopy and suitable laboratory methods are used for identification."
    },

    "Acrylic": {
        "type": "Synthetic Fiber",
        "source": "Manufactured polymer",
        "composition": "Mainly polyacrylonitrile",
        "properties": [
            "Lightweight",
            "Good warmth",
            "Wool-like appearance",
            "Good color retention"
        ],
        "uses": "Sweaters, blankets, knitwear and upholstery",
        "test": "Microscopy and approved analytical methods help confirm fiber identity."
    }
}


# ---------- HEADER ----------
st.markdown("""
<div class="hero">
    <h1>🧵 Fiber Science Lab</h1>
    <p>Explore Fibers • Study Properties • Learn Identification</p>
    <p>Textile Engineering | Second Year</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

col1.metric("Fiber Library", len(fibers))
col2.metric("Fiber Categories", 3)
col3.metric("Learning Mode", "Student")


# ---------- SIDEBAR ----------
st.sidebar.title("🧪 Fiber Science")

page = st.sidebar.radio(
    "Select Section",
    [
        "Fiber Explorer",
        "Fiber Classification",
        "Fiber Comparison",
        "Fiber Quiz"
    ]
)


# ---------- FIBER EXPLORER ----------
if page == "Fiber Explorer":

    st.title("🔬 Fiber Explorer")
    st.write("Select a fiber to explore its source, composition, properties and uses.")

    selected = st.selectbox("Choose Fiber", list(fibers.keys()))
    data = fibers[selected]

    st.markdown(f"""
    <div class="card">
        <h3>{selected}</h3>
        <p><b>Fiber Type:</b> {data['type']}</p>
        <p><b>Source:</b> {data['source']}</p>
        <p><b>Composition:</b> {data['composition']}</p>
        <p><b>Common Uses:</b> {data['uses']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Important Properties")

    for prop in data["properties"]:
        st.write("✓", prop)

    st.subheader("Identification Note")
    st.info(data["test"])

    st.warning(
        "Identification notes are introductory only. "
        "Use your laboratory manual and instructor-approved methods "
        "for reliable fiber identification."
    )


# ---------- CLASSIFICATION ----------
elif page == "Fiber Classification":

    st.title("🌿 Classification of Textile Fibers")

    categories = {
        "Natural Fibers": [
            "Cotton", "Wool", "Silk", "Flax"
        ],
        "Synthetic Fibers": [
            "Polyester", "Nylon", "Acrylic"
        ],
        "Regenerated Fibers": [
            "Viscose"
        ]
    }

    for category, items in categories.items():
        st.markdown(f"""
        <div class="card">
            <h3>{category}</h3>
            <p>{", ".join(items)}</p>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("Basic Concepts")

    with st.expander("What is a textile fiber?"):
        st.write(
            "A textile fiber is a fine material with suitable length, "
            "strength and flexibility that can be processed into yarn or fabric."
        )

    with st.expander("What are natural fibers?"):
        st.write(
            "Natural fibers are obtained from plants, animals or minerals. "
            "Cotton, wool and silk are common examples."
        )

    with st.expander("What are man-made fibers?"):
        st.write(
            "Man-made fibers are produced through industrial processes. "
            "They include synthetic fibers such as polyester and nylon, "
            "and regenerated fibers such as viscose."
        )


# ---------- COMPARISON ----------
elif page == "Fiber Comparison":

    st.title("📊 Compare Two Fibers")

    fiber1 = st.selectbox(
        "Select First Fiber",
        list(fibers.keys()),
        key="fiber1"
    )

    fiber2 = st.selectbox(
        "Select Second Fiber",
        list(fibers.keys()),
        index=4,
        key="fiber2"
    )

    if fiber1 == fiber2:
        st.info("Select two different fibers for comparison.")
    else:
        a = fibers[fiber1]
        b = fibers[fiber2]

        st.subheader("Comparison Table")

        st.table({
            "Feature": [
                "Type",
                "Source",
                "Composition",
                "Properties",
                "Common Uses"
            ],
            fiber1: [
                a["type"],
                a["source"],
                a["composition"],
                ", ".join(a["properties"]),
                a["uses"]
            ],
            fiber2: [
                b["type"],
                b["source"],
                b["composition"],
                ", ".join(b["properties"]),
                b["uses"]
            ]
        })


# ---------- QUIZ ----------
elif page == "Fiber Quiz":

    st.title("📝 Test Your Knowledge")

    questions = [
        {
            "q": "Which fiber mainly consists of cellulose?",
            "options": ["Wool", "Cotton", "Silk", "Nylon"],
            "answer": "Cotton"
        },
        {
            "q": "Which fiber is obtained from sheep?",
            "options": ["Flax", "Cotton", "Wool", "Viscose"],
            "answer": "Wool"
        },
        {
            "q": "Which is a synthetic fiber?",
            "options": ["Silk", "Cotton", "Flax", "Polyester"],
            "answer": "Polyester"
        },
        {
            "q": "Which fiber is regenerated from cellulose?",
            "options": ["Viscose", "Nylon", "Wool", "Silk"],
            "answer": "Viscose"
        },
        {
            "q": "Which fiber is a natural protein fiber?",
            "options": ["Polyester", "Cotton", "Silk", "Viscose"],
            "answer": "Silk"
        }
    ]

    with st.form("fiber_quiz"):
        responses = []

        for i, question in enumerate(questions):
            st.markdown(f"**{i + 1}. {question['q']}**")

            response = st.radio(
                "Choose your answer:",
                question["options"],
                key=f"question_{i}"
            )

            responses.append(response)

        submitted = st.form_submit_button("Check My Answers")

    if submitted:
        score = sum(
            responses[i] == questions[i]["answer"]
            for i in range(len(questions))
        )

        st.success(f"Your score: {score} / {len(questions)}")

        for i, question in enumerate(questions):
            if responses[i] == question["answer"]:
                st.write(f"✅ Question {i + 1}: Correct")
            else:
                st.write(
                    f"❌ Question {i + 1}: "
                    f"Correct answer: {question['answer']}"
                )


# ---------- FOOTER ----------
st.markdown("---")
st.markdown(
    "<div style='text-align:center;color:#52746A;padding:15px;'>"
    "Fiber Science Lab Assistant | Textile Engineering | Second Year"
    "</div>",
    unsafe_allow_html=True
)i
