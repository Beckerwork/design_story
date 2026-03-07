import ipywidgets as widgets
from IPython.display import display, clear_output, HTML

def password3():
    richtiges_passwort = ["MachineLearning", "Machine Learning", "Machine-Learning",
                          "machinelearning", "machine learning", "machine-learning",
                          "MACHINELEARNING", "MACHINE LEARNING", "MACHINE-LEARNING",
                          "Machine learning"]

    # --- Inject CSS ---
    display(HTML("""
    <style>
    .pw-box {
        background-color: #beeaf1 !important;
        border: 4px solid #31708f !important;
        border-radius: 10px !important;
        padding: 24px 32px 20px 32px !important;
        max-width: 420px !important;
        margin: 25px auto 0 auto !important;
    }
    .pw-box .widget-label {
        display: none !important;
    }
    .pw-field input, .pw-text input {
        border: 1.5px solid #31708f !important;
        border-radius: 6px !important;
        padding: 7px 12px !important;
        font-size: 14px !important;
        background: white !important;
        outline: none !important;
        width: 100% !important;
    }
    .pw-field input:focus, .pw-text input:focus {
        box-shadow: 0 0 0 3px rgba(49,112,143,0.2) !important;
    }
    .pw-btn button {
        background-color: #31708f !important;
        color: white !important;
        border: none !important;
        border-radius: 6px !important;
        padding: 9px 28px !important;
        font-weight: bold !important;
        font-size: 14px !important;
        cursor: pointer !important;
        transition: background-color 0.2s !important;
        letter-spacing: 0.3px !important;
    }
    .pw-btn button:hover {
        background-color: #245269 !important;
    }
    .pw-checkbox label {
        color: #31708f !important;
        font-size: 13px !important;
    }
    </style>
    """))

    # --- Widgets ---
    header = widgets.HTML(value="""
        <div style="text-align:center; margin-bottom:16px;">
            <h3 style="color:#31708f; margin:0 0 6px 0;">🔐 Zugang zum Serverraum</h3>
            <p style="margin:0; color:#31708f; font-size:14px;">
                Gebt das Codewort ein, um die Tür zu öffnen:
            </p>
        </div>
        <hr style="border:none; border-top:1px solid #31708f; opacity:0.3; margin-bottom:16px;">
    """)

    passwort_eingabe = widgets.Password(
        placeholder='Codewort eingeben …',
        layout=widgets.Layout(width='280px')
    )
    passwort_eingabe.add_class('pw-field')

    show_passwort = widgets.Checkbox(
        value=False,
        description='Passwort anzeigen',
        layout=widgets.Layout(width='180px', margin='0')
    )
    show_passwort.add_class('pw-checkbox')

    bestaetigen = widgets.Button(
        description='Bestätigen',
        layout=widgets.Layout(width='140px', margin='4px 0 0 0')
    )
    bestaetigen.add_class('pw-btn')

    output = widgets.Output()
    output.add_class('pw-output')
    password_widget_map = {'field': passwort_eingabe}

    input_col = widgets.VBox(
        [passwort_eingabe, show_passwort],
        layout=widgets.Layout(align_items='center', gap='8px')
    )

    def toggle_password_visibility(change):
        if change['new']:
            visible_pass = widgets.Text(
                value=passwort_eingabe.value,
                placeholder='Codewort eingeben …',
                layout=widgets.Layout(width='280px')
            )
            visible_pass.add_class('pw-text')
            def on_visible_change(c):
                passwort_eingabe.value = c['new']
            visible_pass.observe(on_visible_change, names='value')
            input_col.children = (visible_pass, show_passwort)
            password_widget_map['field'] = visible_pass
        else:
            input_col.children = (passwort_eingabe, show_passwort)
            password_widget_map['field'] = passwort_eingabe

    def pruefe_passwort(b):
        with output:
            clear_output()
            pw = password_widget_map['field'].value
            if pw in richtiges_passwort:
                display(widgets.HTML(value="""
                    <div style="text-align:center; margin-top:8px;">
                      <p style="color:#3c763d; font-weight:bold; margin:0 0 12px 0;">
                        ✅ Passwort korrekt! Zugriff gewährt.
                      </p>
                      <a href="story_game_2.ipynb" style="
                        display: inline-block;
                        padding: 10px 24px;
                        border-radius: 8px;
                        border: 2px solid #3c763d;
                        background-color: #3c763d;
                        color: white;
                        text-decoration: none;
                        font-weight: bold;
                        box-shadow: 0 2px 6px rgba(0,0,0,0.15);
                      ">In den Serverraum &nbsp;<i class="fa fa-arrow-right"></i></a>
                    </div>
                """))
            else:
                display(widgets.HTML(value="""
                    <p style="text-align:center; color:#a94442; font-weight:bold; margin-top:8px;">
                        ❌ Falsches Passwort! Zugriff verweigert.
                    </p>
                """))

    show_passwort.observe(toggle_password_visibility, names='value')
    bestaetigen.on_click(pruefe_passwort)

    outer = widgets.VBox(
        [header, input_col, bestaetigen],
        layout=widgets.Layout(align_items='center', gap='10px')
    )
    outer.add_class('pw-box')

    display(outer)
    display(output)