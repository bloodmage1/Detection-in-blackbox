FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu18.04

RUN apt-get update && apt-get install -y \
    python3.8 \
    python3.8-venv \
    python3.8-distutils \
    python3-pip \
    bash \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1

WORKDIR /app
RUN python3 -m venv blackbox_car && \
    . blackbox_car/bin/activate && \
    pip install --upgrade pip && \
    pip install torch qt-material opencv-python

COPY . /app

ENTRYPOINT ["/bin/bash"]
