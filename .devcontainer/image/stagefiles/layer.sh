set -e

export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get install --no-install-recommends --yes --quiet \
    build-essential \
    cmake \
    curl \
    git \
    openssh-client \
    vim-tiny \
    less \
    graphviz \
    libgraphviz-dev \
    pandoc \
    virtualenv \
    ca-certificates


# Make vim tiny default
ln -sfn /usr/bin/vi /usr/bin/vim

# Clean up
apt-get autoremove -y
apt-get clean

rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Append to seismo user's .bashrc to source secrets/.env if it exists
echo '
# Source secrets/.env if it exists
if [ -f "$HOME/workspace/secrets/.env" ]; then
    source "$HOME/workspace/secrets/.env"
fi
' >> /home/seismo/.bashrc
