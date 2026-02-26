import database as db

workers = 1
timeout = 600
bind = "0.0.0.0:10000"

def post_fork(server, worker):
    from api import resume_incomplete_tasks
    import threading
    db.init_db()
    threading.Thread(target=resume_incomplete_tasks, daemon=True).start()
