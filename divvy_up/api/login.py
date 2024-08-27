import frappe
from frappe.auth import LoginManager
from werkzeug.wrappers import Response


@frappe.whitelist(allow_guest=True)
def handle_login():
    try:
        usr = frappe.form_dict.get('usr')
        pwd = frappe.form_dict.get('pwd')

        if not (usr and pwd):
            return Response(
                 '<div class="alert alert-error">Please enter both email and password.</div>'
                 )

        login_manager = LoginManager()
        login_manager.authenticate(user=usr, pwd=pwd)
        login_manager.post_login()

        return Response(
            '''<div class="alert alert-success">Login successful. Redirecting...</div>
        <script>
            setTimeout(function() {
                window.location.href = '/dashboard';
            }, 1000);
        </script>
        ''')
    except frappe.AuthenticationError:
        return Response(
            '<div class="alert alert-error">Invalid email or password. Please try again.</div>'
            )
    except Exception as e:
        frappe.log_error(f"Login Error: {str(e)}")
        return Response(
            '<div class="alert alert-error">An error occurred. Please try again later.</div>'
            )
