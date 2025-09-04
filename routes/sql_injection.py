from flask import request, render_template_string
from db import get_db

SQL_HTML = """
<!doctype html>
<title>SQL Injection Demo</title>
<h2>SQL Injection (intencionalmente vulnerável)</h2>
<form method="GET">
  <label>User id / query fragment:</label>
  <input name="q" placeholder="1" value="{{ q|default('') }}">
  <button type="submit">Buscar</button>
</form>
<pre>{{ output }}</pre>
"""

def init_routes(app):
    @app.route("/sql_injection")
    def sql_injection():
        q = request.args.get("q", "")
        output = ""
        if q:
            db = get_db()
            raw_query = f"SELECT id, username, email, bio FROM users WHERE id = {q};"
            print("[SQL-LOG] Executando query:", raw_query)
            try:
                cur = db.execute(raw_query)
                rows = cur.fetchall()
                if rows:
                    output = "\n".join(
                        f"id={r['id']} | user={r['username']} | email={r['email']} | bio={r['bio']}"
                        for r in rows
                    )
                else:
                    output = "(nenhum resultado)"
            except Exception as e:
                output = f"Erro ao executar query: {e}"
        return render_template_string(SQL_HTML, q=q, output=output)
