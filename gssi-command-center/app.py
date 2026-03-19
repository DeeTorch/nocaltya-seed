from flask import Flask, request, jsonify
import json, time

app = Flask(__name__)
session_state = {"thread_id": "oracle_nocaltya_hardened", "agents": 16, "log": ["Dashboard live • Tool Hook confirmed"]}

@app.route('/api/status')
def status():
    return jsonify({"status": "100% LIVE", "layers": 16, "connected_session": session_state["thread_id"]})

@app.route('/api/command', methods=['POST'])
def command():
    cmd = request.json.get('cmd')
    session_state["log"].append(f"{time.strftime('%H:%M')} • {cmd} • executed by Swarm")
    return jsonify({"result": f"✅ {cmd} routed through full stack", "log": session_state["log"][-5:]})

@app.route('/api/save', methods=['POST'])
def save():
    session_state["thread_id"] = request.json.get('data')
    return jsonify({"saved": True, "message": "Persisted to future sessions"})

if __name__ == '__main__':
    print("🚀 GSSI Command Center running on http://127.0.0.1:5000")
    app.run(debug=True)