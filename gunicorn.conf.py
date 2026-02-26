import database as db

workers = 1
timeout = 600
bind = "0.0.0.0:10000"

def post_fork(server, worker):
    import threading
    from api import resume_incomplete_tasks
    
    def startup():
        db.init_db()
        resume_incomplete_tasks()
    
    threading.Thread(target=startup, daemon=True).start()
