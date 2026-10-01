"""
styles.py
---------
Modern ChatGPT UI Theme
"""

import streamlit as st


def load_css():

    st.markdown(
        """
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');


/* ==========================================================
   GLOBAL
========================================================== */

html,
body,
[class*="css"]{

    font-family:'Inter',sans-serif;

}

*{

    margin:0;

    padding:0;

    box-sizing:border-box;

}

.stApp{

    background:
        radial-gradient(circle at top right,
            rgba(37,99,235,.14),
            transparent 30%),

        radial-gradient(circle at bottom left,
            rgba(16,185,129,.10),
            transparent 25%),

        #0F172A;

    color:#F8FAFC;

}


/* ==========================================================
   MAIN LAYOUT
========================================================== */

.main .block-container{

    max-width:1200px;

    padding-top:1.2rem;

    padding-bottom:2rem;

    padding-left:2rem;

    padding-right:2rem;

}


/* ==========================================================
   SIDEBAR
========================================================== */

[data-testid="stSidebar"]{

    background:#111827;

    border-right:1px solid #1F2937;

}

[data-testid="stSidebar"] .block-container{

    padding-top:1.2rem;

}


/* ==========================================================
   SIDEBAR HEADER
========================================================== */

.sidebar-header{

    margin-bottom:18px;

}

.sidebar-header h2{

    color:#FFFFFF;

    font-size:24px;

    font-weight:700;

    margin-bottom:4px;

}

.sidebar-header p{

    color:#94A3B8;

    font-size:13px;

}


/* ==========================================================
   SEARCH BOX
========================================================== */

input[type="text"]{

    background:#1E293B !important;

    border:1px solid #334155 !important;

    color:#FFFFFF !important;

    border-radius:12px !important;

}

input[type="text"]:focus{

    border-color:#3B82F6 !important;

    box-shadow:0 0 0 2px rgba(59,130,246,.25);

}


/* ==========================================================
   BUTTONS
========================================================== */

.stButton>button{

    width:100%;

    border:none;

    border-radius:12px;

    background:#2563EB;

    color:#FFFFFF;

    font-weight:600;

    padding:.72rem;

    transition:.22s ease;

}

.stButton>button:hover{

    background:#1D4ED8;

    transform:translateY(-2px);

    box-shadow:0 10px 24px rgba(37,99,235,.30);

}

.stButton>button:active{

    transform:scale(.98);

}


/* ==========================================================
   DOWNLOAD BUTTONS
========================================================== */

.stDownloadButton>button{

    width:100%;

    border-radius:12px;

    background:#111827;

    color:#FFFFFF;

    border:1px solid #334155;

}

.stDownloadButton>button:hover{

    background:#1E40AF;

    border-color:#3B82F6;

}


/* ==========================================================
   CHAT HEADER
========================================================== */

.chat-header{

    display:flex;

    justify-content:space-between;

    align-items:center;

    margin-bottom:28px;

    padding-bottom:18px;

    border-bottom:1px solid rgba(255,255,255,.08);

}

.chat-header-left h2{

    color:#FFFFFF;

    font-size:30px;

    font-weight:700;

    margin-bottom:4px;

}

.chat-header-left p{

    color:#94A3B8;

    font-size:15px;

}


/* ==========================================================
   ONLINE STATUS
========================================================== */

.status-online{

    background:rgba(34,197,94,.12);

    color:#22C55E;

    border:1px solid rgba(34,197,94,.22);

    border-radius:999px;

    padding:8px 16px;

    font-size:13px;

    font-weight:600;

}

/* ==========================================================
   WELCOME SCREEN
========================================================== */

.welcome-container{

    display:flex;

    flex-direction:column;

    justify-content:center;

    align-items:center;

    text-align:center;

    padding:3rem 1rem 2rem;

    animation:fadeIn .4s ease;

}

.welcome-title{

    font-size:42px;

    font-weight:800;

    color:#FFFFFF;

    margin-bottom:12px;

    line-height:1.2;

}

.welcome-subtitle{

    max-width:700px;

    color:#94A3B8;

    font-size:17px;

    line-height:1.8;

    margin-bottom:30px;

}


/* ==========================================================
   QUICK ACTIONS
========================================================== */

.quick-actions{

    display:grid;

    grid-template-columns:repeat(3,1fr);

    gap:14px;

    width:100%;

    max-width:850px;

}


/* ==========================================================
   CHAT AREA
========================================================== */

[data-testid="stChatMessage"]{

    background:#111827;

    border:1px solid rgba(255,255,255,.06);

    border-radius:18px;

    padding:16px;

    margin-bottom:16px;

    transition:.2s ease;

}

[data-testid="stChatMessage"]:hover{

    border-color:#3B82F6;

    box-shadow:0 8px 20px rgba(0,0,0,.18);

}


/* ==========================================================
   USER MESSAGE
========================================================== */

div[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]){

    background:#1E293B;

    border-color:#334155;

}


/* ==========================================================
   ASSISTANT MESSAGE
========================================================== */

div[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]){

    background:#111827;

    border-color:#1F2937;

}


/* ==========================================================
   CHAT TYPOGRAPHY
========================================================== */

[data-testid="stChatMessage"] p{

    color:#F8FAFC;

    font-size:15px;

    line-height:1.8;

}

[data-testid="stChatMessage"] ul{

    padding-left:22px;

}

[data-testid="stChatMessage"] li{

    margin-bottom:8px;

}


/* ==========================================================
   CODE BLOCKS
========================================================== */

[data-testid="stMarkdownContainer"] pre{

    background:#0B1220;

    border:1px solid #334155;

    border-radius:12px;

    padding:14px;

    overflow:auto;

}

[data-testid="stMarkdownContainer"] code{

    font-size:14px;

}


/* ==========================================================
   CHAT INPUT
========================================================== */

[data-testid="stChatInput"]{

    margin-top:20px;

}

[data-testid="stChatInput"] textarea{

    background:#111827 !important;

    border:1px solid #334155 !important;

    border-radius:18px !important;

    color:#F8FAFC !important;

    font-size:15px;

    padding:14px !important;

    resize:none;

}

[data-testid="stChatInput"] textarea:focus{

    border-color:#3B82F6 !important;

    box-shadow:0 0 0 2px rgba(59,130,246,.25);

}


/* ==========================================================
   SPINNER
========================================================== */

[data-testid="stSpinner"]{

    color:#60A5FA;

}


/* ==========================================================
   ALERTS
========================================================== */

[data-testid="stAlert"]{

    border-radius:12px;

}


/* ==========================================================
   DIVIDERS
========================================================== */

hr{

    border:none;

    border-top:1px solid rgba(255,255,255,.08);

    margin:18px 0;

}


/* ==========================================================
   DOWNLOAD BUTTONS
========================================================== */

.stDownloadButton{

    margin-bottom:10px;

}
/* ==========================================================
   METRIC CARDS
========================================================== */

[data-testid="metric-container"]{

    background:#1E293B;

    border:1px solid #334155;

    border-radius:14px;

    padding:14px;

    transition:.25s ease;

}

[data-testid="metric-container"]:hover{

    border-color:#3B82F6;

    transform:translateY(-2px);

}


/* ==========================================================
   EXPANDERS
========================================================== */

.streamlit-expanderHeader{

    border-radius:12px;

    font-weight:600;

}


/* ==========================================================
   LINKS
========================================================== */

a{

    color:#60A5FA;

    text-decoration:none;

}

a:hover{

    color:#93C5FD;

    text-decoration:underline;

}


/* ==========================================================
   TEXT SELECTION
========================================================== */

::selection{

    background:#2563EB;

    color:#FFFFFF;

}


/* ==========================================================
   SCROLLBAR
========================================================== */

::-webkit-scrollbar{

    width:10px;

    height:10px;

}

::-webkit-scrollbar-track{

    background:#0F172A;

}

::-webkit-scrollbar-thumb{

    background:#334155;

    border-radius:999px;

}

::-webkit-scrollbar-thumb:hover{

    background:#3B82F6;

}


/* ==========================================================
   ANIMATIONS
========================================================== */

@keyframes fadeIn{

    from{

        opacity:0;

    }

    to{

        opacity:1;

    }

}

@keyframes fadeInUp{

    from{

        opacity:0;

        transform:translateY(10px);

    }

    to{

        opacity:1;

        transform:translateY(0);

    }

}

.block-container{

    animation:fadeIn .35s ease;

}

[data-testid="stChatMessage"]{

    animation:fadeInUp .25s ease;

}


/* ==========================================================
   CHATGPT-LIKE SPACING
========================================================== */

[data-testid="stVerticalBlock"]{

    gap:.5rem;

}

[data-testid="stHorizontalBlock"]{

    gap:.75rem;

}


/* ==========================================================
   MOBILE RESPONSIVE
========================================================== */

@media (max-width:992px){

.main .block-container{

    padding:1rem;

}

.chat-header{

    flex-direction:column;

    align-items:flex-start;

    gap:14px;

}

.chat-header-left h2{

    font-size:26px;

}

.status-online{

    align-self:flex-start;

}

.quick-actions{

    grid-template-columns:1fr;

}

.welcome-title{

    font-size:34px;

}

.welcome-subtitle{

    font-size:15px;

}

}

@media (max-width:768px){

.welcome-container{

    padding:2rem 0;

}

.welcome-title{

    font-size:28px;

}

.welcome-subtitle{

    font-size:14px;

    padding:0 8px;

}

[data-testid="stChatMessage"]{

    padding:12px;

}

[data-testid="stChatInput"] textarea{

    font-size:14px;

}

}


/* ==========================================================
   HIDE STREAMLIT DEFAULT ELEMENTS
========================================================== */

#MainMenu{

    visibility:hidden;

}

footer{

    visibility:hidden;

}


/* ==========================================================
   FINAL POLISH
========================================================== */

.stButton>button{

    box-shadow:0 8px 22px rgba(37,99,235,.20);

}

.stDownloadButton>button{

    box-shadow:0 6px 18px rgba(0,0,0,.18);

}

.stButton>button:focus,
.stDownloadButton>button:focus{

    outline:none;

}

</style>
""",
        unsafe_allow_html=True,
    )