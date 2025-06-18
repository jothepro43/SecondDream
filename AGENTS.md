## Setup Instructions
```bash
# Install required system packages
apt-get update
apt-get install -y curl unzip

# Download latest yt-dlp patched ffmpeg + ffprobe (Linux 64-bit)
curl -L https://github.com/yt-dlp/FFmpeg-Builds/releases/latest/download/ffmpeg-master-latest-linux64-gpl.zip -o ffmpeg.zip

# Extract and move binaries to PATH
unzip ffmpeg.zip
mv ffmpeg-master-latest-linux64-gpl/bin/ffmpeg /usr/local/bin/ffmpeg
mv ffmpeg-master-latest-linux64-gpl/bin/ffprobe /usr/local/bin/ffprobe
chmod +x /usr/local/bin/ffmpeg /usr/local/bin/ffprobe

# Clean up
rm -rf ffmpeg.zip ffmpeg-master-latest-linux64-gpl

# Install Python dependencies
pip install -r requirements.txt
