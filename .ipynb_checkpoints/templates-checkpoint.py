from IPython.display import HTML, display

def info_box(content):
    display(HTML(f"""
    <div style="
        border: 2px solid #28a745; 
        border-radius: 8px; 
        padding: 20px; 
        margin: 10px 0; 
        background-color: #f8fff9; 
        position: relative;
        max-width: 100%;
        box-sizing: border-box;
    ">
        <div style="
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
        ">i</div>
        <div style="color: #155724; font-size: 1.1em; line-height: 1.5;">
            {content}
        </div>
    </div>
    """))