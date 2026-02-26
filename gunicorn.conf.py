import database as db

workers = 1
timeout = 600
bind = "0.0.0.0:10000"

def post_fork(server, worker):
    from api import resume_incomplete_tasks
    print("[POST_FORK] Starting db.init_db...")
    db.init_db()
    print("[POST_FORK] db.init_db done, starting resume...")
    resume_incomplete_tasks()
    print("[POST_FORK] Done, worker ready.")
