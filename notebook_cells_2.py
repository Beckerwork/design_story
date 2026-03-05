from IPython.display import HTML, display

# ─────────────────────────────────────────────────────────────
#  SETUP  —  call once at the top of your notebook
#  Loads Bootstrap + Font Awesome + all cell type styles.
#  After this, just use markdown cells with the class names below.
#
#  Available classes:
#    nc-story     → green  | background reading / information
#    nc-exercise  → blue   | tasks and questions
#    nc-hint      → yellow | collapsible hint (use <details> inside)
#    nc-nav       → navigation bar with prev/next buttons
#
#  Markdown template — copy/paste into any markdown cell:
#
#  ── Story ────────────────────────────────────────────────────
#  <div class="nc-story nc-cell">
#    <div class="nc-badge"><i class="fas fa-book-open"></i> Info</div>
#    <div class="nc-body">
#      <h5>Your Title</h5>
#      Your content here...
#    </div>
#  </div>
#
#  ── Exercise ─────────────────────────────────────────────────
#  <div class="nc-exercise nc-cell">
#    <div class="nc-badge"><i class="fas fa-pencil"></i> Exercise</div>
#    <div class="nc-body">
#      <h5>Your Title</h5>
#      Your content here...
#    </div>
#  </div>
#
#  ── Hint ─────────────────────────────────────────────────────
#  <div class="nc-hint nc-cell">
#    <div class="nc-badge"><i class="fas fa-lightbulb"></i> Hint</div>
#    <div class="nc-body">
#      <details>
#        <summary>💡 Show Hint</summary>
#        <div class="nc-hint-body">Your hint here...</div>
#      </details>
#    </div>
#  </div>
#
#  ── Navigation ───────────────────────────────────────────────
#  <div class="nc-nav">
#    <a class="nc-nav-prev" href="part1.ipynb">← Part 1</a>
#    <a class="nc-nav-next" href="part3.ipynb">Part 3 →</a>
#  </div>
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
