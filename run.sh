#!/bin/bash
docker run -it --gpus all --rm --net host \
    -v /tmp/.X11-unix/:/tmp/.X11.-unix:rw \
    -v /own/env/torch_env_sample/workspace:/home/developer/workspace \
    --cap-add SYS_ADMIN \
    --device /dev/fuse \
    --security-opt apparmor:unconfined \
    -e DISPLAY=:1 \
    -e QT_X11_NO_MITSHM=1 \
    torch_env /bin/bash
