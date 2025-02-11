# Update the system
sudo apt update && sudo apt upgrade -y

# Python dev deps
sudo apt install make \
          build-essential \
          libssl-dev \
          zlib1g-dev \
          libbz2-dev \
          libreadline-dev \
          libsqlite3-dev \
          wget \
          curl \
          llvm \
          libncursesw5-dev \
          xz-utils \
          tk-dev \
          libxml2-dev \
          libxmlsec1-dev \
          libffi-dev \
          jackd2 \
          qjackctl \
          screen \
          liblzma-dev -y

# Install poetry
sudo apt-get install python3-poetry

# Install pyenv
curl -fsSL https://pyenv.run | bash
# echo '' >> ~/.bashrc
# echo '# Pyenv' >> ~/.bashrc
# echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
# echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
# echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc

# Ensures Jack works
sudo usermod -aG audio $(whoami)