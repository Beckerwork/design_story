from IPython.display import HTML, display

def load_styles():
    display(HTML("""
    <style>
    .info-box {
        border: 2px solid #28a745; 
        border-radius: 8px; 
        padding: 20px; 
        margin: 10px 0; 
        background-color: #f8fff9; 
        position: relative;
        max-width: 100%;
        box-sizing: border-box;
        color: #155724;
        font-size: 1.1em;
        line-height: 1.5;
    }
    .info-box-badge {
        position: absolute;
        top: -12px;
        left: 15px;
        background-color: #28a745;
        color: white;
        width: 24px;
        height: 24px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: serif;
        font-weight: bold;
        font-style: italic;
        font-size: 1rem;
    }
    .next-button-container {
        text-align: center;
        margin-top: 20px;
    }
    .next-button {
        display: inline-block;
        background-color: #f8fff9;
        color: #28a745 !important;
        padding: 10px 30px;
        border-radius: 12px;
        border: 2px solid #28a745;
        text-decoration: none;
        font-weight: bold;
        font-size: 1em;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
        transition: box-shadow 0.2s ease;
    }
    .next-button:hover {
        box-shadow: 0 6px 14px rgba(0, 0, 0, 0.25);
    }
     </style>
    """))

def load_styles2():
    display(HTML("""
    <style>
    .info-box2 {
        border: 2px solid #28a745; 
        border-radius: 8px; 
        padding: 20px; 
        margin: 10px 0; 
        background-color: #f8fff9; 
        position: relative;
        max-width: 100%;
        box-sizing: border-box;
    }
    .info-box2::before {
        content: "i";
        position: absolute;
        top: -12px;
        left: 15px;
        background-color: #28a745;
        color: white;
        width: 24px;
        height: 24px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: serif;
        font-weight: bold;
        font-style: italic;
    }
    </style>
    """))

