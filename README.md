# GPT-NeoX-20b-bash-generator

This is an **experimental app** that uses the Huggingface Inference API with the `gpt-neox-20b` model to generate Bash code from requests given in natural language. From time to time it will be improved trying to get better and better results :)


## Try it

Inside `app.py` replace `<YOUR_ACCESS_TOKEN>` with your Huggingface's Access Token, then start the app with `python3 app.py`

To generate an access token register a new account at https://huggingface.co, confirm your email then, from your account go to Settings->Access Tokens and click on `New token` and generate a new token with a rule " read". Use your token to try and test the app.

when you start the app you will be asked `Print the Bash code needed to` ... complete the sentence with the action to be performed and see the result

![Screenshot from 2023-03-21 07-17-42](https://user-images.githubusercontent.com/114559605/226531917-94dcfdc8-3e45-4ef4-938f-604e49da5802.png)
