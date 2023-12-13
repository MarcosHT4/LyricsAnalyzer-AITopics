FROM python:3.11
ENV PORT 8000
ARG OPENAI_KEY
ENV OPENAI_KEY=$OPENAI_KEY

ARG NVIDIA_KEY
ENV NVIDIA_KEY=$NVIDIA_KEY

COPY requirements.txt /
RUN apt-get update && apt-get install git-all git-lfs -y
RUN git-lfs install

COPY ./src /src
RUN cd /src/models && git clone https://huggingface.co/SamLowe/roberta-base-go_emotions
RUN cd /src/models && git clone https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english
RUN pip install -r requirements.txt
RUN pip3 install torch==2.1.1+cpu torchvision==0.16.1+cpu torchaudio==2.1.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
CMD uvicorn src.app:app --host 0.0.0.0 --port ${PORT}
