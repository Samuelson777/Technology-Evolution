import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
    }
    .section-title {
        font-size: 30px;
        font-weight: bold;
        color: #FFFFFF; /* Changed to white for better contrast in dark mode */
        background-color: #333; /* Added background color for contrast */
        padding: 10px; /* Added padding for better appearance */
        border-radius: 5px; /* Rounded corners */
        margin-top: 20px;
    }
    .description {
        font-size: 18px;
        color: #555;
        line-height: 1.5;
    }
    .fun-fact {
        font-size: 16px;
        color: #FF5722;
        font-style: italic;
    }
    .button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        text-align: center;
        display: inline-block;
        margin: 5px 0;
        transition: background-color 0.3s;
    }
    .button:hover {
        background-color: #45a049;
    }
    .tech-card {
        border: 1px solid #ccc;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        background-color: #f9f9f9;
    }
    @media (prefers-color-scheme: dark) {
        .section-title {
            color: #FFFFFF; /* Light color for dark mode */
            background-color: #333; /* Dark background for contrast */
        }
        .description {
            color: #FFFFFF; /* Light color for descriptions in dark mode */
        }
        .fun-fact {
            color: #FF5722; /* Keep fun fact color */
        }
        .tech-card {
            background-color: #444; /* Darker background for tech cards in dark mode */
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.markdown('<div class="title">Technology Evolution</div>', unsafe_allow_html=True)

# **Add Starting Image**
st.image("Tech.jpg", use_container_width=True)  # Updated parameter

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["Technologies", "Seasons"])

# Dictionary of technologies with detailed descriptions, fun facts, images, and resources
technologies = {
    1: {
        "name": "The Wheel",
        "description": "The wheel is one of the most important inventions in human history. It revolutionized transport and trade, enabling the movement of goods and people across vast distances.",
        "fun_fact": "Did you know? The wheel was invented over 5,000 years ago!",
        "image": "Wheel.png",
        "resource": "https://en.wikipedia.org/wiki/Wheel"
    },
    2: {
        "name": "The Printing Press",
        "description": "Invented by Johannes Gutenberg, the printing press allowed for the mass production of books, making literature accessible to the general public and sparking the Renaissance.",
        "fun_fact": "Fun Fact: The printing press made books cheaper and more accessible!",
        "image": "Press.png",
        "resource": "https://en.wikipedia.org/wiki/Printing_press"
    },
    3: {
        "name": "Electricity",
        "description": "Electricity powers our homes, schools, and industries, transforming the way we live. It is essential for modern technology, from lighting to computing.",
        "fun_fact": "Did you know? Electricity powers almost everything we use today!",
        "image": "Electricity.png",
        "resource": "https://en.wikipedia.org/wiki/Electricity"
    },
    4: {
        "name": "The Internet",
        "description": "The Internet connects millions of computers, allowing people to share information instantly. It has transformed communication, commerce, and entertainment.",
        "fun_fact": "Fun Fact: The Internet connects millions of people around the world!",
        "image": "Internet.png",
        "resource": "https://en.wikipedia.org/wiki/Internet"
    },
    5: {
        "name": "Artificial Intelligence",
        "description": "AI simulates human intelligence in machines, learning and making decisions. It is used in various applications, from virtual assistants to autonomous vehicles.",
        "fun_fact": "Did you know? AI can learn and make decisions like humans!",
        "image": "AI.png",
        "resource": "https://en.wikipedia.org/wiki/Artificial_intelligence"
    },
    6: {
        "name": "The Telephone",
        "description": "The telephone revolutionized communication, allowing people to talk to each other over long distances. It laid the foundation for modern telecommunications.",
        "fun_fact": "Did you know? The first successful telephone call was made by Alexander Graham Bell in 1876!",
        "image": "Telephone.png",
        "resource": "https://en.wikipedia.org/wiki/Telephone"
    },
    7: {
        "name": "The Computer",
        "description": "Computers have transformed the way we work and communicate, enabling complex calculations and data processing. They are integral to modern life.",
        "fun_fact": "Did you know? The first programmable computer was created in the 1930s!",
        "image": "Computer.png",
        "resource": "https://en.wikipedia.org/wiki/Computer"
    },
    8: {
        "name": "The Smartphone",
        "description": "Smartphones combine the functionality of a computer with mobile communication, changing how we interact with technology and each other.",
        "fun_fact": "Did you know? The first smartphone was released in 1992!",
        "image": "Smartphone.png",
        "resource": "https://en.wikipedia.org/wiki/Smartphone"
    },
    9: {
        "name": "Blockchain",
        "description": "Blockchain technology enables secure and transparent transactions, revolutionizing finance and data management. It is the backbone of cryptocurrencies.",
        "fun_fact": "Did you know? Bitcoin, the first cryptocurrency, was created in 2009 using blockchain technology!",
        "image": "Blockchain.png",
        "resource": "https://en.wikipedia.org/wiki/Blockchain"
    },
    10: {
        "name": "3D Printing",
        "description": "3D printing allows for the creation of three-dimensional objects from digital files, transforming manufacturing and enabling rapid prototyping.",
        "fun_fact": "Did you know? The first 3D printer was created in 1983!",
        "image": "3d_printing.png",
        "resource": "https://en.wikipedia.org/wiki/3D_printing"
    },
    11: {
        "name": "Renewable Energy",
        "description": "Renewable energy sources, such as solar and wind, provide sustainable alternatives to fossil fuels, helping to combat climate change.",
        "fun_fact": "Did you know? Solar energy is the most abundant energy source on Earth!",
        "image": "Renewableenergy.png",
        "resource": "https://en.wikipedia.org/wiki/Renewable_energy"
    },
    12: {
        "name": "Quantum Computing",
        "description": "Quantum computing uses the principles of quantum mechanics to process information in fundamentally different ways than classical computers.",
        "fun_fact": "Did you know? Quantum computers can solve certain problems much faster than classical computers!",
        "image": "quantumcomputing.png",
        "resource": "https://en.wikipedia.org/wiki/Quantum_computing"
    }
}

# Dictionary of seasonal events with descriptions, fun facts, technologies, and images
seasonal_events = {
    "Spring": {
        "description": "Spring is a season of renewal and growth.",
        "fun_fact": "Did you know? Spring is often associated with new beginnings.",
        "technologies": ["Agricultural Technology", "Renewable Energy"],
        "image": "spring.jpg"
    },
    "Summer": {
        "description": "Summer is the warmest season, marked by long days.",
        "fun_fact": "Did you know? The summer solstice occurs around June 21st.",
        "technologies": ["Cooling Systems", "Solar Energy"],
        "image": "summer.jpg"
    },
    "Autumn": {
        "description": "Autumn is a transitional season with cooler temperatures.",
        "fun_fact": "Did you know? The term 'fall' comes from the phrase 'fall of the leaves.'",
        "technologies": ["Harvesting Equipment", "Food Preservation"],
        "image": "fall.jpg"
    },
    "Winter": {
        "description": "Winter is the coldest season, characterized by snow.",
        "fun_fact": "Did you know? The coldest temperature ever recorded was -128.6°F in Antarctica.",
        "technologies": ["Heating Systems", "Winter Sports Equipment"],
        "image": "winter.jpg"
    }
}

# Function to display technology information
def display_technologies():
    st.markdown('<div class="section-title">Technologies</div>', unsafe_allow_html=True)
    st.write("Gather resources and learn about various technologies that evolved throughout history!")
    
    # Display technology details
    for tech_id, tech_info in technologies.items():
        st.markdown(f"<div class='tech-card'><h3>{tech_info['name']}</h3><div class='description'>{tech_info['description']}</div><div class='fun-fact'>{tech_info['fun_fact']}</div>", unsafe_allow_html=True)
        st.image(tech_info['image'], use_container_width=True)  # Updated parameter
        st.markdown(f"<a href='{tech_info['resource']}' target='_blank' class='button'>Learn More</a></div>", unsafe_allow_html=True)

# Function to display seasonal events
def display_seasons():
    st.markdown('<div class="section-title">Seasonal Events</div>', unsafe_allow_html=True)
    st.write("Explore seasonal challenges and learn about technologies related to each season!")

    # Display current seasonal event
    current_season = st.selectbox("Select a season:", list(seasonal_events.keys()))
    event = seasonal_events[current_season]
    
    st.write(f"**{current_season} Event**: {event['description']}")
    st.write(f"**Fun Fact**: {event['fun_fact']}")
    st.write("**Related Technologies**:")
    for tech in event['technologies']:
        st.write(f"- {tech}")
    st.image(event['image'], use_container_width=True)  # Updated parameter

# Main logic to display the selected page
if page == "Technologies":
    display_technologies()
elif page == "Seasons":
    display_seasons()

# Regular content updates
def update_content():
    st.write("New technologies and resources have been added! Check back often for updates.")

update_content()

# Final message to players
st.write("Thank you for exploring Technology Evolution! Keep learning about the amazing world of technology.")
