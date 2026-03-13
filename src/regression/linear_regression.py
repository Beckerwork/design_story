import threading
import time

from ipywidgets import interactive, widgets, VBox
from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

from utils.colors import colors


def get_independent_variable():
    """Get independent variable (x values)."""
    rng = np.random.default_rng(51)
    independent_variable = rng.uniform(110, 170, 20)
    independent_variable[-1] += 5
    return independent_variable


def get_dependent_variable(independent_variable):
    """Get dependent variable (y values)."""
    rng = np.random.default_rng(53)
    dependent_variable = 10 + (independent_variable - 110) * (30 - 10) / (170 - 110) + rng.normal(0, 3, independent_variable.size)
    return dependent_variable


def plot_data():
    independent_variable = get_independent_variable()
    dependent_variable = get_dependent_variable(independent_variable)

    # Plot height vs speed.
    fig, ax = plt.subplots(figsize=(7, 5))
    fig.canvas.header_visible = False
    
    ax.scatter(independent_variable, dependent_variable, color=colors['dark_blue'], label='Daten der Kinder')

    # Set annotations
    ax.set_xlabel('Körpergröße (cm)')
    ax.set_ylabel('Maximale Geschwindigkeit (km/h)')
    ax.set_title('Größe vs. maximale Geschwindigkeit', y=1.2)
    ax.legend(loc='upper left', bbox_to_anchor=(0.0, 1.2))
    ax.grid(True)
    plt.ylim([-1.5, 31.5])
    # Show plot
    plt.tight_layout()
    plt.show()


def mse(ground_truth, measured_values):
    """Compute mean squared error."""
    return np.mean((ground_truth - measured_values) ** 2)


def fit_regression_line(independent_variable, dependent_variable, power=1):
    """
    Fit linear regression line to data."""
    X = independent_variable.reshape(-1, 1)
    X = PolynomialFeatures(degree=power).fit_transform(X)
    model = LinearRegression().fit(X[:, 1:], dependent_variable)
    ml_slope = model.coef_
    ml_intercept = model.intercept_
    ml_predictions = model.predict(X[:, 1:])
    ml_mse = mse(dependent_variable, ml_predictions)
    return ml_slope, ml_intercept, ml_predictions, ml_mse


def lineare_regression():
    independent_variable = get_independent_variable()
    dependent_variable = get_dependent_variable(independent_variable)

    # Plot height vs speed.
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(independent_variable, dependent_variable, color=colors['dark_blue'], label='Daten der Kinder')

    # Plot adjustable regression line.
    default_slope = 0
    default_intercept = 0
    default_predictions = default_slope * independent_variable + default_intercept
    default_mse = mse(dependent_variable, default_predictions)
    line, = ax.plot(independent_variable, default_slope * independent_variable + default_intercept, color=colors['orange'],
                    linestyle='-', label=f'Eure Gerade: Output = {default_slope}'.replace('.', ',') + f'* Input + {default_intercept}'.replace('.', ',') + f'(Fehlerwert: {default_mse:.2f})'.replace('.', ','))

    def update_adjustable_line(slope, intercept):
        """Update the adjustable regression line, which is changed by the sliders."""
        student_predictions = slope * independent_variable + intercept
        student_mse = mse(dependent_variable, student_predictions)
        line.set_ydata(student_predictions)
        line.set_label(f"Eure Gerade: Output = {slope:.2f}".replace('.', ',') + f" * Input + {intercept:.2f}".replace('.', ',') + f" (Fehlerwert: {student_mse:.2f})".replace('.', ','))
        ax.legend()
        fig.canvas.draw_idle()

    w_adj_line = interactive(update_adjustable_line,
                             slope=widgets.FloatSlider(min=0.05, max=0.30, step=0.01, value=0, description='Steigung'),
                             intercept=widgets.FloatSlider(min=-30, max=-15, step=0.01, value=0, description='y-Achse'),)
    display(w_adj_line)

    # Plot the ml regression line (by default invisible, see checkbox).
    ml_slope, ml_intercept, ml_predictions, ml_mse = fit_regression_line(independent_variable, dependent_variable)
    regression_line, = ax.plot(independent_variable, ml_predictions, color=colors['green'], linestyle='-', label='',
                               visible=False)
    # Placeholder for the annotation warning, if the manual line is too far away from a good result.
    annotation_warning = ax.annotate(
        "Die manuelle Gerade ist noch etwas zu ungenau.\n Bitte versuche es erneut.",
        xy=(125, 15),
        xytext=(125, 15.2),
        textcoords="data",
        bbox=dict(boxstyle="round,pad=0.3", fc=colors['brown'], ec=colors['grey'], lw=1),
        visible=False,  # initially hidden
        fontsize=14
    )
    def update_regression_line(change):
        """Function to show or hide the regression line depending on the checkbox."""
        if change['new']:  # Checkbox is activated
            intercept_current = w_adj_line.kwargs['intercept']
            slope_current = w_adj_line.kwargs['slope']
            pred_current = intercept_current + slope_current * independent_variable
            mse_current = mse(dependent_variable, pred_current)
            if abs(mse_current - ml_mse) > 5:
                annotation_warning.set_visible(True)
                regression_line.set_visible(False)
                regression_line.set_label('')
                fig.canvas.draw_idle()  # redraw line
                def hide_warning_after_delay():
                    time.sleep(3)
                    checkbox.value = False
                    annotation_warning.set_visible(False)
                    fig.canvas.draw_idle()
                # Run the delay in a background thread
                threading.Thread(target=hide_warning_after_delay).start()
            else:
                regression_line.set_visible(True)
                regression_line.set_label(
                f'Roboter Gerade: Output = {ml_slope[0]:.2f}'.replace('.', ',') + f' * Input + {ml_intercept:.2f}'.replace('.', ',') + f' (Fehlerwert: {ml_mse:.2f})'.replace('.', ','))
        else:  # Checkbox is deactivated
            regression_line.set_visible(False)
            regression_line.set_label('')
        ax.legend()
        fig.canvas.draw_idle()  # redraw line
    # Create a checkbox, which execute the function update_regression line if it is clicked.
    checkbox = widgets.Checkbox(value=False, description='Zeige Regressionsgerade', disabled=False, indent=False)
    checkbox.observe(update_regression_line, names='value')
    display(checkbox)


    # Set annotations
    ax.set_xlabel('Körpergröße (cm)')
    ax.set_ylabel('Maximale Geschwindigkeit (km/h)')
    ax.set_title('Größe vs. maximale Geschwindigkeit', y=1.2)
    ax.legend(loc='upper left', bbox_to_anchor=(0.0, 1.2))
    ax.grid(True)
    # Show plot
    plt.tight_layout()
    plt.show()

def lineare_regression_big():
    independent_variable = get_independent_variable()
    dependent_variable = get_dependent_variable(independent_variable)

    fig, ax = plt.subplots(figsize=(7, 7))
    fig.canvas.header_visible = False
    
    ax.scatter(independent_variable, dependent_variable, color=colors['dark_blue'], label='Daten der Kinder')

    x_max = max(abs(independent_variable.min()), abs(independent_variable.max())) + 5
    y_max = max(abs(dependent_variable.min()), abs(dependent_variable.max())) +5 
    ax.set_xlim(-10, x_max)
    ax.set_ylim(-y_max, y_max)

    # Move spines to center
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    ax.add_patch(plt.Rectangle((0, 0), 1, 1, fill=False, transform=ax.transAxes, clip_on=False, linewidth=1, edgecolor='black'))

    # Full-range x for drawing lines
    x_line = np.linspace(-10, x_max, 300)

    default_slope = 0
    default_intercept = 0
    default_predictions = default_slope * independent_variable + default_intercept
    default_mse = mse(dependent_variable, default_predictions)
    line, = ax.plot(x_line, default_slope * x_line + default_intercept, color=colors['orange'],
                    linestyle='-', label=f'Eure Gerade: Output = {default_slope}'.replace('.', ',') + f'* Input + {default_intercept}'.replace('.', ',') + f'(Fehlerwert: {default_mse:.2f})'.replace('.', ','))

    def update_adjustable_line(slope, intercept):
        student_predictions = slope * independent_variable + intercept
        student_mse = mse(dependent_variable, student_predictions)
        line.set_xdata(x_line)
        line.set_ydata(slope * x_line + intercept)
        line.set_label(f"Eure Gerade: Output = {slope:.2f}".replace('.', ',') + f" * Input + {intercept:.2f}".replace('.', ',') + f" (Fehlerwert: {student_mse:.2f})".replace('.', ','))
        ax.legend()
        fig.canvas.draw_idle()

    w_adj_line = interactive(update_adjustable_line,
                             slope=widgets.FloatSlider(min=0.10, max=0.40, step=0.01, value=0.10, description='Steigung'),
                             intercept=widgets.FloatSlider(min=-30, max=-10, step=0.01, value=-10, description='y-Achse'),)
    display(w_adj_line)

    ml_slope, ml_intercept, ml_predictions, ml_mse = fit_regression_line(independent_variable, dependent_variable)
    regression_line, = ax.plot(x_line, ml_slope[0] * x_line + ml_intercept, color=colors['green'], linestyle='-', label='',
                               visible=False)
    
    annotation_warning = ax.annotate(
        "Die manuelle Gerade ist noch etwas zu ungenau.\n Bitte versuche es erneut.",
        xy=(0.5, 0.5),
        xycoords='axes fraction',
        ha='center', va='center',
        color='black',
        bbox=dict(boxstyle="round,pad=0.3", fc='#fcf8e3', ec='#8a6d3b', lw=1),
        visible=False,
        fontsize=14
    )

    def update_regression_line(change):
        if change['new']:
            intercept_current = w_adj_line.kwargs['intercept']
            slope_current = w_adj_line.kwargs['slope']
            pred_current = intercept_current + slope_current * independent_variable
            mse_current = mse(dependent_variable, pred_current)
            if abs(mse_current - ml_mse) > 5:
                annotation_warning.set_visible(True)
                regression_line.set_visible(False)
                regression_line.set_label('')
                fig.canvas.draw_idle()
                def hide_warning_after_delay():
                    time.sleep(3)
                    checkbox.value = False
                    annotation_warning.set_visible(False)
                    fig.canvas.draw_idle()
                threading.Thread(target=hide_warning_after_delay).start()
            else:
                regression_line.set_visible(True)
                regression_line.set_label(
                f'Roboter Gerade: Output = {ml_slope[0]:.2f}'.replace('.', ',') + f' * Input + {ml_intercept:.2f}'.replace('.', ',') + f' (Fehlerwert: {ml_mse:.2f})'.replace('.', ','))
        else:
            regression_line.set_visible(False)
            regression_line.set_label('')
        ax.legend()
        fig.canvas.draw_idle()

    checkbox = widgets.Checkbox(value=False, description='Zeige Regressionsgerade', disabled=False, indent=False)
    checkbox.observe(update_regression_line, names='value')
    display(checkbox)

    ax.set_xlabel('Körpergröße (cm)')
    ax.set_ylabel('Maximale Geschwindigkeit (km/h)')
    ax.set_title('Größe vs. maximale Geschwindigkeit', y=1.2)
    ax.legend(loc='upper left', bbox_to_anchor=(0.0, 1.2))
    ax.grid(True)
    plt.tight_layout()
    plt.show()


def zeige_lineare_regression():
    independent_variable = get_independent_variable()
    dependent_variable = get_dependent_variable(independent_variable)

    # Plot height vs speed.
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(independent_variable, dependent_variable, color=colors['dark_blue'], label='Daten der Kinder')

    # Plot the ml regression line (by default invisible, see checkbox).
    ml_slope, ml_intercept, ml_predictions, ml_mse = fit_regression_line(independent_variable, dependent_variable)
    regression_line, = ax.plot(independent_variable, ml_predictions, color=colors['green'], linestyle='-', label='',
                               visible=True)
    regression_line.set_label(
        f'Roboter Gerade: Output = {ml_slope[0]:.2f}'.replace('.', ',') + 
        f' * Input + {ml_intercept:.2f}'.replace('.', ',') + 
        f' (Fehlerwert: {ml_mse:.2f})'.replace('.', ','))

    ax.text(145.5, 21, "Sarah", fontsize=9, ha='left', color=colors['purple'])
    ax.scatter(145, 21.3, color=colors['purple'])

    ax.text(152.5, 26.7, "Ben", fontsize=9, ha='right', color=colors['purple'])
    ax.scatter(153, 27, color=colors['purple'])  

    ax.set_xlabel('Körpergröße (cm)')
    ax.set_ylabel('Maximale Geschwindigkeit (km/h)')
    ax.set_title('Größe vs. maximale Geschwindigkeit', y=1.2)
    ax.legend(loc='upper left', bbox_to_anchor=(0.0, 1.2))
    ax.grid(True)
    # Show plot
    plt.tight_layout()
    plt.show()