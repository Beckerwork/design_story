import ipywidgets as widgets
from IPython.display import display, clear_output, HTML

def guess_speed():
    korrekte_antwort = 22.11  # m * 145 + c = 0.33 * 145 + (-25.74)
    toleranz = 1

    # --- Inject CSS ---
    display(HTML("""
    <style>
    .gs-box {
        background-color: #beeaf1 !important;
        border: 4px solid #31708f !important;
        border-radius: 10px !important;
        padding: 24px 32px 20px 32px !important;
        max-width: 420px !important;
        margin: 25px auto 0 auto !important;
    }
    .gs-box .widget-label {
        display: none !important;
    }
    .gs-field input {
        border: 1.5px solid #31708f !important;
        border-radius: 6px !important;
        padding: 7px 12px !important;
        font-size: 14px !important;
        background: white !important;
        outline: none !important;
        width: 100% !important;
    }
    .gs-field input:focus {
        box-shadow: 0 0 0 3px rgba(49,112,143,0.2) !important;
    }
    .gs-btn button {
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
    .gs-btn button:hover {
        background-color: #245269 !important;
    }
    </style>
    """))

    # --- Widgets ---
    header = widgets.HTML(value="""
        <div style="text-align:center; margin-bottom:16px;">
            <h3 style="color:#31708f; margin:0 0 6px 0;">🤖 Maschinenvorhersage</h3>
            <p style="margin:0; color:#31708f; font-size:14px;">
                Was glauben die Maschinen, wie schnell Sarah ist?<br>
                Benutze die Gerade der Roboter, um es herauszufinden!
            </p>
        </div>
        <hr style="border:none; border-top:1px solid #31708f; opacity:0.3; margin-bottom:16px;">
    """)

    eingabe = widgets.Text(
        placeholder='Zahl wie z.B. 10,50',
        layout=widgets.Layout(width='200px')
    )
    eingabe.add_class('gs-field')

    bestaetigen = widgets.Button(
        description='Überprüfen',
        layout=widgets.Layout(width='140px', margin='4px 0 0 0')
    )
    bestaetigen.add_class('gs-btn')

    output = widgets.Output()
    output.add_class('pw-output')

    def pruefe_antwort(b):
        with output:
            clear_output()
            raw = eingabe.value.strip().replace(',', '.')
            try:
                wert = float(raw)
            except ValueError:
                display(widgets.HTML(value="""
                    <p style="text-align:center; color:#a94442; font-weight:bold; font-size:large; margin-top:8px;">
                        ⚠️ Bitte eine Zahl eingeben (z. B. 10,50).
                    </p>
                """))
                return

            if abs(wert - korrekte_antwort) <= toleranz:
                display(widgets.HTML(value=f"""
                    <div style="text-align:center; margin-top:8px;">
                      <p style="color:#3c763d; font-weight:bold; font-size:large; margin:0 0 8px 0;">
                        ✅ Richtig! Die Roboter schätzen Sarahs Geschwindigkeit auf ca. {korrekte_antwort} km/h.
                      </p>
                      <p style="color:#31708f; font-size:14px; margin:0;">
                        Dein Wert liegt nah genug an der Vorhersage der Geraden.
                      </p>
                    </div>
                """))
            else:
                display(widgets.HTML(value=f"""
                    <p style="text-align:center; color:#a94442; font-weight:bold; font-size:large; margin-top:8px;">
                        ❌ Nicht ganz. Schau nochmal genau auf die Gerade bei einer Körpergröße von 145 cm.
                    </p>
                """))

    bestaetigen.on_click(pruefe_antwort)

    outer = widgets.VBox(
        [header, eingabe, bestaetigen],
        layout=widgets.Layout(align_items='center', gap='10px')
    )
    outer.add_class('gs-box')

    display(outer)
    display(output)
