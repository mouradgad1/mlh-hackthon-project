from flask import Flask, render_template, request, jsonify
import yt_dlp
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    if not query:
        return jsonify({'error': 'No search query provided'}), 400
    
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'extract_flat': True,
            'default_search': 'ytsearch10',
            'noplaylist': True,
            'extractor_args': {
                'youtube': {
                    'skip': ['dash', 'hls'],
                    'player_client': ['android'],  
                    'player_skip': ['configs'],
                }
            },
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept-Language': 'en-US,en;q=0.9'
            }
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f'ytsearch10:{query}', download=False)
            
            results = []
            for entry in info.get('entries', []):
                if not entry:
                    continue
                    
                results.append({
                    'title': entry.get('title', 'Unknown Track'),
                    'thumbnail': entry.get('thumbnails', [{}])[0].get('url', ''),
                    'video_id': entry.get('id', ''),
                    'duration': entry.get('duration', 0),
                    'channel': entry.get('uploader', 'Unknown Artist')
                })
            
            return jsonify({'results': results})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/stream/<video_id>')
def stream(video_id):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'extract_flat': True
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f'https://www.youtube.com/watch?v={video_id}', download=False)
            audio_url = info.get('url', None)
            
            if not audio_url:
                return jsonify({'error': 'Could not extract audio URL'}), 500
                
            return jsonify({
                'audio_url': audio_url,
                'title': info.get('title', 'Unknown Track'),
                'thumbnail': info.get('thumbnails', [{}])[0].get('url', ''),
                'channel': info.get('uploader', 'Unknown Artist')
            })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)