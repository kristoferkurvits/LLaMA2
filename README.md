# LLaMA2

This is a very simple API interface for LLaMA2 model which works as a downstream LLM model for my [discord bot project](https://github.com/kristoferkurvits/discord).

## Setup
Start by downloading "llama-2-7b-chat.Q2_K.gguf" from [HuggingFace](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/tree/main) and store it together with the contents of this repository.

Then run
```
    pip install -r requirements.txt
    docker build -t llama2 .
    docker run -p 127.0.0.1:5000:5000 llama2
```

API available on http://127.0.0.1:5000/llama
[POST] example request body
 ```
 {
    "user_message": "What's the tallest mountain?",
    "system_message": "You are a smart assistant",
    "max_tokens": 100
}
```