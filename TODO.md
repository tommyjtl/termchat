# TO-DO

## Level 1

- [ ] Add `-q` option to ask an immediate question and get the answer
  - [ ] Parse the code, allow user to select which code snippet to use

- [ ] press `shift` to erase current input
- [x] copy the answer to clipboard
- [ ] interrupt a unresponsive request
- [ ] interrupt a too long response
- [ ] Add examples use cases
- [ ] Add Markdown support for terminal displaying

- [ ] Setup a `~/.config/termchat/` directory for storing character presets
- [ ] Add error exception when model API is not responding
  - retry with same previous chat context
```text
Enter your message: what spaceship are we in?
That model is currently overloaded with other requests. You can retry your request, or contact us through our help center at help.openai.com if the error persists. (Please include the request ID 68e572a183a8f9b1ab105972ff859e46 in your message.) (Error occurred while streaming.)
```
- [ ] copy latest answer to clipboard
- [ ] Add character customization to `chat.py`
  - Extract information from article/episode digest
  - Incorporate embedding comparison for the closest match in the given context
  - [reference 1](https://promptbase.com/prompt/chat-with-a-movieseriesgames-character)
- [ ] Able to load chat history from a chat history json
- [ ] Add response prefix, use the character name as the prefix

## Level 2

- [ ] Problem with PDF Q&A
  - Not considered the full context from the PDF, only chunks the relevent text
- [ ] Create a PyPI package as `termchat`
- [ ] Allow passing URL for online PDF files (or not?)
- [ ] Use KNN instead of the naive dot product for the closest match in the given context
- [ ] Streaming response for the chatbot [reference](https://til.simonwillison.net/gpt3/python-chatgpt-streaming-api)
- [x] Type `/exit` to terminate the program