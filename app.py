from flask import Flask, render_template, request, redirect, url_for, flash
from database import init_db, get_db
from pathlib import Path
import os

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY=os.environ.get("SECRET_KEY", "troque-esta-chave-em-producao"),
        DATABASE=os.environ.get("DATABASE_PATH", str(Path(__file__).with_name("taskflow.db"))),
    )
    if test_config:
        app.config.update(test_config)

    Path(app.config["DATABASE"]).parent.mkdir(parents=True, exist_ok=True)
    init_db(app)

    @app.get("/")
    def index():
        status = request.args.get("status", "")
        db = get_db()
        if status in ("Pendente", "Em andamento", "Concluída"):
            tasks = db.execute(
                "SELECT * FROM tasks WHERE status = ? ORDER BY id DESC", (status,)
            ).fetchall()
        else:
            tasks = db.execute("SELECT * FROM tasks ORDER BY id DESC").fetchall()
        return render_template("index.html", tasks=tasks, selected_status=status)

    @app.post("/tasks")
    def create_task():
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        priority = request.form.get("priority", "Média")
        if not title:
            flash("Informe um título para a tarefa.", "error")
            return redirect(url_for("index"))
        if priority not in ("Baixa", "Média", "Alta"):
            priority = "Média"
        get_db().execute(
            "INSERT INTO tasks (title, description, priority) VALUES (?, ?, ?)",
            (title, description, priority),
        )
        get_db().commit()
        flash("Tarefa cadastrada com sucesso.", "success")
        return redirect(url_for("index"))

    @app.post("/tasks/<int:task_id>/update")
    def update_task(task_id):
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        status = request.form.get("status", "Pendente")
        priority = request.form.get("priority", "Média")
        if not title:
            flash("O título não pode ficar vazio.", "error")
            return redirect(url_for("index"))
        if status not in ("Pendente", "Em andamento", "Concluída"):
            flash("Status inválido.", "error")
            return redirect(url_for("index"))
        if priority not in ("Baixa", "Média", "Alta"):
            flash("Prioridade inválida.", "error")
            return redirect(url_for("index"))
        db = get_db()
        existing = db.execute("SELECT id FROM tasks WHERE id = ?", (task_id,)).fetchone()
        if existing is None:
            flash("Tarefa não encontrada.", "error")
            return redirect(url_for("index"))
        db.execute(
            """UPDATE tasks SET title = ?, description = ?, status = ?, priority = ?
               WHERE id = ?""",
            (title, description, status, priority, task_id),
        )
        db.commit()
        flash("Tarefa atualizada.", "success")
        return redirect(url_for("index"))

    @app.post("/tasks/<int:task_id>/delete")
    def delete_task(task_id):
        db = get_db()
        db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        db.commit()
        flash("Tarefa removida.", "success")
        return redirect(url_for("index"))

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
