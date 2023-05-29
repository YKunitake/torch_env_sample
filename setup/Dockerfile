FROM nvidia/cuda:11.3.1-cudnn8-devel-ubuntu20.04
ENV DEBIAN_FRONTEND=noninteractive
#Arguments
ARG USER=developer
ARG GROUP=developer
ARG UID=1000
ARG GID=${UID}
ARG SHELL=/bin/bash

WORKDIR /root
ADD https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-keyring_1.0-1_all.deb .
RUN rm /etc/apt/sources.list.d/cuda.list && \
    rm /etc/apt/sources.list.d/nvidia-ml.list && \
    apt-key del 7fa2af80 && \
    dpkg -i cuda-keyring_1.0-1_all.deb && \
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub && \
    rm cuda-keyring_1.0-1_all.deb && \
    apt-get update && apt-get install -y \
    #base
    sudo \
    #timezone
    tzdata locales curl wget gnupg2 \
    #language
    language-pack-ja-base language-pack-ja fonts-ipafont-gothic dbus-x11 \
    fcitx-mozc fcitx-imlist \
    #opengl
    libglu1-mesa-dev freeglut3-dev mesa-common-dev \
    #etc
    libpcl-dev cmake cmake-curses-gui \
    git vim libconfig++-dev libglvnd-dev libgl1-mesa-dev libegl1-mesa-dev \
    libgles2-mesa-dev libglvnd0 libgl1 libglx0 libegl1 libgles2 libopencv-dev\
    #blensor etc
    libusb-1.0-0 fuse libfuse-dev \
    #gdal
    gdal-bin libsm6 libxrender1 libxext6 libglib2.0-0 \
    #python
    python3 python3-pip python3-argcomplete python3-dev python3-setuptools \
    #torchvision
    libjpeg-dev zlib1g-dev libavcodec-dev libavformat-dev libswscale-dev && \
    rm -rf /var/lib/apt/lists/*
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES graphics,utility,compute
ENV LD_LIBRARY_PATH /usr/lib/cuda/lib64
ENV TORCH_CUDA_ARCH_LIST 6.0 6.1 7.0 8.6+PTX
RUN pip3 install --upgrade pip && \
    pip3 install setuptools numpy && \
    pip3 install -U setuptools numpy && \
    pip3 install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 -f https://download.pytorch.org/whl/cu113/torch_stable.html && \
    pip3 install pycocotools opencv-python-headless open3d wheel \
    matplotlib pyshp networkx==2.2 scikit-learn plyfile trimesh hydra-core \
    omegaconf cupy-cuda113 gym collections-extended more-itertools
RUN pip3 install PyQt5 launchpadlib toml timm nibabel tqdm easydict scipy \
    coloredlogs h5py gitpython PyYAML && \
    ln -s /usr/local/cuda/lib64/libcudart.so /usr/lib/libcudart.so && \
    rm -rf /var/lib/apt/lists/*

#user setting
RUN groupadd --gid ${GID} ${GROUP} && \
    useradd -g ${GID} -u ${UID} -ms ${SHELL} ${USER} && \
    echo "${USER}:${USER}" | chpasswd && \
    usermod -aG sudo ${USER} && \
    echo "${USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/${USER} && \
    chmod 0440 /etc/sudoers.d/${USER}

USER ${USER}
CMD mkdir /home/${USER}/workspace
WORKDIR /home/${USER}/workspace

ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES graphics,utility,compute
ENV LD_LIBRARY_PATH /usr/lib/cuda/lib64
ENV TORCH_CUDA_ARCH_LIST 6.0 6.1 7.0 8.6+PTX
