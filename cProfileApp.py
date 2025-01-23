import cProfile
import pstats
import io
from app import app

def run_app():
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    pr = cProfile.Profile()
    pr.enable()
    run_app()
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    with open("profile_results.txt", "w") as f:
        f.write(s.getvalue())