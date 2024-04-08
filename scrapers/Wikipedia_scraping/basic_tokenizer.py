from tokenizers import Tokenizer, models, pre_tokenizers, decoders, trainers

# our function defining how we will train the tokenizer
def train_tokenizer(text_file, vocab_size):
    # we will use a Byte-Pair Encoding (BPE) tokenizer
    tokenizer = Tokenizer(models.BPE())

    # some pre_tokenizer and decoder customization (taken from documentation)
    tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel()
    tokenizer.decoder = decoders.ByteLevel()

    # Train the tokenizer on the text data
    trainer = trainers.BpeTrainer(vocab_size=vocab_size, special_tokens=["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]"])
    tokenizer.train([text_file], trainer)

    return tokenizer

# function to use our trained tokenizer on a text file
def tokenize_text(text_file, tokenizer):
    # keep track of tokens
    tokens = []
    with open(text_file, 'r', encoding='utf-8') as f:
        # go through each line, strip whitespace
        for line in f:
            line = line.strip()
            if line:  # Ignore empty lines
                # encode the line and split into tokens using the encoded line
                encoded = tokenizer.encode(line)
                tokens.extend(encoded.tokens)
    return tokens

# Using the tokenizer on our wikipedia data
text_file_path = "wikipedia_data.txt" 
# looking online, 170,000 words in the english language are actively being used so we will use that number for 
# the tokenizer
vocab_size = 170000 
# train the tokenizer and then output the tokens
tokenizer = train_tokenizer(text_file_path, vocab_size)
tokens = tokenize_text(text_file_path, tokenizer)
print(tokens)
