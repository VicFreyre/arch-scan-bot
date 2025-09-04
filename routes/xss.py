from flask import request, render_template_string

XSS_HTML = """
<!doctype html>
<title>Reflected XSS Demo</title>
<h2>Reflected XSS (intencionalmente vulnerável)</h2>
<form method="GET">
  <label>Mensagem (será refletida sem escape):</label>
  <input name="msg" value="{{ msg|default('') }}">
  <button type="submit">Refletir</button>
</form>
<p>Output:</p>
<div style="border:1px solid #ccc; padding:8px;">
  {{ reflected|safe }}
</div>
"""

def init_routes(app):
    @app.route("/xss")
    def xss_demo():
        msg = request.args.get("msg", "")
        return render_template_string(XSS_HTML, msg=msg, reflected=msg)
    