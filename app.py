import streamlit as st
import pandas as pd
import time
import os

# 1. Page Configuration
st.set_page_config( 
    page_title="HostelMate AI – Smart Student Housing Platform",
    page_icon="🏠",
    layout="wide"
)

# Inject Clean Custom UI Card and Typography Overrides
st.markdown("""
    <style>
    /* Premium property item visual cards styling */
    .property-card {
        background-color: #ffffff;
        border: 1px solid #eef2f6;
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .property-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.02);
    }
    /* Clean custom badge layouts */
    .amenity-tag {
        background-color: #f1f5f9;
        color: #475569;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 13px;
        font-weight: 500;
        display: inline-block;
        margin-right: 6px;
        margin-bottom: 6px;
    }
    /* Metric container blocks */
    .metric-container {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Helper function to pinpoint file absolute paths safely
def get_csv_path():
    current_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_folder, "rooms.csv")

# Safe rerun wrapper to handle all Streamlit versions cleanly
def safe_rerun():
    try:
        st.rerun()
    except AttributeError:
        st.experimental_rerun()

# 2. Dynamic CSV Data Loading Engine & State Session Manager
def load_all_listings():
    try:
        file_path = get_csv_path()
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            # Force rent values to numeric type safely
            df['rent'] = pd.to_numeric(df['rent'], errors='coerce').fillna(0).astype(int)
            return df
        else:
            return pd.DataFrame(columns=['name', 'type', 'state', 'city', 'rent', 'distance', 'facilities', 'description', 'contact'])
    except Exception as e:
        st.error(f"System Error Loading CSV: {str(e)}")
        return pd.DataFrame(columns=['name', 'type', 'state', 'city', 'rent', 'distance', 'facilities', 'description', 'contact'])

if "df_rooms" not in st.session_state:
    st.session_state.df_rooms = load_all_listings()

df_rooms = st.session_state.df_rooms

selected_state = "Not Selected"
selected_city = "Not Selected"
final_filtered_df = pd.DataFrame()

# =========================================================================
# 3. SIDEBAR LAYOUT
# =========================================================================
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #4F8BF9; font-weight: 800; margin-bottom: 0;'>HostelMate AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 13px; color: #64748b; margin-bottom: 25px;'>Smart Student Housing Ecosystem</p>", unsafe_allow_html=True)
    
    st.markdown("<p style='font-size: 16px; font-weight: 700; color: #1e293b; margin-bottom: 10px;'>Navigation</p>", unsafe_allow_html=True)
    menu = st.radio(
        "Go to Screen:",
        ["Home & Explore", "AI Assistant Agent", "Owner Dashboard"],
        label_visibility="collapsed"
    )
    st.markdown("<br>", unsafe_allow_html=True)
    
    if menu == "Home & Explore" and not df_rooms.empty:
        st.markdown("<p style='font-size: 14px; font-weight: 700; color: #1e293b; margin-bottom: 5px;'>Active Context</p>", unsafe_allow_html=True)
        st.info("Tip: Combine your drop-down region selection with our text search to filter items instantly.")
    elif menu == "AI Assistant Agent":
        st.markdown("<p style='font-size: 14px; font-weight: 700; color: #1e293b; margin-bottom: 5px;'>Agent Insights</p>", unsafe_allow_html=True)
        st.success("Status: Ready to Match")
    elif menu == "Owner Dashboard":
        st.markdown("<p style='font-size: 14px; font-weight: 700; color: #1e293b; margin-bottom: 5px;'>Host Console</p>", unsafe_allow_html=True)
        st.info("Note: Submissions append instantly to database memory structures and sync directly to local storage matrices.")
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("<p style='font-size: 14px; font-weight: 700; color: #1e293b; margin-bottom: 5px;'>System Status</p>", unsafe_allow_html=True)
    if not df_rooms.empty:
        st.success("Database Connection: Online")
        st.markdown(f"Total Dataset: `{len(df_rooms)}` verified listings")
    else:
        st.error("Database Connection: Offline")
        st.markdown("Total Dataset: `0` available")
        
    st.markdown("<br><hr>", unsafe_allow_html=True)
   
    st.markdown("<p style='font-size: 11px; color: #94a3b8; text-align: center;'>Designed for Students</p>", unsafe_allow_html=True)

# Verify data exists before rendering application screens
if df_rooms.empty and menu != "Owner Dashboard":
    st.warning("Please resolve the CSV file issue or check the error message above to view the platform layouts.")
else:
    # -------------------------------------------------------------------------
    # SCREEN 1: HOME & EXPLORE
    # -------------------------------------------------------------------------
    if menu == "Home & Explore":
        
        # 🌟 Sleek, built-in CSS Home Icon Layout (No external image file needed!)
        st.markdown("""
            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 5px;">
                <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); 
                            padding: 12px; border-radius: 12px; display: flex; align-items: center; justify-content: center;
                            box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);">
                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                        <polyline points="9 22 9 12 15 12 15 22"></polyline>
                    </svg>
                </div>
                <div>
                    <h1 style='font-weight: 800; color: #1e293b; margin: 0;'>HostelMate AI</h1>
                    <p style='font-size: 14px; color: #64748b; margin: 0;'>Verified Student Housing Ecosystem</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<p style='font-size: 16px; color: #64748b; margin-top: 5px;'>Find perfect student accommodations using smart, localized data mapping.</p>", unsafe_allow_html=True)
        st.markdown("---")
        # Micro Dashboard Market Figures Layout
        stat_col1, stat_col2, stat_col3 = st.columns(3)
        with stat_col1:
            st.markdown(f"""<div class='metric-container'>
                <p style='margin:0; font-size:14px; color:#64748b; font-weight:600; text-transform:uppercase;'>Verified Listings</p>
                <p style='margin:5px 0 0 0; font-size:28px; color:#1e293b; font-weight:700;'>{len(df_rooms)}+ Properties</p>
            </div>""", unsafe_allow_html=True)
        with stat_col2:
            min_rent = int(df_rooms['rent'].min()) if not df_rooms.empty else 0
            st.markdown(f"""<div class='metric-container'>
                <p style='margin:0; font-size:14px; color:#64748b; font-weight:600; text-transform:uppercase;'>Starting Price</p>
                <p style='margin:5px 0 0 0; font-size:28px; color:#10b981; font-weight:700;'>₹{min_rent:,}/mo</p>
            </div>""", unsafe_allow_html=True)
        with stat_col3:
            avg_rent = int(df_rooms['rent'].mean()) if not df_rooms.empty else 0
            st.markdown(f"""<div class='metric-container'>
                <p style='margin:0; font-size:14px; color:#64748b; font-weight:600; text-transform:uppercase;'>Market Average</p>
                <p style='margin:5px 0 0 0; font-size:28px; color:#3b82f6; font-weight:700;'>₹{avg_rent:,}/mo</p>
            </div>""", unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Interactive Regional Filter Component Block
        st.markdown("<p style='font-size: 20px; font-weight: 700; color: #1e293b; margin-bottom: 10px;'>Filter Accommodations</p>", unsafe_allow_html=True)
        with st.container():
            filter_col1, filter_col2 = st.columns(2)
            with filter_col1:
                states_list = sorted(df_rooms['state'].dropna().unique()) if not df_rooms.empty else []
                selected_state = st.selectbox("Target State", states_list if states_list else ["No Data"])
            with filter_col2:
                state_filtered_df = df_rooms[df_rooms['state'] == selected_state] if not df_rooms.empty else pd.DataFrame()
                cities_list = sorted(state_filtered_df['city'].dropna().unique()) if not state_filtered_df.empty else []
                selected_city = st.selectbox("Targeted City", cities_list if cities_list else ["No Data"])
        
        search_query = st.text_input("Keyword Search (e.g., 'AC', 'Wifi', 'Girls', 'Boys', 'Near Campus')", placeholder="Type here to narrow properties down by facilities or descriptions...")
                
        if not df_rooms.empty and selected_city != "No Data":
            final_filtered_df = state_filtered_df[state_filtered_df['city'] == selected_city]
            
            if search_query:
                q = search_query.lower()
                final_filtered_df = final_filtered_df[
                    final_filtered_df['name'].str.lower().str.contains(q, na=False) |
                    final_filtered_df['facilities'].str.lower().str.contains(q, na=False) |
                    final_filtered_df['description'].str.lower().str.contains(q, na=False)
                ]
        else:
            final_filtered_df = pd.DataFrame()
        
        st.markdown(f"<p style='font-size: 18px; font-weight: 700; color: #1e293b; margin-top: 20px;'>Matching Results ({len(final_filtered_df)} items discovered)</p>", unsafe_allow_html=True)
        
        if final_filtered_df.empty:
            st.info("No verified student properties match your specific parameters.")
        else:
            for _, row in final_filtered_df.iterrows():
                p_name = str(row['name'])
                p_type = str(row['type'])
                p_dist = str(row['distance'])
                p_desc = str(row['description'])
                p_contact = str(row['contact'])
                p_rent = int(row['rent'])
                
                card_html = f"""
                <div class="property-card">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap;">
                        <div style="flex: 3; min-width: 300px;">
                            <span style="background-color: #e0f2fe; color: #0369a1; font-size: 11px; font-weight: 700; padding: 4px 8px; border-radius: 4px; text-transform: uppercase; letter-spacing: 0.5px;">{p_type}</span>
                            <h3 style="margin: 8px 0 4px 0; color: #1e293b; font-weight: 700;">{p_name}</h3>
                            <p style="color: #64748b; font-size: 14px; margin-bottom: 12px;"><b>Campus Proximity:</b> {p_dist}</p>
                            <p style="color: #334155; font-size: 15px; line-height: 1.5; margin-bottom: 16px;">{p_desc}</p>
                            <div style="margin-top: 10px;">
                """
                
                facilities_field = str(row['facilities']) if pd.notna(row['facilities']) else "Standard"
                for facility in facilities_field.split(','):
                    card_html += f'<span class="amenity-tag">{facility.strip()}</span>'
                
                card_html += f"""
                            </div>
                        </div>
                        <div style="flex: 1; min-width: 200px; background-color: #f8fafc; border-left: 4px solid #4F8BF9; padding: 16px; border-radius: 0 8px 8px 0; text-align: right; box-sizing: border-box;">
                            <p style="margin: 0; font-size: 13px; color: #64748b; font-weight: 500;">Monthly Value</p>
                            <h2 style="margin: 0 0 10px 0; color: #1e293b; font-weight: 800; font-size: 26px;">₹{p_rent:,}</h2>
                            <span style="background-color: #dcfce7; color: #15803d; font-size: 12px; font-weight: 600; padding: 6px 12px; border-radius: 20px; display: inline-block; margin-bottom: 10px;">Direct Listing</span>
                            <p style="margin: 5px 0 0 0; font-size: 13px; color: #475569; font-weight: 600; font-family: monospace;">Contact: {p_contact}</p>
                        </div>
                    </div>
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)

    # -------------------------------------------------------------------------
    # SCREEN 2: AI CHATBOT (FREE GROQ LLM AGENT)
    
    elif menu == "AI Assistant Agent":
        # 🌟 Beautiful custom layout containing a sleek, styled AI badge and header
        st.markdown("""
            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 5px;">
                <div style="background: linear-gradient(135deg, #4F8BF9 0%, #3b82f6 100%); 
                            padding: 12px; border-radius: 12px; display: flex; align-items: center; justify-content: center;
                            box-shadow: 0 4px 12px rgba(79, 139, 249, 0.3);">
                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M12 8V4H8"></path>
                        <rect width="16" height="12" x="4" y="8" rx="2"></rect>
                        <path d="M2 14h2"></path>
                        <path d="M20 14h2"></path>
                        <path d="M15 13v2"></path>
                        <path d="M9 13v2"></path>
                    </svg>
                </div>
                <div>
                    <h1 style='font-weight: 800; color: #1e293b; margin: 0;'>Ask HostelMate AI</h1>
                    <p style='font-size: 14px; color: #64748b; margin: 0;'>Intelligent Agent Sandbox Matrix</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<p style='font-size: 16px; color: #64748b; margin-top: 5px;'>Powered by LangGraph Orchestration & Free Groq Llama-3</p>", unsafe_allow_html=True)
        st.markdown("---")

        # Imports
        from langchain_groq import ChatGroq
        from langchain_core.tools import tool
        from langgraph.prebuilt import create_react_agent
        from langchain_core.messages import AIMessage, HumanMessage
        import json

        # Define the database search tool
        @tool
        def query_accommodation_database(criteria_keyword: str = "", max_budget: int = None) -> str:
            """
            Queries the local student accommodation database. 
            Use this tool whenever a student asks to find, list, or look up rooms, hostels, PGs, or flats.
            You can pass a keyword (like a city name, 'Wifi', 'AC', 'Girls') and an optional max_budget ceiling integer.
            """
            df = load_all_listings()
            if df.empty:
                return "The room database is currently empty."
            
            if max_budget:
                df = df[df['rent'] <= max_budget]
                
            if criteria_keyword:
                q = criteria_keyword.lower()
                df = df[
                    df['name'].str.lower().str.contains(q, na=False) |
                    df['facilities'].str.lower().str.contains(q, na=False) |
                    df['description'].str.lower().str.contains(q, na=False) |
                    df['city'].str.lower().str.contains(q, na=False) |
                    df['state'].str.lower().str.contains(q, na=False)
                ]
            
            if df.empty:
                return "No properties found matching those parameters."
            return df.to_json(orient="records")

        tools = [query_accommodation_database]

        # Initialize the Brain & Agent Engine safely using GROQ configuration
        try:
            if "GROQ_API_KEY" in st.secrets:
                api_key = st.secrets["GROQ_API_KEY"]
            else:
                api_key = os.environ.get("GROQ_API_KEY") 
            
            if not api_key:
                st.error("API Key missing! Please configure GROQ_API_KEY inside your .streamlit/secrets.toml file.")
                st.stop()
            
            # Integrated Free Meta Llama 3 model via Groq Engine
            llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0, groq_api_key=api_key)
            
            # 🌟 SYSTEM INSTRUCTION UPDATE: Allowed casual banter & friendly chatter
            system_instruction = """You are a professional, friendly, and highly helpful student housing AI agent for 'HostelMate AI'. 
            
            CRITICAL BEHAVIOR:
            1. If the user says hello, hi, greets you, or asks casual questions, respond warmly and politely as a friendly assistant. You do NOT need to call a tool for general chit-chat or greetings.
            2. Whenever a student asks to find, look up, or suggest real rooms/hostels/PGs, you MUST use the 'query_accommodation_database' tool to get accurate data.
            
            When presenting properties found in the database:
            - Use bullet points or bold titles.
            - Explicitly state the rent price (₹) and owner contact information."""
            
            agent_modifier = create_react_agent(llm, tools, prompt=system_instruction)
        except Exception as e:
            st.error(f"Could not initialize Groq Model. Details: {str(e)}")
            st.stop()

        # Streamlit Chat Interface Memory State
        if "agent_chat_history" not in st.session_state:
            st.session_state.agent_chat_history = []
            st.session_state.display_messages = [
                {"role": "assistant", "content": "Hi there! I am your updated free AI Agent. I can interpret budgets and find rooms across our entire registry. Try asking me: 'Show me places in Mumbai under ₹10,000'!"}
            ]

        # UI Enhancement: One-Click Quick Suggestion Buttons for Students
        st.markdown("<p style='font-size: 14px; font-weight: 600; color: #475569; margin-bottom: 5px;'>Quick Suggestions:</p>", unsafe_allow_html=True)
        sug_col1, sug_col2, sug_col3 = st.columns(3)
        
        suggested_query = None
        with sug_col1:
            if st.button("🔍 Options under ₹10,000", use_container_width=True):
                suggested_query = "Show me student housing places under 10000 rupees"
        with sug_col2:
            if st.button("🚶 Accommodations with Wi-Fi", use_container_width=True):
                suggested_query = "Find me student rooms that have Wifi"
        with sug_col3:
            if st.button("🏠 View all listings", use_container_width=True):
                suggested_query = "What verified properties do you have right now?"

        # Display history logs
        for msg in st.session_state.display_messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        # Chat Input & Processing Execution Loop
        user_input = st.chat_input("Ask the agent to scan your housing database...")
        
        if suggested_query:
            user_input = suggested_query

        if user_input:
            # Display user message instantly on the UI
            with st.chat_message("user"):
                st.markdown(user_input)
            
            st.session_state.display_messages.append({"role": "user", "content": user_input})

            with st.chat_message("assistant"):
                with st.spinner("Agent is thinking..."):
                    try:
                        # Append as an explicit HumanMessage class object for LangGraph
                        st.session_state.agent_chat_history.append(HumanMessage(content=user_input))
                        
                        # Run through the LangGraph engine safely
                        response = agent_modifier.invoke({"messages": st.session_state.agent_chat_history})
                        
                        # 🌟 ROBUST FALLBACK PROCESSING FOR CASUAL TALK
                        if isinstance(response, dict) and "messages" in response:
                            agent_output = response["messages"][-1].content
                        elif hasattr(response, "content"):
                            agent_output = response.content
                        else:
                            agent_output = str(response)

                        # Render response beautifully
                        st.markdown(agent_output)
                        
                        # Update back to memory arrays cleanly
                        st.session_state.agent_chat_history.append(AIMessage(content=agent_output))
                        st.session_state.display_messages.append({"role": "assistant", "content": agent_output})
                        
                    except Exception as loop_err:
                        st.error(f"Agent Engine Error: {str(loop_err)}")
            
            if suggested_query:
                time.sleep(0.1)
                safe_rerun()

    # -------------------------------------------------------------------------
    # SCREEN 3: OWNER DASHBOARD
    # -------------------------------------------------------------------------
    elif menu == "Owner Dashboard":
        st.markdown("<h1 style='font-weight: 800; color: #1e293b;'>Property Owner Center</h1>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px; color: #64748b; margin-top: -15px;'>Upload rental assets, manage active market slots, and view structural diagnostics.</p>", unsafe_allow_html=True)
        st.markdown("---")
        
        tab_upload, tab_manage = st.tabs(["Add New Property", "Manage Active Listings"])
        
        with tab_upload:
            st.markdown("<p style='font-size: 18px; font-weight: 700; color: #1e293b;'>Create Accommodation Entry</p>", unsafe_allow_html=True)
            
            with st.form("owner_upload_form", clear_on_submit=True):
                col_f1, col_f2 = st.columns(2)
                
                with col_f1:
                    prop_name = st.text_input("Property Name / Identity Title*", placeholder="e.g., Starlight Premium Student Living")
                    prop_type = st.selectbox("Accommodation Variant", ["Hostel", "PG", "1 BHK Flat", "2 BHK Flat", "Shared Room"])
                    prop_state = st.text_input("Target State*", placeholder="e.g., Maharashtra")
                    prop_city = st.text_input("Target City*", placeholder="e.g., Mumbai")
                    prop_rent = st.number_input("Complete Monthly Rent (₹)*", min_value=500, value=6500, step=500)
                
                with col_f2:
                    prop_dist = st.text_input("Campus Distance Parameter", placeholder="e.g., 200m from IIT Main Gate")
                    prop_facilities = st.text_input("Facilities (Comma Separated Keychains)", placeholder="Wi-Fi, Laundry, Gym, Veg Food")
                    prop_contact = st.text_input("Owner Contact Secure Hotline*", placeholder="e.g., +91 99999 88888")
                    prop_desc = st.text_area("Public Marketing Description", placeholder="Enter specific flat terms, dynamic environment aspects, or roommate rules...")
                
                st.markdown("<p style='color: #64748b; font-size:12px;'>* Represents an essential requirement field indicator.</p>", unsafe_allow_html=True)
                submit_button = st.form_submit_button("Deploy Asset to Live Directory")
                
                if submit_button:
                    if prop_name and prop_state and prop_city and prop_contact:
                        new_room = {
                            'name': prop_name,
                            'type': prop_type,
                            'state': prop_state.strip(),
                            'city': prop_city.strip(),
                            'rent': int(prop_rent),
                            'distance': prop_dist if prop_dist else "Contact Owner",
                            'facilities': prop_facilities if prop_facilities else "Standard Amenities",
                            'description': prop_desc if prop_desc else "No primary text shared by landlord.",
                            'contact': prop_contact
                        }
                        
                        st.session_state.df_rooms = pd.concat([st.session_state.df_rooms, pd.DataFrame([new_room])], ignore_index=True)
                        
                        try:
                            st.session_state.df_rooms.to_csv(get_csv_path(), index=False)
                            st.success(f"Success! '{prop_name}' has been written to rooms.csv and updated live.")
                        except Exception as csv_err:
                            st.warning(f"Appended to temporary variables, but file sync failed: {str(csv_err)}")
                            
                        time.sleep(0.5)
                        safe_rerun()
                    else:
                        st.error("Submission Blocked: Please complete all mandatory fields to deploy structural indexing.")

        with tab_manage:
            st.markdown("<p style='font-size: 18px; font-weight: 700; color: #1e293b;'>Active Operational Database Logs</p>", unsafe_allow_html=True)
            
            if st.session_state.df_rooms.empty:
                st.info("No items active within localized data structures.")
            else:
                st.dataframe(st.session_state.df_rooms, use_container_width=True)
                
                st.markdown("<br><hr>", unsafe_allow_html=True)
                st.markdown("<p style='font-size: 18px; font-weight: 700; color: #1e293b;'>Unlist Property From Platform Matrix</p>", unsafe_allow_html=True)
                
                listings_names = st.session_state.df_rooms['name'].tolist()
                selected_remove_target = st.selectbox("Select Target Unit to Purge:", listings_names)
                
                if st.button("Terminate Marketplace Listing", type="primary"):
                    target_index = st.session_state.df_rooms[st.session_state.df_rooms['name'] == selected_remove_target].index[0]
                    st.session_state.df_rooms = st.session_state.df_rooms.drop(target_index).reset_index(drop=True)
                    
                    try:
                        st.session_state.df_rooms.to_csv(get_csv_path(), index=False)
                        st.warning(f"System updated: '{selected_remove_target}' has been wiped from rooms.csv successfully.")
                    except Exception as csv_err:
                        st.error(f"Memory trace discarded but file save state failed: {str(csv_err)}")
                        
                    time.sleep(0.5)
                    safe_rerun()