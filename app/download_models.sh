echo "Download decoder"
rm -f decoder.zip
rm -rf decoder
curl -L -o 'decoder.zip' 'https://drive.google.com/u/0/uc?id=1-47870h4pWhPpJvEJ1BH0Ypv59pkGPgx&export=download&confirm=t'
unzip decoder.zip

echo "Download diffusion_model"
rm -f diffusion_model.zip
rm -rf diffusion_model
curl -L -o 'diffusion_model.zip' 'https://drive.google.com/uc?id=1chrurR7xtX3i8GkgkIEas8ipiUvflDt9&export=download&confirm=t'
unzip diffusion_model.zip

echo "Download text_encoder"
rm -f text_encoder.zip
rm -rf text_encoder
curl -L -o 'text_encoder.zip' 'https://drive.google.com/uc?id=1-4mR0oI68fecEnYXT5gUhffIwW4SRoeK&export=download&confirm=t'
unzip text_encoder.zip