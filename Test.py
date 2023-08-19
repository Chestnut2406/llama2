import replicate
output = replicate.run(
    "replicate/llama-2-70b:14ce4448d5e7e9ed0c37745ac46eca157aab09061f0c179ac2b323b5de56552b",
    input={"prompt": ...}
)
# The replicate/llama-2-70b model can stream output as it's running.
# The predict method returns an iterator, and you can iterate over that output.
for item in output:
    # https://replicate.com/replicate/llama-2-70b/versions/14ce4448d5e7e9ed0c37745ac46eca157aab09061f0c179ac2b323b5de56552b/api#output-schema
    print(item)