from . import app
import json
from flask import jsonify, request, Response

# Fallback in-memory data store for testing
songs_data = [{"id": 1, "title": "Test Song", "artist": "Test Artist"}]

@app.route("/health", methods=["GET"])
def health():
    return jsonify(dict(status="OK")), 200

@app.route("/count", methods=["GET"])
def count():
    return jsonify(length=len(songs_data)), 200

@app.route("/song", methods=["GET"])
def get_songs():
    return jsonify({"songs": songs_data}), 200

@app.route("/song/<int:id>", methods=["GET"])
def get_song_by_id(id):
    for song in songs_data:
        if song.get("id") == id:
            return jsonify(song), 200
    return jsonify({"message": "song not found"}), 404

@app.route("/song", methods=["POST"])
def create_song():
    song = request.get_json()
    songs_data.append(song)
    return jsonify(song), 201

@app.route("/song/<int:id>", methods=["PUT"])
def update_song(id):
    song_data = request.get_json()
    for i, song in enumerate(songs_data):
        if song.get("id") == id:
            songs_data[i].update(song_data)
            return jsonify(songs_data[i]), 200
    return jsonify({"message": "song not found"}), 404

@app.route("/song/<int:id>", methods=["DELETE"])
def delete_song(id):
    for i, song in enumerate(songs_data):
        if song.get("id") == id:
            del songs_data[i]
            return "", 204
    return jsonify({"message": "song not found"}), 404
