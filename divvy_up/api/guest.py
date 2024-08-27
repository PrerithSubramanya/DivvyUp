import frappe
from werkzeug.wrappers import Response


@frappe.whitelist(allow_guest=True)
def update_theme():
    # Toggle the theme
    current_theme = frappe.cache().get_value("theme") or "light"
    new_theme = "dark" if current_theme == "light" else "light"
    
    # Set the new theme in a cache
    frappe.cache().set_value("theme", new_theme)
    
    # Render the full content that includes all necessary blocks
    context = {"theme": new_theme}
    rendered_html = frappe.render_template("templates/pages/base.html", context)
    
    # Return the fully rendered HTML for the main-div
    return Response(rendered_html)
