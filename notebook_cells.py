from IPython.display import HTML, display

# ─────────────────────────────────────────────────────────────
#  SETUP  —  call once at the top of your notebook
#  Loads Bootstrap + Font Awesome (works in BinderHub, VS Code,
#  JupyterLab, and classic Jupyter)
# ─────────────────────────────────────────────────────────────

def setup():
    display(HTML("""
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <link rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
    /* ── Shared base ─────────────────────────────────────── */
    .nc-cell {
        border-radius: 10px;
        padding: 20px 24px;
        margin: 12px 0;
        position: relative;
        font-size: 1em;
        line-height: 1.7;
    }
    .nc-cell .nc-badge {
        position: absolute;
        top: -13px;
        left: 16px;
        padding: 2px 14px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.8em;
        letter-spacing: 0.4px;
        color: white;
    }
    .nc-cell .nc-body {
        margin-top: 6px;
    }
    .nc-cell h4, .nc-cell h5 {
        margin-bottom: 10px;
    }

    /* ── Story / Information ─────────────────────────────── */
    .nc-story {
        background-color: #f0f9f1;
        border: 2px solid #28a745;
        color: #1a3d23;
    }
    .nc-story .nc-badge { background-color: #28a745; }

    /* ── Exercise ────────────────────────────────────────── */
    .nc-exercise {
        background-color: #f0f4ff;
        border: 2px solid #0d6efd;
        color: #0a2366;
    }
    .nc-exercise .nc-badge { background-color: #0d6efd; }

    /* ── Hint ────────────────────────────────────────────── */
    .nc-hint {
        background-color: #fffdf0;
        border: 2px solid #ffc107;
        color: #4d3c00;
    }
    .nc-hint .nc-badge { background-color: #ffc107; color: #4d3c00; }
    .nc-hint summary {
        cursor: pointer;
        font-weight: bold;
        list-style: none;
        color: #7a5c00;
    }
    .nc-hint summary::-webkit-details-marker { display: none; }
    .nc-hint .nc-hint-body {
        margin-top: 12px;
        padding-top: 10px;
        border-top: 1px solid #ffe082;
    }

    /* ── Navigation buttons ──────────────────────────────── */
    .nc-nav {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin: 20px 0;
    }
    .nc-nav a {
        display: inline-block;
        padding: 10px 28px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        font-size: 0.95em;
        border: 2px solid #0d6efd;
        transition: background-color 0.2s, color 0.2s;
    }
    .nc-nav a.nc-nav-prev {
        background-color: white;
        color: #0d6efd;
    }
    .nc-nav a.nc-nav-next {
        background-color: #0d6efd;
        color: white;
    }
    </style>
    """))


# ─────────────────────────────────────────────────────────────
#  CELL TYPES
# ─────────────────────────────────────────────────────────────

def story(title, content):
    """
    Green information / story cell.
    Use for background reading, explanations, or narrative context.

    Example:
        story("What is a Neural Network?", "A neural network is...")
    """
    display(HTML(f"""
    <div class="nc-cell nc-story">
        <div class="nc-badge">
            <i class="fas fa-book-open"></i>&nbsp; Info
        </div>
        <div class="nc-body">
            <h5>{title}</h5>
            {content}
        </div>
    </div>
    """))


def exercise(title, content):
    """
    Blue exercise cell.
    Use for tasks, questions, and things students should actively do.

    Example:
        exercise("Exercise 1", "Write a function that...")
    """
    display(HTML(f"""
    <div class="nc-cell nc-exercise">
        <div class="nc-badge">
            <i class="fas fa-pencil"></i>&nbsp; Exercise
        </div>
        <div class="nc-body">
            <h5>{title}</h5>
            {content}
        </div>
    </div>
    """))


def hint(summary_text, content):
    """
    Yellow collapsible hint cell. Hidden by default — click to reveal.
    Use for tips that students should try without first.

    Example:
        hint("Show Hint", "Try using a list comprehension here.")
    """
    display(HTML(f"""
    <div class="nc-cell nc-hint">
        <div class="nc-badge">
            <i class="fas fa-lightbulb"></i>&nbsp; Hint
        </div>
        <div class="nc-body">
            <details>
                <summary>💡 &nbsp;{summary_text}</summary>
                <div class="nc-hint-body">{content}</div>
            </details>
        </div>
    </div>
    """))


def nav(prev_label, prev_link, next_label, next_link):
    """
    Navigation bar with a Previous and Next button.
    Pass None for either side to show only one button.

    Example:
        nav("← Part 1", "part1.ipynb", "Part 3 →", "part3.ipynb")
        nav(None, None, "Part 2 →", "part2.ipynb")
    """
    prev_html = (
        f'<a class="nc-nav-prev" href="{prev_link}">← {prev_label}</a>'
        if prev_label else ""
    )
    next_html = (
        f'<a class="nc-nav-next" href="{next_link}">{next_label} →</a>'
        if next_label else ""
    )
    display(HTML(f"""
    <div class="nc-nav">
        {prev_html}
        {next_html}
    </div>
    """))
